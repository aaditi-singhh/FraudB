import re
import urllib.request
import sys

with open('deploy_output.txt', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

match = re.search(r'(https://fraudb[^ \n\r\t]+\.vercel\.app)', content)
if match:
    url = match.group(1)
    print(f"URL: {url}")
    try:
        req = urllib.request.Request(url, method='HEAD')
        res = urllib.request.urlopen(req)
        print(f"Status: {res.status}")
    except Exception as e:
        print(f"Error checking url: {e}")
else:
    print("No URL found")
