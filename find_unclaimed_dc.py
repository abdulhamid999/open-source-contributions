import subprocess
import json
import re

print("Fetching open DeepChem issues...")
cmd_issues = ["gh", "issue", "list", "--repo", "deepchem/deepchem", "--state", "open", "--limit", "100", "--json", "number,title,assignees,comments,labels,createdAt"]
issues = json.loads(subprocess.check_output(cmd_issues).decode())

print("Fetching recent DeepChem PRs...")
cmd_prs = ["gh", "pr", "list", "--repo", "deepchem/deepchem", "--state", "all", "--limit", "200", "--json", "number,title,body,headRefName,state"]
prs = json.loads(subprocess.check_output(cmd_prs).decode())

unclaimed = []
for iss in issues:
    num = iss["number"]
    if iss.get("assignees"):
        continue
    num_pattern = re.compile(rf"(?:#|\bissues/|\bissue/|\bgh-|\bfix/|\brefactor/|\bfeat/){num}\b", re.IGNORECASE)
    matching_prs = [p for p in prs if num_pattern.search(f"{p.get('title', '')} {p.get('headRefName', '')} {p.get('body', '')}") or f"#{num}" in f"{p.get('title', '')} {p.get('body', '')}"]
    if matching_prs:
        continue
    unclaimed.append(iss)

print(f"\nFound {len(unclaimed)} completely unclaimed DeepChem issues:")
for iss in unclaimed[:20]:
    comments = iss.get("comments", 0)
    print(f"#{iss['number']}: {iss['title']} (Comments: {comments})")

