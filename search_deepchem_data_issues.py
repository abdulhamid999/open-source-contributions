import urllib.request
import json

url = "https://api.github.com/repos/deepchem/deepchem/issues?state=open&per_page=100"
req = urllib.request.Request(url, headers={"User-Agent": "GSoC-Contributor-Tool"})
with urllib.request.urlopen(req) as resp:
    issues = json.loads(resp.read().decode())

print("=== Open DeepChem issues in dataset / featurizer ===")
for iss in issues:
    if "pull_request" in iss:
        continue
    title = iss["title"].lower()
    body = (iss.get("body") or "").lower()
    if any(k in title for k in ["featurizer", "dataset", "data", "feat", "loader", "split"]):
        assignee = iss["assignee"]["login"] if iss["assignee"] else "Unassigned"
        print(f"#{iss['number']}: {iss['title']} (Assignee: {assignee}, Comments: {iss['comments']})")
        print(f"   URL: {iss['html_url']}")

