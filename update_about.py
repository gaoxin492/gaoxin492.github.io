import re

with open('_pages/about.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Update intro paragraph
old_intro_regex = r"I am a Master's student in Applied Math.*?(?=\s*</div>)"
new_intro = r"""I am a Master's student in Applied Math at Fudan University and an incoming CS Ph.D. student at Yale University, advised by Prof. [Rex Ying](https://scholar.google.cat/citations?user=6fqNXooAAAAJ&hl=ca). **My research focuses on Multimodal Structured Reasoning**, aiming to build systems that integrate explicit structural priors with dynamic reasoning capabilities. Currently, I am exploring principled reasoning frameworks in Vision-Language Models (VLMs), spatial-aware planning, and complex continuous representations. Feel free to reach out if you'd like to learn more about my work, chat, or explore potential collaborations. You can find my publications on my [google scholar](https://scholar.google.com/citations?user=1UKUQUEAAAAJ&hl=zh-CN)."""

content = re.sub(old_intro_regex, new_intro, content, flags=re.DOTALL)

# Update Publications introduction
old_pub_intro = r"# 📝 Selected Publications\n\nMy research primarily focus on two directions: \*\*Robust Representation in Complex Environments\*\* and \*\*Safety and Verification in AI Systems\*\*\.\n\n## Robust Representation in Complex Environments"
new_pub_intro = r"""# 📝 Selected Publications

My research primarily focuses on **Multimodal Structured Reasoning**, along with other exploratory works in distribution modeling and vision foundation models.

## Multimodal Structured Reasoning"""
content = content.replace(old_pub_intro, new_pub_intro)

# Rename the second section
content = content.replace("## Safety and Verification in AI Systems", "## Other Explorations")

# Keywords styling
def get_keywords_html(keywords):
    tags = ''.join([f'<span style="background-color: #f1f8ff; color: #0366d6; padding: 2px 6px; border-radius: 3px; font-size: 0.85em; border: 1px solid #c8e1ff; margin-right: 6px;">{k}</span>' for k in keywords])
    return f'\n\n<div style="margin-top: 8px;">{tags}</div>\n'

# Adding keywords to papers. We can match the title lines to insert keywords right after the author lists or at the end of the - bullet point.
# "MVP"
content = content.replace("**Xin Gao**, Jian Pu", "**Xin Gao**, Jian Pu" + get_keywords_html(["Distribution Modeling", "Multi-view Learning", "VAE"]))

# "MacTok"
content = content.replace("**Hengyu Zeng#**, **Xin Gao#**, Guanghao Li, Yuxiang Yan, Jiaoyang Ruan, Junpeng Ma, Haoyu Albert Wang, Jian Pu", "**Hengyu Zeng#**, **Xin Gao#**, Guanghao Li, Yuxiang Yan, Jiaoyang Ruan, Junpeng Ma, Haoyu Albert Wang, Jian Pu" + get_keywords_html(["Continuous Tokenization", "Representation", "Image Generation"]))

# "IVQ"
content = content.replace("Shujian Gao, Yuan Wang, Chenglong Ma, **Xin Gao**, Jiangtao Yan, Junzhi Ning, Cheng Tang, Changkai Ji, Huihui Xu, Wei Li, Ziyan Huang et al.", "Shujian Gao, Yuan Wang, Chenglong Ma, **Xin Gao**, Jiangtao Yan, Junzhi Ning, Cheng Tang, Changkai Ji, Huihui Xu, Wei Li, Ziyan Huang et al." + get_keywords_html(["Concept Bottleneck", "Interpretability", "Vector Quantization"]))

# "OrderMind"
content = content.replace("Yuxiang Yan, Zhiyuan Zhou, **Xin Gao**, Guanghao Li, Shenglin Li, Jiaqi Chen, Qunyan Pu, Jian Pu", "Yuxiang Yan, Zhiyuan Zhou, **Xin Gao**, Guanghao Li, Shenglin Li, Jiaqi Chen, Qunyan Pu, Jian Pu" + get_keywords_html(["Spatial Reasoning", "VLM", "Robotic Manipulation"]))

# "ARTDECO"
content = content.replace("Guanghao Li, Kerui Ren, Linning Xu, Zhewen Zheng, Changjian Jiang, **Xin Gao**, Bo Dai, Jian Pu, Mulin Yu, Jiangmiao Pang", "Guanghao Li, Kerui Ren, Linning Xu, Zhewen Zheng, Changjian Jiang, **Xin Gao**, Bo Dai, Jian Pu, Mulin Yu, Jiangmiao Pang" + get_keywords_html(["3D Gaussian Splatting", "Structure", "SLAM"]))

# "GOOD"
content = content.replace("**Xin Gao**, Jiyao Liu, Guanghao Li, Yueming Lyu, Jianxiong Gao, Weichen Yu, Ningsheng Xu, Liang Wang, Caifeng Shan, Ziwei Liu, Chenyang Si", "**Xin Gao**, Jiyao Liu, Guanghao Li, Yueming Lyu, Jianxiong Gao, Weichen Yu, Ningsheng Xu, Liang Wang, Caifeng Shan, Ziwei Liu, Chenyang Si" + get_keywords_html(["Diffusion Models", "OOD Detection"]))

# "Dark-ISP"
content = content.replace("**Jiasheng Guo#**, **Xin Gao#**, Yuxiang Yan, Guanghao Li, Jian Pu", "**Jiasheng Guo#**, **Xin Gao#**, Yuxiang Yan, Guanghao Li, Jian Pu" + get_keywords_html(["RAW Processing", "Low-Light", "Object Detection"]))

# "Loong"
content = content.replace("Xingyue Huang, Rishabh, Gregor Franke, Ziyi Yang, Jiamu Bai, Weijie Bai, Jinhe Bi, Zifeng Ding, Yiqun Duan, Chengyu Fan, Wendong Fan, **Xin Gao** et al.", "Xingyue Huang, Rishabh, Gregor Franke, Ziyi Yang, Jiamu Bai, Weijie Bai, Jinhe Bi, Zifeng Ding, Yiqun Duan, Chengyu Fan, Wendong Fan, **Xin Gao** et al." + get_keywords_html(["Large Language Models", "Structured Reasoning", "RL"]))

with open('_pages/about.md', 'w', encoding='utf-8') as f:
    f.write(content)
