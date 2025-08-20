import os
import re

ROOT = r"d:\GitHubRepos\Intro-to-Coding-with-Python-with-a-Screenreader"
pattern_file = re.compile(r"lessonpart.*\.yml$", re.IGNORECASE)
pattern_content_line = re.compile(r"^content:\s*([>|][+-]?)\s*$")

modified = []
skipped = []
backups = []
errors = []

for dirpath, dirnames, filenames in os.walk(ROOT):
    for fn in filenames:
        if pattern_file.search(fn):
            fp = os.path.join(dirpath, fn)
            try:
                with open(fp, 'r', encoding='utf-8') as f:
                    lines = f.readlines()

                # create backup
                bak_path = fp + '.bak'
                with open(bak_path, 'w', encoding='utf-8') as b:
                    b.writelines(lines)
                backups.append(bak_path)

                # find content: line
                i = 0
                found = False
                for idx, line in enumerate(lines):
                    if pattern_content_line.match(line):
                        i = idx
                        found = True
                        break
                if not found:
                    skipped.append((fp, 'no content block'))
                    continue

                # collect block lines after content:
                block_lines = []
                for j in range(i+1, len(lines)):
                    l = lines[j]
                    # if line starts with space(s), consider part of block
                    if re.match(r"^\s+", l):
                        block_lines.append(l)
                    else:
                        break

                block_text = ''.join([l.lstrip('\n') if l.strip()=='' else l for l in block_lines])
                # Heuristic: if block already contains markdown markers, skip modifying content but backup already made
                if ('```' in block_text) or re.search(r'^\s*#', block_text, re.MULTILINE):
                    skipped.append((fp, 'already markdown'))
                    continue

                # otherwise, change the scalar indicator from > to | (preserve any + or -)
                orig_line = lines[i]
                m = pattern_content_line.match(orig_line)
                if not m:
                    skipped.append((fp, 'content line parse failed'))
                    continue
                scalar = m.group(1)
                if scalar.startswith('|'):
                    skipped.append((fp, 'already literal'))
                    continue
                new_scalar = '|' + scalar[1:]
                lines[i] = re.sub(r"^content:\s*[>|][+-]?\s*$", f"content: {new_scalar}\n", orig_line)

                # write back
                with open(fp, 'w', encoding='utf-8') as f:
                    f.writelines(lines)

                modified.append(fp)
            except Exception as e:
                errors.append((fp, str(e)))

print('Backups created:', len(backups))
print('Modified:', len(modified))
print('Skipped:', len(skipped))
print('Errors:', len(errors))
for s in skipped[:20]:
    print('S:', s[0], '-', s[1])
for e in errors[:20]:
    print('E:', e[0], '-', e[1])
