import re

with open('_pages/about.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Debug prints to see what was read
print("Length of content:", len(content))

# Update intro paragraph using robust regex
old_intro_regex = r"I am a Master's student in Applied Math.*?google-scholar-stats.*?\)\."
new_intro = r"""I am a Master's student in Applied Math at Fudan University and an incoming CS Ph.D. student at Yale University, advised by Prof. [Rex Ying](https://scholar.google.cat/citations?user=6fqNXooAAAAJ&hl=ca). **My research focuses on Multimodal Structured Reasoning**, aiming to build systems that integrate explicit structural priors with dynamic reasoning capabilities. Currently, I am exploring principled reasoning frameworks in Vision-Language Models (VLMs), spatial-aware planning, and complex continuous representations. Feel free to reach out if you'd like to learn more about my work, chat, or explore potential collaborations. You can find my publications on my [google scholar](https://scholar.google.com/citations?user=1UKUQUEAAAAJ&hl=zh-CN)."""

content = re.sub(old_intro_regex, new_intro, content, flags=re.DOTALL)

# Update Publications introduction heavily replacing the section
pub_regex = r"# 📝 Selected Publications.*?## [^\n]+"
new_pub = r"""# 📝 Selected Publications

My research primarily focuses on **Multimodal Structured Reasoning**, along with other exploratory works in distribution modeling and vision foundation models.

## Multimodal Structured Reasoning"""
content = re.sub(pub_regex, new_pub, content, flags=re.DOTALL | re.MULTILINE)

# Also rename the second section (if it exists)
content = re.sub(r"## Safety and Verification in AI Systems", "## Other Explorations", content)

# Write back temporarily to check
with open('_pages/about.md', 'w', encoding='utf-8') as f:
    f.write(content)
print("Changes applied. New Length:", len(content))

