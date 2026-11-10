import subprocess
import json

sub_issues = [5074, 5075, 5081, 5082, 5083, 5084, 5085, 5086, 5087, 5088]

for num in sub_issues:
    res = subprocess.run(['gh', 'issue', 'view', str(num), '--repo', 'boa-dev/boa', '--json', 'number,title,state,assignees,comments'], capture_output=True, text=True)
    if res.returncode == 0:
        data = json.loads(res.stdout)
        assignees = [a['login'] for a in data.get('assignees', [])]
        
        pr_res = subprocess.run(['gh', 'pr', 'list', '--repo', 'boa-dev/boa', '--search', str(num), '--json', 'number,title,state'], capture_output=True, text=True)
        prs = json.loads(pr_res.stdout) if pr_res.returncode == 0 else []
        pr_str = f"PR: #{prs[0]['number']} ({prs[0]['state']})" if prs else "NO PR"
        
        print(f"#{data['number']} [{data['state']}] [{pr_str}] Assignee: {assignees}: {data['title']}")

