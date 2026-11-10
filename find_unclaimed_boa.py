import subprocess
import json
import sys

def main():
    cmd = ['gh', 'issue', 'list', '--repo', 'boa-dev/boa', '--state', 'open', '--limit', '150', '--json', 'number,title,assignees,comments,labels,createdAt']
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("Error fetching issues:", res.stderr)
        return

    issues = json.loads(res.stdout)
    print(f"Total open issues fetched: {len(issues)}")

    unclaimed = []
    for iss in issues:
        num = iss['number']
        title = iss['title']
        assignees = [a['login'] for a in iss.get('assignees', [])]
        labels = [l['name'] for l in iss.get('labels', [])]

        if assignees:
            continue

        # Check if any PR links or mentions this issue
        pr_cmd = ['gh', 'pr', 'list', '--repo', 'boa-dev/boa', '--search', str(num), '--json', 'number,title,state']
        pr_res = subprocess.run(pr_cmd, capture_output=True, text=True)
        if pr_res.returncode != 0:
            continue
        prs = json.loads(pr_res.stdout)

        # If any PR mentions this issue, skip it
        if len(prs) > 0:
            continue

        unclaimed.append(iss)
        print(f"Unclaimed #{num}: {title}")
        print(f"   Labels: {labels} | Comments: {iss['comments']} | Created: {iss['createdAt']}")
        print(f"   URL: https://github.com/boa-dev/boa/issues/{num}\n")
        if len(unclaimed) >= 15:
            break

if __name__ == '__main__':
    main()
