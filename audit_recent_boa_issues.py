import subprocess
import json

def main():
    cmd = ['gh', 'issue', 'list', '--repo', 'boa-dev/boa', '--state', 'open', '--limit', '40', '--json', 'number,title,assignees,comments,labels,createdAt']
    issues = json.loads(subprocess.run(cmd, capture_output=True, text=True).stdout)

    print(f"Auditing {len(issues)} recent open issues...")
    for iss in issues:
        num = iss['number']
        title = iss['title']
        assignees = [a['login'] for a in iss.get('assignees', [])]
        
        pr_cmd = ['gh', 'pr', 'list', '--repo', 'boa-dev/boa', '--search', str(num), '--state', 'all', '--json', 'number,title,state,headRefName']
        prs = json.loads(subprocess.run(pr_cmd, capture_output=True, text=True).stdout)
        
        # Check if any PR mentions this issue
        has_pr = len(prs) > 0
        pr_info = f"PR: #{prs[0]['number']} ({prs[0]['state']})" if has_pr else "NO PR"
        assignee_info = f"Assignee: {assignees[0]}" if assignees else "UNASSIGNED"
        
        print(f"#{num} [{pr_info}] [{assignee_info}]: {title}")

if __name__ == '__main__':
    main()

