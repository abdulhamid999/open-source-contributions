import subprocess
import json
import re

def main():
    print("Fetching open issues...")
    cmd_issues = ['gh', 'issue', 'list', '--repo', 'boa-dev/boa', '--state', 'open', '--limit', '100', '--json', 'number,title,assignees,comments,labels,createdAt']
    res_issues = subprocess.run(cmd_issues, capture_output=True, text=True)
    if res_issues.returncode != 0:
        print("Error fetching issues:", res_issues.stderr)
        return
    issues = json.loads(res_issues.stdout)
    print(f"Fetched {len(issues)} open issues.")

    print("Fetching recent PRs...")
    cmd_prs = ['gh', 'pr', 'list', '--repo', 'boa-dev/boa', '--state', 'all', '--limit', '200', '--json', 'number,title,body,headRefName,state']
    res_prs = subprocess.run(cmd_prs, capture_output=True, text=True)
    if res_prs.returncode != 0:
        print("Error fetching PRs:", res_prs.stderr)
        return
    prs = json.loads(res_prs.stdout)
    print(f"Fetched {len(prs)} PRs.")

    # Build reference mapping: issue number -> list of PRs
    # A PR references an issue if the issue number appears as #<num> or in title/body/branch
    unclaimed = []
    for iss in issues:
        num = iss['number']
        title = iss['title']
        assignees = [a['login'] for a in iss.get('assignees', [])]
        labels = [l['name'] for l in iss.get('labels', [])]

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

        unclaimed.append({
            'num': num,
            'title': title,
            'labels': labels,
            'comments': iss.get('comments', 0),
            'createdAt': iss.get('createdAt', '')
        })

    print(f"\nFound {len(unclaimed)} unclaimed open issues with NO PRs:")
    for item in unclaimed:
        print(f"#{item['num']}: {item['title']}")
        print(f"   Labels: {item['labels']} | Comments: {item['comments']} | Created: {item['createdAt']}")
        print(f"   URL: https://github.com/boa-dev/boa/issues/{item['num']}\n")

if __name__ == '__main__':
    main()

