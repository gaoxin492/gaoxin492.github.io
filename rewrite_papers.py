import re

with open('_pages/about.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Define paper blocks explicitly to avoid regex messes
papers = {
    "MVP": """<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2025</div><img src='images/2025_01_MVP/MVP_Pipeline.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MVP: Deep Incomplete Multi-view Learning via Cyclic Permutation of VAEs](https://openreview.net/pdf?id=s4MwstmB8o)

 **Xin Gao**, Jian Pu

<div style="margin-top: 8px;"><span class="keyword-badge">Distribution Modeling</span><span class="keyword-badge">Multi-view Learning</span><span class="keyword-badge">VAE</span></div>

[![GitHub Stars](https://img.shields.io/github/stars/gaoxin492/MVP?style=social)](https://github.com/gaoxin492/MVP)
[![GitHub Forks](https://img.shields.io/github/forks/gaoxin492/MVP?style=social)](https://github.com/gaoxin492/MVP)
[[Project page]](https://github.com/gaoxin/MVP)

- **MVP** introduces a novel approach to incomplete multi-view representation learning by leveraging latent space correspondences in Variational Auto-Encoders, enabling the inference of missing views and enhancing the consistency of multi-view data even with irregularly missing information.
</div>
</div>""",

    "MacTok": """<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2026</div><img src='images/2026_02_MacTok/mactok.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MacTok: Robust Continuous Tokenization for Image Generation](https://arxiv.org/abs/TBD)

**Hengyu Zeng#**, **Xin Gao#**, Guanghao Li, Yuxiang Yan, Jiaoyang Ruan, Junpeng Ma, Haoyu Albert Wang, Jian Pu

<div style="margin-top: 8px;"><span class="keyword-badge">Continuous Tokenization</span><span class="keyword-badge">Representation</span><span class="keyword-badge">Image Generation</span></div>

- **MacTok** identifies and mitigates the severe "posterior collapse" failure in continuous image tokenizers. We formulate tokenization as a rigorous information preservation task by introducing DINO-guided semantic masking and multi-level representation alignment, forcing the model to infer robust semantics from incomplete visual evidence. This prevents structural degradation and yields state-of-the-art generation fidelity (gFID 1.52 at 512x512) with up to 64x fewer tokens.
</div>
</div>""",

    "IVQ": """<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2026</div><img src='images/2026_01_IVQ/IVQ.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Escaping Low-Rank Traps: Interpretable Visual Concept Learning via Implicit Vector Quantization](https://openreview.net/pdf?id=9M2VrpAtR1)

Shujian Gao, Yuan Wang, Chenglong Ma, **Xin Gao**, Jiangtao Yan, Junzhi Ning, Cheng Tang, Changkai Ji, Huihui Xu, Wei Li, Ziyan Huang et al.

<div style="margin-top: 8px;"><span class="keyword-badge">Concept Bottleneck</span><span class="keyword-badge">Interpretability</span><span class="keyword-badge">Vector Quantization</span></div>

- **IVQ** addresses representational collapse in Concept Bottleneck Models (CBMs), where vision-concept alignment degrades under low-rank feature traps. Rather than imposing a hard, lossy bottleneck, IVQ acts as a structural regularizer that anchors patch features to learned semantic prototypes without quantizing the forward pass, preserving high-rank and structured representations for robust, interpretable concept learning.
</div>
</div>""",

    "OrderMind": """<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2025</div><img src='images/2025_09_order/order.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Learning Spatial-Aware Manipulation Ordering](https://arxiv.org/pdf/2510.25138)

Yuxiang Yan, Zhiyuan Zhou, **Xin Gao**, Guanghao Li, Shenglin Li, Jiaqi Chen, Qunyan Pu, Jian Pu

<div style="margin-top: 8px;"><span class="keyword-badge">Spatial Reasoning</span><span class="keyword-badge">VLM</span><span class="keyword-badge">Robotic Manipulation</span></div>

- This paper introduces **OrderMind**, a spatial-aware manipulation ordering framework that learns object priorities from local geometry via a kNN spatial graph and a lightweight temporal module, supervised by VLM-distilled spatial priors. It also presents the **Manipulation Ordering Benchmark** (163k+ samples) for cluttered scenes.
</div>
</div>""",

    "ARTDECO": """<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2026</div><img src='images/2026_01_Artdeco/Artdeco.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[ARTDECO: Toward High-Fidelity On-the-Fly Reconstruction with Hierarchical Gaussian Structure and Feed-Forward Guidance](https://arxiv.org/pdf/2510.08551)

 Guanghao Li, Kerui Ren, Linning Xu, Zhewen Zheng, Changjian Jiang, **Xin Gao**, Bo Dai, Jian Pu, Mulin Yu, Jiangmiao Pang

<div style="margin-top: 8px;"><span class="keyword-badge">3D Gaussian Splatting</span><span class="keyword-badge">Structure</span><span class="keyword-badge">SLAM</span></div>

[![GitHub Stars](https://img.shields.io/github/stars/InternRobotics/ARTDECO?style=social)](https://github.com/InternRobotics/ARTDECO)
[![GitHub Forks](https://img.shields.io/github/forks/InternRobotics/ARTDECO?style=social)](https://github.com/InternRobotics/ARTDECO)
[[Project page]](https://city-super.github.io/artdeco/)

- **ARTDECO** unifies feed-forward 3D foundation priors with SLAM-style global optimization, and introduces a hierarchical 3D Gaussian scene representation with LoD-aware rendering to achieve efficient, robust, and high-fidelity on-the-fly monocular 3D reconstruction.

</div>
</div>""",

    "GOOD": """<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2025</div><img src='images/2025_09_GOOD/GOOD.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[GOOD: Training-Free Guided Diffusion Sampling for Out-of-Distribution Detection](https://arxiv.org/pdf/2510.17131)

**Xin Gao**, Jiyao Liu, Guanghao Li, Yueming Lyu, Jianxiong Gao, Weichen Yu, Ningsheng Xu, Liang Wang, Caifeng Shan, Ziwei Liu, Chenyang Si

<div style="margin-top: 8px;"><span class="keyword-badge">Diffusion Models</span><span class="keyword-badge">OOD Detection</span></div>

- **GOOD** is a training-free diffusion guidance framework that shapes a robust OOD/ID decision boundary. It steers sampling with two gradients—image-level toward low-density regions and feature-level toward sparse zones—to generate diverse, controllable OOD examples.
</div>
</div>""",

    "Dark-ISP": """<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICCV 2025</div><img src='images/2025_06_DarkISP/DarkISP.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Dark-ISP: Enhancing RAW Image Processing for Low-Light Object Detection](https://openreview.net/forum?id=7Z3G2ScIwN)

**Jiasheng Guo#**, **Xin Gao#**, Yuxiang Yan, Guanghao Li, Jian Pu

<div style="margin-top: 8px;"><span class="keyword-badge">RAW Processing</span><span class="keyword-badge">Low-Light</span><span class="keyword-badge">Object Detection</span></div>

- **Dark-ISP** is a lightweight, self-adaptive ISP plugin that enhances low-light object detection by processing Bayer RAW images. It breaks down traditional ISP pipelines into optimized linear and nonlinear sub-modules, using physics-informed priors for automatic RAW-to-RGB conversion.
</div>
</div>""",

    "Loong": """<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2025 Workshop</div><img src='images/2025_09_Loong/Loong.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Loong: Synthesize Long Chain-of-Thoughts at Scale through Verifiers](https://arxiv.org/abs/2509.03059)

Xingyue Huang, Rishabh, Gregor Franke, Ziyi Yang, Jiamu Bai, Weijie Bai, Jinhe Bi, Zifeng Ding, Yiqun Duan, Chengyu Fan, Wendong Fan, **Xin Gao** et al.

<div style="margin-top: 8px;"><span class="keyword-badge">Large Language Models</span><span class="keyword-badge">Structured Reasoning</span><span class="keyword-badge">RL</span></div>

[![GitHub Stars](https://img.shields.io/github/stars/camel-ai/loong?style=social)](https://github.com/camel-ai/loong)
[![GitHub Forks](https://img.shields.io/github/forks/camel-ai/loong?style=social)](https://github.com/camel-ai/loong)
[[Project page]](https://github.com/camel-ai/loong)

- **Loong** is an open-source framework for scalable, verifiable reasoning data. It pairs **LoongBench** (8,729 human-vetted, code-checkable examples across 12 domains) with **LoongEnv**, a modular generator forming an agent–environment loop for RL with verifiable rewards and broad-domain CoT training.
</div>
</div>"""
}

# Construct the new publications section
new_pub_section = f"""## Multimodal Structured Reasoning

{papers['OrderMind']}

{papers['Loong']}

{papers['MacTok']}

{papers['IVQ']}

{papers['ARTDECO']}


## Other Explorations

{papers['MVP']}

{papers['GOOD']}

{papers['Dark-ISP']}

"""

# Find the start and end of the publications section
start_marker = "## Multimodal Structured Reasoning\n"
end_marker = "\n<!-- ========================================================================================================================== -->\n\n\n\n<!-- # Why PhD?"

# In case the exact end_marker isn't perfect, let's just find "<!-- # Why PhD?"
start_idx = text.find(start_marker)
end_idx = text.find("\n<!-- # Why PhD?")
if end_idx == -1: end_idx = text.find("\n# 🎖 Honors and Awards")

if start_idx != -1 and end_idx != -1:
    new_text = text[:start_idx] + new_pub_section + text[end_idx:]
    with open('_pages/about.md', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Replaced successfully!")
else:
    print(f"Couldn't find markers: start={start_idx}, end={end_idx}")

