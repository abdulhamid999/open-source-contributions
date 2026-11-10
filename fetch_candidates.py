import urllib.request
import json

def fetch_issues(repo, labels=None):
    url = f"https://api.github.com/repos/{repo}/issues?state=open&per_page=30"
    if labels:
        url += f"&labels={labels}"
    req = urllib.request.Request(url, headers={"User-Agent": "GSoC-Contributor-Tool"})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            issues = []
            for item in data:
                if "pull_request" in item:
                    continue
                issues.append({
                    "number": item["number"],
                    "title": item["title"],
                    "comments": item["comments"],
                    "assignees": [a["login"] for a in item.get("assignees", [])],
                    "labels": [l["name"] for l in item.get("labels", [])],
                    "html_url": item["html_url"],
                    "body": (item.get("body") or "")[:200]
                })
            return issues
    except Exception as e:
        print(f"Error fetching {repo}: {e}")
        return []

print("=== FOSSASIA/pslab-app open issues ===")
pslab_issues = fetch_issues("fossasia/pslab-app")
for iss in pslab_issues[:15]:
    assigned = iss["assignees"] if iss["assignees"] else "Unassigned"
    print(f"#{iss['number']}: {iss['title']} (Comments: {iss['comments']}, Assignee: {assigned})")
    print(f"   Labels: {iss['labels']}")
    print(f"   URL: {iss['html_url']}\n")

print("\n=== DeepChem/deepchem 'good first issue' ===")
dc_issues = fetch_issues("deepchem/deepchem", labels="good%20first%20issue")
for iss in dc_issues[:10]:
    assigned = iss["assignees"] if iss["assignees"] else "Unassigned"
    print(f"#{iss['number']}: {iss['title']} (Comments: {iss['comments']}, Assignee: {assigned})")
    print(f"   Labels: {iss['labels']}")
    print(f"   URL: {iss['html_url']}\n")

if not dc_issues:
    print("No 'good first issue' with that exact label, checking general open issues...")
    dc_general = fetch_issues("deepchem/deepchem")
    for iss in dc_general[:10]:
        assigned = iss["assignees"] if iss["assignees"] else "Unassigned"
        print(f"#{iss['number']}: {iss['title']} (Comments: {iss['comments']}, Assignee: {assigned})")
        print(f"   Labels: {iss['labels']}")
        print(f"   URL: {iss['html_url']}\n")

