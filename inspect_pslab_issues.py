import urllib.request
import json

for num in [3023, 3348, 3475, 3463]:
    url = f"https://api.github.com/repos/fossasia/pslab-app/issues/{num}"
    req = urllib.request.Request(url, headers={"User-Agent": "GSoC-Contributor-Tool"})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            print(f"=== #{num}: {data['title']} ===")
            print(f"State: {data['state']}, Assignee: {data.get('assignee')}")
            print(data['body'])
            print("\n" + "="*50 + "\n")
    except Exception as e:
        print(f"Error fetching #{num}: {e}")

