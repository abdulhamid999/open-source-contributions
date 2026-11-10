import subprocess
import json
import time

def get_prs(num):
    for _ in range(3):
        try:
            cmd = ['gh', 'pr', 'list', '--repo', 'boa-dev/boa', '--search', str(num), '--state', 'all', '--json', 'number,title,state,headRefName']
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
            if res.returncode == 0 and res.stdout.strip():
                return json.loads(res.stdout)
        except Exception:
            time.sleep(1)
    return []

def main():
    cmd = ['gh', 'issue', 'list', '--repo', 'boa-dev/boa', '--state', 'open', '--limit', '80', '--json', 'number,title,assignees,comments,labels,createdAt']
    issues = json.loads(subprocess.run(cmd, capture_output=True, text=True).stdout)

    print(f"Auditing open issues 20 to 60...")
    for iss in issues[18:60]:
        num = iss['number']
        title = iss['title']
        assignees = [a['login'] for a in iss.get('assignees', [])]
        
        prs = get_prs(num)
        
        has_pr = len(prs) > 0
        pr_info = f"PR: #{prs[0]['number']} ({prs[0]['state']})" if has_pr else "NO PR"
        assignee_info = f"Assignee: {assignees[0]}" if assignees else "UNASSIGNED"
        
        print(f"#{num} [{pr_info}] [{assignee_info}]: {title} (Comments: {iss['comments']})")

if __name__ == '__main__':
    main()

