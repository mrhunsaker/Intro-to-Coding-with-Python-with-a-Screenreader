import os
import re
import shutil

ROOT = r"d:\GitHubRepos\Intro-to-Coding-with-Python-with-a-Screenreader"
pattern = re.compile(r"lessonpart3\.yml$", re.IGNORECASE)
content_re = re.compile(r"^content:\s*([>|][+-]?)\s*$")

backed = []
modified = []
skipped = []
errors = []

for dirpath, dirnames, filenames in os.walk(ROOT):
    for fn in filenames:
        if pattern.search(fn):
            fp = os.path.join(dirpath, fn)
            try:
                with open(fp, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                # backup
                bak = fp + '.bak'
                shutil.copy2(fp, bak)
                backed.append(bak)
                # find content
                cidx = None
                for i,l in enumerate(lines):
                    if content_re.match(l):
                        cidx = i
                        break
                if cidx is None:
                    skipped.append((fp, 'no content'))
                    continue
                # extract block
                j = cidx + 1
                block = []
                base_indent = None
                # skip initial empty lines
                while j < len(lines) and lines[j].strip() == '':
                    block.append('')
                    j += 1
                if j < len(lines) and re.match(r"^\s+", lines[j]):
                    base_indent = re.match(r"^(\s+)", lines[j]).group(1)
                else:
                    base_indent = '  '
                while j < len(lines):
                    line = lines[j]
                    if line.startswith(base_indent) or line.strip()=='':
                        if line.strip()=='':
                            block.append('')
                        else:
                            block.append(line[len(base_indent):].rstrip('\n'))
                        j += 1
                    else:
                        break
                if not block:
                    skipped.append((fp, 'empty content'))
                    continue
                # Remove possible existing tag line
                tag = '#file:lessonpart3.yml'
                idx_first = 0
                # find first non-empty
                for k,bl in enumerate(block):
                    if bl.strip()!='':
                        idx_first = k
                        break
                has_tag = (block[idx_first].strip() == tag)
                content_lines = block[idx_first+1:] if has_tag else block[idx_first:]
                # Split into paragraphs
                paras = []
                cur = []
                for line in content_lines:
                    if line.strip() == '':
                        if cur:
                            paras.append('\n'.join(cur).strip())
                            cur = []
                    else:
                        cur.append(line)
                if cur:
                    paras.append('\n'.join(cur).strip())
                # Build new block: keep tag on top
                new_block = []
                if has_tag:
                    new_block.append(tag)
                    new_block.append('')
                # For each paragraph, if it starts with code fence or header or list marker, keep as-is; else convert to single-line bullet
                for p in paras:
                    stripped = p.lstrip()
                    if stripped.startswith('```') or re.match(r"^#", stripped) or re.match(r"^[-*+]\s+", stripped) or re.match(r"^\d+\.\s+", stripped):
                        # preserve original paragraph lines
                        new_block.extend(p.split('\n'))
                        new_block.append('')
                    else:
                        # collapse internal newlines to spaces for bullet
                        one = ' '.join([ln.strip() for ln in p.split('\n') if ln.strip()!=''])
                        new_block.append(f'- {one}')
                        new_block.append('')
                # Write back with literal scalar
                lines[cidx] = 'content: |\n'
                indented = [base_indent + (l + '\n' if l!='' else '\n') for l in new_block]
                new_lines = lines[:cidx+1] + indented + lines[j:]
                with open(fp, 'w', encoding='utf-8') as f:
                    f.writelines(new_lines)
                modified.append(fp)
            except Exception as e:
                errors.append((fp, str(e)))

print('Backups:', len(backed))
print('Modified:', len(modified))
print('Skipped:', len(skipped))
print('Errors:', len(errors))
for s in skipped[:20]:
    print('S:', s[0], '-', s[1])
for e in errors[:20]:
    print('E:', e[0], '-', e[1])
