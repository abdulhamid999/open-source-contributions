import subprocess
import json
import time

for attempt in range(5):
    try:
        res = subprocess.run(['gh', 'issue', 'view', '4350', '--repo', 'boa-dev/boa'], capture_output=True, text=True, timeout=20)
        if res.returncode == 0:
            print(res.stdout)
            break
        else:
            print(f"Attempt {attempt+1} error: {res.stderr}")
    except Exception as e:
        print(f"Attempt {attempt+1} exception: {e}")
    time.sleep(2)

