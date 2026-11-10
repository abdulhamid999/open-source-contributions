import urllib.request
import json

for num in [5236, 5264, 5266]:
    url = f"https://api.github.com/repos/deepchem/deepchem/issues/{num}"
    req = urllib.request.Request(url, headers={"User-Agent": "GSoC-Contributor-Tool"})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            print(f"=== #{num}: {data['title']} ===")
            print(data['body'])
            print("\n" + "="*50 + "\n")
    except Exception as e:
        print(f"Error fetching #{num}: {e}")

