import os
import re
import shutil

ROOT = r"d:\GitHubRepos\Intro-to-Coding-with-Python-with-a-Screenreader"
pattern = re.compile(r"lessonpart3\.yml$", re.IGNORECASE)
content_re = re.compile(r"^content:\s*([>|][+-]?)\s*$")

modified = []
skipped = []
backed = []
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
                # find content line
                content_idx = None
                for i,l in enumerate(lines):
                    if content_re.match(l):
                        content_idx = i
                        break
                if content_idx is None:
                    skipped.append((fp, 'no content scalar'))
                    continue
                # extract block
                block_lines = []
                j = content_idx + 1
                # determine base indent
                if j < len(lines) and re.match(r"^\s+", lines[j]):
                    base_indent = re.match(r"^(\s+)", lines[j]).group(1)
                else:
                    base_indent = '  '
                while j < len(lines):
                    line = lines[j]
                    if line.startswith(base_indent) or line.strip()=='':
                        # strip base indent if present
                        if line.strip()=='':
                            block_lines.append('')
                        else:
                            block_lines.append(line[len(base_indent):].rstrip('\n'))
                        j += 1
                    else:
                        break
                # first non-empty line
                first_nonempty = None
                for bl in block_lines:
                    if bl.strip()!='':
                        first_nonempty = bl.strip()
                        break
                tag = '#file:lessonpart3.yml'
                if first_nonempty == tag:
                    skipped.append((fp, 'tag present'))
                    continue
                # otherwise, prepend tag and blank line
                new_block = [tag, ''] + block_lines
                # write back with literal scalar '|'
                lines[content_idx] = 'content: |\n'
                indented = [base_indent + (l + '\n' if l!='' else '\n') for l in new_block]
                new_lines = lines[:content_idx+1] + indented + lines[j:]
                with open(fp, 'w', encoding='utf-8') as f:
                    f.writelines(new_lines)
                modified.append(fp)
            except Exception as e:
                errors.append((fp, str(e)))

print('Backups:', len(backed))
print('Modified:', len(modified))
print('Skipped:', len(skipped))
print('Errors:', len(errors))
for s in skipped[:50]:
    print('S:', s[0], '-', s[1])
for e in errors[:50]:
    print('E:', e[0], '-', e[1])
