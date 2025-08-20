import os
import re
import shutil

ROOT = r"d:\GitHubRepos\Intro-to-Coding-with-Python-with-a-Screenreader"
pattern_file = re.compile(r"lessonpart.*\.yml$", re.IGNORECASE)
pattern_content = re.compile(r"^content:\s*([>|][+-]?)\s*$")

backups = []
modified = []
skipped = []
errors = []

def extract_block(lines, idx):
    # lines[idx] is content: > or |
    block = []
    i = idx + 1
    # Determine indentation of first block line
    if i < len(lines) and re.match(r"^\s+", lines[i]):
        indent_match = re.match(r"^(\s+)", lines[i])
        base_indent = indent_match.group(1)
    else:
        base_indent = '  '
    while i < len(lines):
        line = lines[i]
        if line.startswith(base_indent) or (line.strip()=="" and line.startswith('\n')):
            # remove the base indent
            if line.strip() == '':
                block.append('')
            else:
                block.append(line[len(base_indent):].rstrip('\n'))
            i += 1
        else:
            break
    return block, i

# Heuristics to decide whether a text is already markdown
def is_markdown(text):
    if '```' in text:
        return True
    if re.search(r"^\s*#", text, re.MULTILINE):
        return True
    if re.search(r"^\s*[-*+]\s+\w+", text, re.MULTILINE):
        return True
    return False

# Heuristic to detect code-like lines
def looks_like_code(line):
    stripped = line.lstrip()
    return (stripped.startswith('def ') or stripped.startswith('class ') or
            'print(' in stripped or stripped.endswith(':') and ('    ' in line or '\t' in line) or
            re.match(r"^[ \t]{4,}\S", line) is not None or re.match(r"^\s*>>>", line) is not None)


def convert_to_markdown(block_lines):
    out = []
    i = 0
    n = len(block_lines)
    while i < n:
        line = block_lines[i]
        if line.strip() == '':
            out.append('')
            i += 1
            continue
        # Header: line ending with ':' and not starting with list marker
        if line.strip().endswith(':') and not re.match(r"^\s*[-*+]\s+", line):
            text = line.strip().rstrip(':').strip()
            # Promote to H2
            out.append('## ' + text)
            # skip possible following blank line
            i += 1
            continue
        # Detect code block: sequence of lines that look like code (indented or contain python tokens)
        if looks_like_code(line):
            # gather code block
            code_lines = []
            while i < n and (block_lines[i].strip() != '' and (re.match(r"^[ \t]{4,}", block_lines[i]) or looks_like_code(block_lines[i]))):
                # remove up to 4 leading spaces if present
                code_lines.append(re.sub(r"^\s{0,4}", '', block_lines[i]))
                i += 1
            # wrap in fenced block
            out.append('```python')
            out.extend(code_lines)
            out.append('```')
            continue
        # Numbered list normalization: convert leading '1.' or '1)' to '1.'
        m = re.match(r"^\s*(\d+)[\.)]\s+(.*)$", line)
        if m:
            num = m.group(1)
            rest = m.group(2)
            out.append(f"{num}. {rest}")
            i += 1
            continue
        # Bullet lists with leading '-' or '*' or '•'
        m2 = re.match(r"^\s*[-*•]\s+(.*)$", line)
        if m2:
            out.append('- ' + m2.group(1).strip())
            i += 1
            continue
        # Default: treat as paragraph line, join consecutive paragraph lines
        para_lines = [line.strip()]
        i += 1
        while i < n and block_lines[i].strip() != '':
            para_lines.append(block_lines[i].strip())
            i += 1
        out.append(' '.join(para_lines))
    # Ensure trailing newline
    return out

for dirpath, dirnames, filenames in os.walk(ROOT):
    for fn in filenames:
        if pattern_file.search(fn):
            fp = os.path.join(dirpath, fn)
            try:
                with open(fp, 'r', encoding='utf-8') as f:
                    lines = f.readlines()

                # create backup (overwrite existing bak)
                bak = fp + '.bak'
                shutil.copy2(fp, bak)
                backups.append(bak)

                # find content line
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
                    skipped.append((fp, 'already markdown'))
                    continue

                # convert
                new_block = convert_to_markdown(block_lines)

                # prepare new YAML block: keep original scalar modifiers but use |+
                orig = lines[content_idx]
                m = pattern_content.match(orig)
                scalar_suffix = ''
                if m:
                    suffix = m.group(1)
                    # keep + or - if present
                    if len(suffix) > 1:
                        scalar_suffix = suffix[1:]
                new_scalar = '|' + scalar_suffix
                lines[content_idx] = f"content: {new_scalar}\n"

                # build indented block lines (2 spaces indent)
                new_block_indented = ["  " + l + '\n' for l in new_block]
                # write new file: keep everything before content_idx+1, then insert new block and remaining lines after end_idx
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
for s in skipped[:20]:
    print('S:', s[0], '-', s[1])
for e in errors[:20]:
    print('E:', e[0], '-', e[1])
