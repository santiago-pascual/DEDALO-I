"""Strict manifest, syntax, relative Markdown links and limited secret checks."""
from pathlib import Path
import ast, hashlib, re, sys
ROOT=Path(__file__).resolve().parents[1]
MANIFEST='PUBLICATION_MANIFEST.md'

def inventory(root):
    files={}
    for p in root.rglob('*'):
        rel=p.relative_to(root)
        if any(part in {'.git','__pycache__','.venv'} for part in rel.parts): continue
        if p.is_symlink(): raise ValueError(f'Symlink: {rel}')
        if p.is_file(): files[rel.as_posix()]=p
    return files

def validate(root=ROOT):
    files=inventory(root); manifest=files.pop(MANIFEST).read_text(encoding='utf-8')
    entries=re.findall(r'^\| `([^`]+)` \| `([0-9a-f]{64})` \|$',manifest,re.M)
    expected=dict(entries)
    if len(entries)!=len(expected) or set(expected)!=set(files): raise ValueError(f'Manifest mismatch: missing={set(expected)-set(files)} unexpected={set(files)-set(expected)}')
    patterns=[r'gh[pousr]_[A-Za-z0-9]{30,}',r'github_pat_[A-Za-z0-9_]{30,}',r'AKIA[0-9A-Z]{16}',r'-----BEGIN [A-Z ]*PRIVATE KEY-----',r'\b\d{8,12}:[A-Za-z0-9_-]{30,}\b',r'(?i)(?:api[_-]?key|password|secret|token)\s*[:=]\s*[\x22\x27][A-Za-z0-9_+/=-]{16,}[\x22\x27]',r'(?i)[A-Z]:\\Users\\[^\\\s]+',r'/home/[^/\s]+/']
    # Skip scanner's own pattern definitions for pattern matching, not hash/syntax.
    for name,p in files.items():
        if hashlib.sha256(p.read_bytes()).hexdigest()!=expected[name]: raise ValueError(f'Hash mismatch: {name}')
        if p.suffix not in {'.md','.py','.svg','.yml','.cff',''} or p.name.startswith('.env') or any(x in name.lower() for x in ('checkpoint','journal','credentials','private_key')): raise ValueError(f'Unexpected file type/name: {name}')
        s=p.read_text(encoding='utf-8')
        if name!='scripts/validate_publication.py' and any(re.search(q,s) for q in patterns): raise ValueError(f'Sensitive pattern: {name}')
        if p.suffix=='.py': ast.parse(s,filename=name)
        if p.suffix=='.md':
            for dest in re.findall(r'\]\(([^)]+)\)',s):
                if dest.startswith(('https://','http://','mailto:','#')): continue
                target=(p.parent/dest.split('#')[0]).resolve()
                if not target.is_relative_to(root.resolve()) or not target.is_file(): raise ValueError(f'Broken relative link: {name}: {dest}')
    for dest in re.findall(r'\]\(([^)]+)\)',manifest):
        if not dest.startswith(('https://','http://','#')) and not (root/dest.split('#')[0]).is_file(): raise ValueError(f'Broken manifest link: {dest}')
    return len(files)
if __name__=='__main__':
    try: print(f'Publication validation PASS: {validate()} hashed files')
    except (ValueError,OSError,SyntaxError) as exc: sys.exit(str(exc))
