import re

def get_badge_html(keywords):
    tags = ''.join([f'<span style="background-color: #f1f8ff; color: #0366d6; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; border: 1px solid #c8e1ff; margin-right: 6px; display: inline-block;">{k}</span>' for k in keywords])
    return f'\n<div style="margin-top: 8px;">{tags}</div>\n'

papers = {
    "MVP": f"""<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2025</div><img src='images/2025_01_MVP/MVP_Pipeline.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MVP: Deep Incomplete Multi-view Learning via Cyclic Permutation of VAEs](https://openreview.net/pdf?id=s4MwstmB8o)

 **Xin Gao**, Jian Pu
{get_badge_html(['Multimodal Representation', 'Structural Consistency', 'Cross-modal Reasoning'])}
[![GitHub Stars](https://img.shields.io/github/stars/gaoxin492/MVP?style=social)](https://github.com/gaoxin492/MVP)
[![GitHub Forks](https://img.shields.io/github/forks/gaoxin492/MVP?style=social)](https://github.com/gaoxin492/MVP)
[[Project page]](https://github.com/gaoxin/MVP)

- **MVP** introduces a structured framework for multimodal representation learning by leveraging latent space correspondences. By modeling the structural consistency across incomplete views, the system can dynamically infer missing modalities, providing a robust representational foundation for cross-modal reasoning.
</div>
</div>""",

    "MacTok": f"""<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2026</div><img src='images/2026_02_MacTok/mactok.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MacTok: Robust Continuous Tokenization for Image Generation](https://arxiv.org/abs/TBD)

**Hengyu Zeng#**, **Xin Gao#**, Guanghao Li, Yuxiang Yan, Jiaoyang Ruan, Junpeng Ma, Haoyu Albert Wang, Jian Pu
{get_badge_html(['Continuous Representation', 'Semantic Masking', 'Visual Reasoning'])}
- **MacTok** formulates visual tokenization as a continuous and structured information preservation task. By introducing semantic masking and multi-level structural alignment, it forces the model to perform inferential reasoning over incomplete visual evidence. This establishes a highly compressed yet structurally intact representation essential for generative reasoning.
</div>
</div>""",

    "BMC": f"""<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2026</div><img src='images/2026_05_BMC/BMC.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Reasoning on the Manifold: Bidirectional Consistency for Self-Verification in Diffusion Language Models](https://arxiv.org/abs/TBD)

Jiaoyang Ruan#, **Xin Gao#**, Yinda Chen, Hengyu Zeng, Liang Du, Guanghao Li, Jie Fu, Jian Pu
{get_badge_html(['Diffusion Language Models', 'Geometric Reasoning', 'Self-Verification'])}
- **BMC** introduces a geometric perspective to structured reasoning in Diffusion Language Models. By framing reasoning trajectories as stable paths on a high-density manifold, it provides an unsupervised mechanism for logical self-verification. BMC serves as a dense structural reward, empowering models to dynamically verify their reasoning steps and self-evolve efficiently.
</div>
</div>""",

    "GOOD": f"""<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2025</div><img src='images/2025_09_GOOD/GOOD.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[GOOD: Training-Free Guided Diffusion Sampling for Out-of-Distribution Detection](https://arxiv.org/pdf/2510.17131)

**Xin Gao**, Jiyao Liu, Guanghao Li, Yueming Lyu, Jianxiong Gao, Weichen Yu, Ningsheng Xu, Liang Wang, Caifeng Shan, Ziwei Liu, Chenyang Si
{get_badge_html(['Reliable Reasoning', 'Diffusion Models', 'Decision Boundary'])}
- **GOOD** is a framework designed to enhance the reliability of generative reasoning boundaries. By dynamically guiding the diffusion sampling process, it systematically probes the structured boundaries of the learned distribution, providing crucial mechanisms for reliable decision-making and handling out-of-distribution environments safely.
</div>
</div>""",

    "OrderMind": f"""<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2025</div><img src='images/2025_09_order/order.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Learning Spatial-Aware Manipulation Ordering](https://arxiv.org/pdf/2510.25138)

Yuxiang Yan, Zhiyuan Zhou, **Xin Gao**, Guanghao Li, Shenglin Li, Jiaqi Chen, Qunyan Pu, Jian Pu
{get_badge_html(['Spatial Reasoning', 'Vision-Language Models', 'Embodied Planning'])}
- **OrderMind** is a structured spatial reasoning framework that integrates explicit geometric priors with Vision-Language Models (VLMs) for embodied decision-making. By extracting structured relational logic via spatial graphs and VLM-distilled knowledge, it endows agents with dynamic, long-horizon reasoning capabilities in complex physical environments.
</div>
</div>""",

    "IVQ": f"""<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2026</div><img src='images/2026_01_IVQ/IVQ.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Escaping Low-Rank Traps: Interpretable Visual Concept Learning via Implicit Vector Quantization](https://openreview.net/pdf?id=9M2VrpAtR1)

Shujian Gao, Yuan Wang, Chenglong Ma, **Xin Gao**, Jiangtao Yan, Junzhi Ning, Cheng Tang, Changkai Ji, Huihui Xu, Wei Li, Ziyan Huang et al.
{get_badge_html(['Interpretable Reasoning', 'Concept Representation', 'Structured Regularization'])}
- **IVQ** bridges the gap between low-level dense features and high-level logical reasoning by establishing structured concept representations. Serving as an implicit structural regularizer, it anchors visual features to explicit semantic prototypes continuously, preserving a high-dimensional, explainable reasoning space critical for verifiable multimodal systems.
</div>
</div>""",

    "Dark-ISP": f"""<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICCV 2025</div><img src='images/2025_06_DarkISP/DarkISP.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Dark-ISP: Enhancing RAW Image Processing for Low-Light Object Detection](https://openreview.net/forum?id=7Z3G2ScIwN)

**Jiasheng Guo#**, **Xin Gao#**, Yuxiang Yan, Guanghao Li, Jian Pu
{get_badge_html(['Physical Priors', 'Perceptual Reasoning', 'Robust Perception'])}
- **Dark-ISP** integrates explicit physical and structural priors into the early stages of visual perception to ensure robust multimodal reasoning under fundamentally degraded conditions. By reformulating sensory pipelines with physics-informed constraints, it guarantees reliable feature extraction, forming a resilient foundation for downstream semantic reasoning.
</div>
</div>""",

    "ARTDECO": f"""<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2026</div><img src='images/2026_01_Artdeco/Artdeco.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[ARTDECO: Toward High-Fidelity On-the-Fly Reconstruction with Hierarchical Gaussian Structure and Feed-Forward Guidance](https://arxiv.org/pdf/2510.08551)

 Guanghao Li, Kerui Ren, Linning Xu, Zhewen Zheng, Changjian Jiang, **Xin Gao**, Bo Dai, Jian Pu, Mulin Yu, Jiangmiao Pang
{get_badge_html(['3D Structured Reasoning', 'Spatial Representation', 'Scene Understanding'])}
[![GitHub Stars](https://img.shields.io/github/stars/InternRobotics/ARTDECO?style=social)](https://github.com/InternRobotics/ARTDECO)
[![GitHub Forks](https://img.shields.io/github/forks/InternRobotics/ARTDECO?style=social)](https://github.com/InternRobotics/ARTDECO)
[[Project page]](https://city-super.github.io/artdeco/)

- **ARTDECO** formulates dynamic scene understanding as a continuous structured reasoning problem. By integrating feed-forward foundational priors with hierarchical spatial optimizations, it builds highly structured, globally consistent 3D representations on the fly. This equips multimodal agents with the exact geometrical and spatial context needed for complex physical reasoning.
</div>
</div>""",

    "Loong": f"""<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2025 Workshop</div><img src='images/2025_09_Loong/Loong.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Loong: Synthesize Long Chain-of-Thoughts at Scale through Verifiers](https://arxiv.org/abs/2509.03059)

Xingyue Huang, Rishabh, Gregor Franke, Ziyi Yang, Jiamu Bai, Weijie Bai, Jinhe Bi, Zifeng Ding, Yiqun Duan, Chengyu Fan, Wendong Fan, **Xin Gao** et al.
{get_badge_html(['Chain-of-Thought', 'Structured Reasoning', 'Large Language Models'])}
[![GitHub Stars](https://img.shields.io/github/stars/camel-ai/loong?style=social)](https://github.com/camel-ai/loong)
[![GitHub Forks](https://img.shields.io/github/forks/camel-ai/loong?style=social)](https://github.com/camel-ai/loong)
[[Project page]](https://github.com/camel-ai/loong)

- **Loong** is a comprehensive framework for scalable, verifiable Chain-of-Thought reasoning. By structuring the reasoning process into an interactive agent-environment loop with verifiable rewards, it scales structured reasoning data generation. This provides a crucial automated mechanism for training models in rigorous, logically sound deduction.
</div>
</div>"""
}

desired_order = ["MVP", "MacTok", "BMC", "GOOD", "OrderMind", "IVQ", "Dark-ISP", "ARTDECO", "Loong"]
new_papers_content = "\n\n".join([papers[k] for k in desired_order])

# Make sure we replace the whole publication block properly.
with open('_pages/about.md', 'r', encoding='utf-8') as f:
    text = f.read()

pub_start = text.find("# 📝 Selected Publications")
end_idx = text.find("\n# 🎖 Honors and Awards")
if end_idx == -1: end_idx = text.find("<!-- # Why PhD?")

if pub_start != -1 and end_idx != -1:
    new_header = """# 📝 Selected Publications

All of my works are driven by a singular goal: **Multimodal Structured Reasoning**. Whether it is through representing continuous visual semantics, verifying reasoning trajectories, or parsing complex 3D environments, my research seeks to endow AI systems with the ability to reason structurally.

"""
    
    final_text = text[:pub_start] + new_header + new_papers_content + "\n\n" + text[end_idx:]
    with open('_pages/about.md', 'w', encoding='utf-8') as f:
        f.write(final_text)
    print("Rewritten successfully.")
else:
    print("FAIL. Could not find markers.")

