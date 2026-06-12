import re

with open('_pages/about.md', 'r') as f:
    text = f.read()

# Let's count how many badges we have and what they are
matches = re.findall(r'<div style="margin-top: 8px;">(.*?)</div>', text)
for i, m in enumerate(matches):
    print(f"Paper {i+1} tags:", re.findall(r'>([^<]+)</span>', m))
