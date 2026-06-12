import re

with open('_pages/about.md', 'r', encoding='utf-8') as f:
    text = f.read()

# We want to add a news line for BMC.
# BMC is ICML 2026. The latest news is 2026.03 CVPR.
new_news = "- *2026.05*: [BMC](https://arxiv.org/abs/TBD) accepted to **ICML 2026**.\n"

if "*2026.05*: [BMC]" not in text:
    # Insert it right after `<div class="news-window" markdown="1">\n`
    # or before `- *2026.03*:`
    text = text.replace('<div class="news-window" markdown="1">\n', '<div class="news-window" markdown="1">\n' + new_news)
    with open('_pages/about.md', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Added to news")
