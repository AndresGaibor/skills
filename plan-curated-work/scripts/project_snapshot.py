#!/usr/bin/env python3
"""Worker-only mechanical Git snapshot. No content extraction or semantic claims."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
from datetime import datetime, timezone


def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args], stderr=subprocess.PIPE)


def snapshot(repo):
    repo = Path(git(repo, 'rev-parse', '--show-toplevel').decode().strip()).resolve()
    status_before = git(repo, 'status', '--porcelain=v1', '-z')
    head_before = git(repo, 'rev-parse', '--verify', 'HEAD').decode().strip()
    names = sorted(set(git(repo, 'ls-files', '-z', '--cached', '--others', '--exclude-standard').split(b'\0')) - {b''})
    entries = []
    unstable = []
    for raw in names:
        relative = os.fsdecode(raw)
        path = repo / relative
        if path.is_symlink():
            entries.append({'path': relative, 'kind': 'symlink', 'content_read': False})
            continue
        if not path.exists():
            entries.append({'path': relative, 'kind': 'missing'})
            continue
        if not path.is_file():
            entries.append({'path': relative, 'kind': 'non-file'})
            continue
        try:
            before = path.stat()
            digest = hashlib.sha256()
            with path.open('rb') as stream:
                for chunk in iter(lambda: stream.read(1024 * 1024), b''):
                    digest.update(chunk)
            after = path.stat()
            if (before.st_mtime_ns, before.st_size, before.st_ino) != (after.st_mtime_ns, after.st_size, after.st_ino):
                unstable.append(relative)
            entries.append({'path': relative, 'kind': 'file', 'bytes': after.st_size, 'sha256': digest.hexdigest()})
        except FileNotFoundError:
            unstable.append(relative)
            entries.append({'path': relative, 'kind': 'changed-during-snapshot'})
    status_after = git(repo, 'status', '--porcelain=v1', '-z')
    head_after = git(repo, 'rev-parse', '--verify', 'HEAD').decode().strip()
    dirty = bool(status_after)
    return {
        'schema_version': 1,
        'generated_at_utc': datetime.now(timezone.utc).isoformat(),
        'repo_root': str(repo), 'commit': head_after,
        'branch': git(repo, 'branch', '--show-current').decode().strip(),
        'dirty': dirty,
        'status_porcelain_z': status_after.decode('utf-8', errors='replace'),
        'files': entries,
        'unstable_files': unstable,
        'identity_changed_during_snapshot': head_before != head_after or status_before != status_after,
        'consistency': 'best-effort; not an atomic snapshot; revalidate selected source hashes before handoff',
        'semantic_index': False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    data = snapshot(args.repo.resolve())
    output = args.output.resolve()
    repo = Path(data['repo_root'])
    if output == repo or repo in output.parents:
        parser.error('--output must be outside the repository to avoid indexing itself')
    if output.exists():
        parser.error('--output must be a new delivery path; refusing overwrite')
    output.parent.mkdir(parents=True, exist_ok=True)
    # Hard-link publication is atomic and refuses concurrent overwrite on local filesystems.
    fd, temp = tempfile.mkstemp(prefix='.snapshot-', dir=output.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as stream:
            json.dump(data, stream, ensure_ascii=True, indent=2)
            stream.write('\n')
        os.link(temp, output)
    finally:
        os.unlink(temp)
    print(json.dumps({'output': str(output), 'files': len(data['files']), 'dirty': data['dirty'], 'unstable': bool(data['unstable_files']) or data['identity_changed_during_snapshot']}))


if __name__ == '__main__':
    main()
