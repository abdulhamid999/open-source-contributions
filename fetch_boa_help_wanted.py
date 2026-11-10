import subprocess
import json

cmd = ["gh", "api", "repos/boa-dev/boa/issues?state=open&labels=Help%20Wanted&per_page=30"]
res = subprocess.run(cmd, capture_output=True, text=True)
issues = json.loads(res.stdout)

print(f"=== Boa 'Help Wanted' issues ({len(issues)} found) ===")
for item in issues:
    if "pull_request" in item:
        continue
    assignee = item["assignee"]["login"] if item["assignee"] else "Unassigned"
    labels = [l["name"] for l in item.get("labels", [])]
    print(f"#{item['number']}: {item['title']} (Assignee: {assignee}, Comments: {item['comments']})")
    print(f"   Labels: {labels}")
    print(f"   URL: {item['html_url']}\n")

