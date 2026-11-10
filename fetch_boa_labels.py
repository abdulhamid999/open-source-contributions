import subprocess
import json

cmd = ["gh", "api", "repos/boa-dev/boa/labels?per_page=100"]
res = subprocess.run(cmd, capture_output=True, text=True)
labels = json.loads(res.stdout)

print("Matching labels in Boa:")
for l in labels:
    name = l["name"]
    if any(k in name.lower() for k in ["easy", "good", "first", "help", "beginner", "test"]):
        print(" -", name)

# Now check issues with E-Easy or C-Tests
cmd2 = ["gh", "api", "repos/boa-dev/boa/issues?state=open&labels=E-Easy&per_page=30"]
res2 = subprocess.run(cmd2, capture_output=True, text=True)
easy_issues = json.loads(res2.stdout)
print(f"\n=== Issues with 'E-Easy' ({len(easy_issues)} found) ===")
for item in easy_issues:
    if "pull_request" in item:
        continue
    assignee = item["assignee"]["login"] if item["assignee"] else "Unassigned"
    labels_list = [x["name"] for x in item.get("labels", [])]
    print(f"#{item['number']}: {item['title']} (Assignee: {assignee}, Comments: {item['comments']})")
    print(f"   Labels: {labels_list}")
    print(f"   URL: {item['html_url']}\n")

