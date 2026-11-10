with open(r'C:\OpenSource\boa\cli\src\main.rs', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines, 1):
    if '.unwrap()' in line or '.expect(' in line:
        print(f"{i}: {line.strip()}")

