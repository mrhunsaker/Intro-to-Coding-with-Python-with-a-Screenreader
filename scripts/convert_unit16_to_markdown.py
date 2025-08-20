import os
import re
import shutil

ROOT = r"d:\GitHubRepos\Intro-to-Coding-with-Python-with-a-Screenreader\unit16"
pattern_file = re.compile(r"lessonpart.*\.yml$", re.IGNORECASE)
pattern_content = re.compile(r"^content:\s*([>|][+-]?)\s*$")

backups = []
modified = []
skipped = []
errors = []

def extract_block(lines, idx):
    block = []
    i = idx + 1
    # indent of first non-empty block line
    base_indent = None
    while i < len(lines) and lines[i].strip() == '':
        block.append('')
        i += 1
    if i < len(lines) and re.match(r"^\s+", lines[i]):
        match = re.match(r"^(\s+)", lines[i])
        base_indent = match.group(1)
    else:
        base_indent = '  '
    while i < len(lines):
        line = lines[i]
        if line.startswith(base_indent) or line.strip() == '':
            # strip base indent
            if line.strip() == '':
                block.append('')
            else:
                block.append(line[len(base_indent):].rstrip('\n'))
            i += 1
        else:
            break
    return block, i

def is_markdown(text):
    if '```' in text:
        return True
    if re.search(r"^\s*#", text, re.MULTILINE):
        return True
    return False

def looks_like_code(line):
    stripped = line.lstrip()
    return (stripped.startswith('def ') or stripped.startswith('class ') or
            'print(' in stripped or stripped.endswith(':') and ('    ' in line or '\t' in line) or
            re.match(r"^[ \t]{4,}\S", line) is not None or re.match(r"^\s*>>>", line) is not None)

def convert_block(block_lines):
    out = []
    i = 0
    n = len(block_lines)
    while i < n:
        line = block_lines[i]
        if line.strip() == '':
            out.append('')
            i += 1
            continue
        # Header pattern like 'A.1 Title' -> convert to '## Title'
        m = re.match(r"^\s*A\.\d+(?:\.\d+)?\s+(.*)$", line)
        if m:
            out.append('## ' + m.group(1).strip())
            i += 1
            continue
        # Code block detection
        if looks_like_code(line):
            code_lines = []
            while i < n and (block_lines[i].strip() != '' and (re.match(r"^[ \t]{4,}", block_lines[i]) or looks_like_code(block_lines[i]))):
                code_lines.append(re.sub(r"^\s{0,4}", '', block_lines[i]))
                i += 1
            out.append('```python')
            out.extend(code_lines)
            out.append('```')
            continue
        # Bullet list markers 
- or 
	- -> convert to -
        m2 = re.match(r"^\s*[•◦]\s*(.*)$", line)
        if m2:
            out.append('- ' + m2.group(1).strip())
            i += 1
            continue
        # Default paragraph assembly
        para = [line.strip()]
        i += 1
        while i < n and block_lines[i].strip() != '':
            para.append(block_lines[i].strip())
            i += 1
        out.append(' '.join(para))
    return out

for dirpath, dirnames, filenames in os.walk(ROOT):
    for fn in filenames:
        if pattern_file.search(fn):
            fp = os.path.join(dirpath, fn)
            try:
                with open(fp, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                bak = fp + '.bak'
                shutil.copy2(fp, bak)
                backups.append(bak)
                # find content
                content_idx = None
                for idx, line in enumerate(lines):
                    if pattern_content.match(line):
                        content_idx = idx
                        break
                if content_idx is None:
                    skipped.append((fp, 'no content scalar'))
                    continue
                block_lines, end_idx = extract_block(lines, content_idx)
                if not block_lines:
                    skipped.append((fp, 'empty content'))
                    continue
                block_text = '\n'.join(block_lines)
                if is_markdown(block_text):
                    # ensure scalar is literal |
                    orig = lines[content_idx]
                    if '|' in orig:
                        skipped.append((fp, 'already markdown scalar'))
                        continue
                    else:
                        lines[content_idx] = re.sub(r"^content:\s*[>|][+-]?\s*$", 'content: |\n', lines[content_idx])
                        with open(fp, 'w', encoding='utf-8') as f:
                            f.writelines(lines)
                        modified.append(fp)
                        continue
                # convert to markdown
                new_block = convert_block(block_lines)
                lines[content_idx] = 'content: |\n'
                new_block_indented = ['  ' + l + '\n' for l in new_block]
                new_lines = lines[:content_idx+1] + new_block_indented + lines[end_idx:]
                with open(fp, 'w', encoding='utf-8') as f:
                    f.writelines(new_lines)
                modified.append(fp)
            except Exception as e:
                errors.append((fp, str(e)))

print('Backups:', len(backups))
print('Modified:', len(modified))
print('Skipped:', len(skipped))
print('Errors:', len(errors))
for s in skipped:
    print('S:', s[0], '-', s[1])
for e in errors:
    print('E:', e[0], '-', e[1])
