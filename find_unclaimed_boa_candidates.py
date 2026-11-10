import json
import subprocess

try:
    with open(r"C:\OpenSource\boa_issues_50.json", "r", encoding="utf-16") as f:
        issues = json.load(f)
except Exception:
    with open(r"C:\OpenSource\boa_issues_50.json", "r", encoding="utf-8-sig") as f:
        issues = json.load(f)

print(f"Total issues loaded: {len(issues)}")

for issue in issues:
    num = issue["number"]
    title = issue["title"]
    assignees = issue.get("assignees", [])
    comments = issue.get("comments", [])
    
    # If assigned, skip
    if assignees:
        continue
    
    # Check if someone in comments volunteered
    volunteered = False
    for c in comments:
        body = c.get("body", "").lower()
        if any(w in body for w in ["i'll work", "i will work", "can i work", "working on this", "claim", "i would like to work", "take this"]):
            volunteered = True
            break
    if volunteered:
        continue
    
    # Check if there is any PR for this issue
    cmd = ["gh", "pr", "list", "--repo", "boa-dev/boa", "--search", str(num), "--state", "all", "--json", "number,state,title"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        prs = json.loads(res.stdout)
        if len(prs) == 0:
            print(f"Candidate #{num}: {title} (Comments: {len(comments)})")
