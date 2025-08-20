import os
import re

ROOT = r"d:\GitHubRepos\Intro-to-Coding-with-Python-with-a-Screenreader"
pattern = re.compile(r"unit(\d+)[\\/]+lesson(\d+)", re.IGNORECASE)

modified = []
skipped = []
errors = []

for dirpath, dirnames, filenames in os.walk(ROOT):
    for fn in filenames:
        if fn.lower() == 'lessonpart2.yml':
            fp = os.path.join(dirpath, fn)
            try:
                with open(fp, 'r', encoding='utf-8') as f:
                    txt = f.read()
                if 'showEditor:' in txt:
                    skipped.append(fp)
                    continue
                m = pattern.search(fp.replace('\\\\', '\\'))
                if not m:
                    errors.append((fp, 'unit/lesson pattern not found'))
                    continue
                unit = int(m.group(1))
                lesson = int(m.group(2))
                a = unit - 1
                editor_path = f"course1/unit{unit}/lesson{lesson}/lessonpart2/Lesson{a}_{lesson}.py"
                append_block = '\nshowEditor: true\neditors:\n  - ' + editor_path + '\n'
                # Ensure file ends with a newline before appending
                if not txt.endswith('\n'):
                    txt = txt + '\n'
                txt = txt + append_block
                with open(fp, 'w', encoding='utf-8') as f:
                    f.write(txt)
                modified.append((fp, editor_path))
            except Exception as e:
                errors.append((fp, str(e)))

print('Modified:', len(modified))
for p, e in modified[:50]:
    print('+', p, '->', e)
print('Skipped (already had showEditor):', len(skipped))
print('Errors:', len(errors))
for p, msg in errors[:50]:
    print('!', p, msg)
