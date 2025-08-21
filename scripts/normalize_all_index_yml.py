import os
import re
import shutil

ROOT = r"d:\GitHubRepos\Intro-to-Coding-with-Python-with-a-Screenreader"
pattern = re.compile(r"index\.yml$", re.IGNORECASE)
desc_re = re.compile(r"^description:\s*([>|][+-]?)\s*$")
lessonparts_re = re.compile(r"^lessonParts:\s*$")

backups = []
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
                bak = fp + '.bak'
                shutil.copy2(fp, bak)
                backups.append(bak)

                changed = False
                # handle description
                for i, line in enumerate(lines):
                    m = desc_re.match(line)
                    if m:
                        # extract block
                        j = i + 1
                        block = []
                        # detect base indent
                        if j < len(lines) and re.match(r"^\s+", lines[j]):
                            base = re.match(r"^(\s+)", lines[j]).group(1)
                        else:
                            base = '  '
                        while j < len(lines):
                            if lines[j].startswith(base) or lines[j].strip()=='':
                                # strip base indent
                                if lines[j].strip()=='':
                                    block.append('')
                                else:
                                    block.append(lines[j][len(base):].rstrip('\n'))
                                j += 1
                            else:
                                break
                        # rewrite as literal '|'
                        lines[i] = 'description: |\n'
                        new_block = [base + (b + '\n' if b!='' else '\n') for b in block]
                        lines = lines[:i+1] + new_block + lines[j:]
                        changed = True
                        break
                # handle lessonParts
                for i, line in enumerate(lines):
                    if lessonparts_re.match(line):
                        j = i + 1
                        items = []
                        while j < len(lines) and (lines[j].startswith(' ') or lines[j].strip()==''):
                            s = lines[j].strip()
                            if s.startswith('-'):
                                item = s.lstrip('-').strip()
                                if item:
                                    items.append(item)
                            elif s!='':
                                # maybe plain scalar, add
                                items.append(s)
                            j += 1
                        # if items is empty, skip
                        if items:
                            new_lines = [lines[i]]
                            for it in items:
                                new_lines.append('  - ' + it + '\n')
                            lines = lines[:i] + new_lines + lines[j:]
                            changed = True
                        break
                if changed:
                    with open(fp, 'w', encoding='utf-8') as f:
                        f.writelines(lines)
                    modified.append(fp)
                else:
                    skipped.append(fp)
            except Exception as e:
                errors.append((fp, str(e)))

print('Backups:', len(backups))
print('Modified:', len(modified))
print('Skipped:', len(skipped))
print('Errors:', len(errors))
for e in errors[:20]:
    print('E:', e[0], '-', e[1])
