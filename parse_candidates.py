import json
import re

with open(r'C:\Users\admin\.gemini\antigravity\brain\f60a073a-e57f-4776-ab34-c8a4b41c13df\.system_generated\steps\698\output.txt', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
print(f"Total lines in output: {len(lines)}")
for line in lines:
    if line.startswith('#'):
        # extract issue number, title, and comments
        m = re.match(r'#(\d+):\s*(.*?)\s*\(Comments:\s*(.*?),\s*Labels:\s*(.*?)\)', line)
        if m:
            num, title, comments_raw, labels = m.groups()
            c_count = comments_raw.count("'id':") if comments_raw.startswith('[') else comments_raw
            print(f"#{num}: {title} | Comments: {c_count} | Labels: {labels}")

