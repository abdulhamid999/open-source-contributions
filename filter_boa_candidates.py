import subprocess
import json
import re

def main():
    cmd_issues = ['gh', 'issue', 'list', '--repo', 'boa-dev/boa', '--state', 'open', '--limit', '100', '--json', 'number,title,assignees,comments,labels,createdAt']
    issues = json.loads(subprocess.run(cmd_issues, capture_output=True, text=True).stdout)

    cmd_prs = ['gh', 'pr', 'list', '--repo', 'boa-dev/boa', '--state', 'all', '--limit', '200', '--json', 'number,title,body,headRefName,state']
    prs = json.loads(subprocess.run(cmd_prs, capture_output=True, text=True).stdout)

    print("=== HIGH-POTENTIAL UNCLAIMED BOA ISSUES ===")
    for iss in issues:
        num = iss['number']
        title = iss['title']
        assignees = iss.get('assignees', [])
        if assignees:
            continue

        num_pattern = re.compile(rf'(?:#|\bissues/|\bissue/|\bgh-|\bfix/|\brefactor/|\bfeat/){num}\b', re.IGNORECASE)
        matching_prs = []
        for p in prs:
            search_str = f"{p.get('title', '')} {p.get('headRefName', '')} {p.get('body', '')}"
            if num_pattern.search(search_str) or f"#{num}" in search_str:
                matching_prs.append(p)

        if matching_prs:
            continue

        # Skip issues that are marked discussion or huge proposals
        labels = [l['name'] for l in iss.get('labels', [])]
        comments_count = iss.get('comments', 0)
        
        # We want issues that look like concrete bugs or feature gaps
        print(f"#{num}: {title} (Comments: {comments_count}, Labels: {labels})")

if __name__ == '__main__':
    main()

