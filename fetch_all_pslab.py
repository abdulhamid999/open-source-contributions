import urllib.request
import json

def fetch_all_issues(repo):
    issues = []
    page = 1
    while True:
        url = f"https://api.github.com/repos/{repo}/issues?state=open&per_page=100&page={page}"
        req = urllib.request.Request(url, headers={"User-Agent": "GSoC-Contributor-Tool"})
        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode())
                if not data:
                    break
                for item in data:
                    if "pull_request" in item:
                        continue
                    issues.append(item)
                if len(data) < 100:
                    break
                page += 1
        except Exception as e:
            print(f"Error on page {page}: {e}")
            break
    return issues

issues = fetch_all_issues("fossasia/pslab-app")
print(f"Total open issues in pslab-app: {len(issues)}")
for item in issues:
    labels = [l["name"] for l in item.get("labels", [])]
    assignee = item.get("assignee")
    assignee_name = assignee["login"] if assignee else "None"
    print(f"#{item['number']}: {item['title']} | Labels: {labels} | Assignee: {assignee_name}")

