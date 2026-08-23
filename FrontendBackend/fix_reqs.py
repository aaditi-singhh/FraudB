import codecs

with open('requirements.txt', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

clean_lines = []
for line in lines:
    line = line.replace('\x00', '')
    if line.strip():
        clean_lines.append(line.strip())

with open('requirements.txt', 'w', encoding='utf-8') as f:
    for line in clean_lines:
        f.write(line + '\n')
