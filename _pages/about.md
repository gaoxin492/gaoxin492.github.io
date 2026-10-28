---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

<div style="font-size: 1.1em;" markdown="1">
I'm a first-year CS PhD student at Yale University, advised by Prof. [Rex Ying](https://scholar.google.cat/citations?user=6fqNXooAAAAJ&hl=ca).

My current research focuses on **Beyond Natural Language Reasoning**. I am interested in how models acquire generalizable reasoning abilities through computational processes that are not limited to natural language. My goal is to develop reusable, compositional, and transferable reasoning mechanisms that enable more flexible and generalizable intelligence.
</div>

{% include reasoning-structures.html %}

<div style="font-size: 1.1em;" markdown="1">
My previous work spans multimodal representation learning, generative modeling, and reasoning. I welcome discussions and potential collaborations. You can find my publications on [Google Scholar](https://scholar.google.com/citations?user=1UKUQUEAAAAJ&hl=zh-CN).
</div>

<!-- <p style="font-size: 0.85em; font-style: italic; color: #888;">(Note: You might notice some early Medical AI publications on my Google Scholar. These stem from my first-year lab rotation exploring probabilistic modeling and uncertainty estimation. While I maintain close ties with my brilliant former colleagues, my research is now entirely focused on domain-agnostic multimodal systems.)</p> -->


# 🔥 News
<div class="news-window" markdown="1">
- *2026.10*: Released [AesCode](https://microsoft.github.io/AesCode/), our work on aesthetic code generation with decoupled cross-modal rewards.
- *2026.05*: [BMC](https://arxiv.org/abs/TBD) accepted to **ICML 2026**.
- *2026.03*: Two papers ([MacTok](https://github.com/alienflm/MacTok) and [GIFT](https://arxiv.org/abs/TBD)) accepted to **CVPR 2026**, with **MacTok selected as a Highlight**.
- *2026.02*: Joined Microsoft Research Asia (MSRA) as a Research Intern.
- *2026.02*: Two papers ([ARTDECO](https://arxiv.org/pdf/2510.08551) and [IVQ](https://openreview.net/pdf?id=9M2VrpAtR1)) accepted to **ICLR 2026**.
- *2025.09*: Two papers ([GOOD](https://arxiv.org/pdf/2510.17131) and [OrderMind](https://arxiv.org/pdf/2510.25138)) accepted to **NeurIPS 2025**.
- *2025.09*: [Loong](https://arxiv.org/abs/2509.03059) accepted to **NeurIPS 2025 Workshop**.
- *2025.05*: Joined Shanghai AILab as a Research Intern, working with [Jie Fu](https://bigaidream.github.io/).
- *2025.04*: Welcomed two cats into my life: Fellow and Putao 🐱🍇
- *2025.01*: [MVP](https://openreview.net/forum?id=s4MwstmB8o) accepted to **ICLR 2025**.
- *2024.12*: Joined as a Research Intern, working with Prof. [Chenyang Si](https://chenyangsi.top/) and Prof. [Ziwei Liu](https://liuziwei7.github.io/).
</div>
<!-- Honored to collaborate with them on these promising projects. -->

# 📝 Selected Publications

My work spans multimodal representation learning, visual generation, and reasoning, informing my current interests in how models learn, reason, and improve.

<sup>#</sup> Equal contribution.

<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint 2026</div><img src='images/2026_10_AesCode/overview.png' alt="AesCode training pipeline with design graph supervision and decoupled cross-modal rewards" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[AesCode: Aesthetic Code Generation with Decoupled Cross-Modal Rewards](https://arxiv.org/abs/2610.18860)

**Xin Gao**, Yifan Yang, Xin Li, Pan Wang, Yan Li, Muzhao Tian, Mingxi Cheng, Bei Liu, Kai Qiu, Qi Dai, Dong Chen, Yue Dong, Leandros Tassiulas, Rex Ying, Ji Li, Chong Luo

<div style="margin-top: 8px;"><span style="background-color: #f1f8ff; color: #0366d6; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; border: 1px solid #c8e1ff; margin-right: 6px; display: inline-block;">Code Generation</span><span style="background-color: #f1f8ff; color: #0366d6; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; border: 1px solid #c8e1ff; margin-right: 6px; display: inline-block;">Reinforcement Learning with Verifiable Rewards (RLVR)</span><span style="background-color: #f1f8ff; color: #0366d6; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; border: 1px solid #c8e1ff; margin-right: 6px; display: inline-block;">Multimodal Learning</span></div>

[![GitHub Stars](https://img.shields.io/github/stars/microsoft/AesCode?style=social)](https://github.com/microsoft/AesCode)
[![GitHub Forks](https://img.shields.io/github/forks/microsoft/AesCode?style=social)](https://github.com/microsoft/AesCode)
[[Project page]](https://microsoft.github.io/AesCode/)

- **AesCode** uses design-graph supervision and decoupled cross-modal rewards to generate editable visual artifacts as code, learning aesthetic guidance from images while preserving prompt-specified content.
</div>
</div>

<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2025</div><img src='images/2025_01_MVP/MVP_Pipeline.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MVP: Deep Incomplete Multi-view Learning via Cyclic Permutation of VAEs](https://openreview.net/pdf?id=s4MwstmB8o)

 **Xin Gao**, Jian Pu

<div style="margin-top: 8px;"><span style="background-color: #f1f8ff; color: #0366d6; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; border: 1px solid #c8e1ff; margin-right: 6px; display: inline-block;">Multi-modal Learning</span><span style="background-color: #f1f8ff; color: #0366d6; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; border: 1px solid #c8e1ff; margin-right: 6px; display: inline-block;">Latent Space</span><span style="background-color: #f1f8ff; color: #0366d6; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; border: 1px solid #c8e1ff; margin-right: 6px; display: inline-block;">Cross-modal Generation</span></div>
[![GitHub Stars](https://img.shields.io/github/stars/gaoxin492/MVP?style=social)](https://github.com/gaoxin492/MVP)
[![GitHub Forks](https://img.shields.io/github/forks/gaoxin492/MVP?style=social)](https://github.com/gaoxin492/MVP)
[[Project page]](https://github.com/gaoxin/MVP)

- **MVP** introduces a robust generative approach to incomplete multi-view representation learning by leveraging latent space correspondences in Variational Auto-Encoders. This enables the inference of missing modalities and enhances multi-view consistency even with irregularly missing information.
</div>
</div>

<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2026 · Highlight</div><img src='images/2026_02_MacTok/mactok.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MacTok: Robust Continuous Tokenization for Image Generation](https://cvpr.thecvf.com/virtual/2026/poster/36668)

Hengyu Zeng<sup>#</sup>, **Xin Gao**<sup>#</sup>, Guanghao Li, Yuxiang Yan, Jiaoyang Ruan, Junpeng Ma, Haoyu Albert Wang, Jian Pu

<div style="margin-top: 8px;"><span style="background-color: #f1f8ff; color: #0366d6; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; border: 1px solid #c8e1ff; margin-right: 6px; display: inline-block;">Continuous Tokenization</span><span style="background-color: #f1f8ff; color: #0366d6; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; border: 1px solid #c8e1ff; margin-right: 6px; display: inline-block;">Posterior Collapse</span><span style="background-color: #f1f8ff; color: #0366d6; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; border: 1px solid #c8e1ff; margin-right: 6px; display: inline-block;">Image Generation</span></div>
[![GitHub Stars](https://img.shields.io/github/stars/alienflm/MacTok?style=social)](https://github.com/alienflm/MacTok)
[![GitHub Forks](https://img.shields.io/github/forks/alienflm/MacTok?style=social)](https://github.com/alienflm/MacTok)

- **MacTok** addresses the severe "posterior collapse" failure in continuous image tokenizers. By introducing DINO-guided semantic masking and multi-level representation alignment, it forces the model to infer robust semantics from incomplete visual evidence, yielding state-of-the-art generation fidelity.
</div>
</div>

<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2026</div><img src='images/2026_05_BMC/BMC.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Reasoning on the Manifold: Bidirectional Consistency for Self-Verification in Diffusion Language Models](https://arxiv.org/abs/TBD)

Jiaoyang Ruan<sup>#</sup>, **Xin Gao**<sup>#</sup>, Yinda Chen, Hengyu Zeng, Liang Du, Guanghao Li, Jie Fu, Jian Pu

<div style="margin-top: 8px;"><span style="background-color: #f1f8ff; color: #0366d6; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; border: 1px solid #c8e1ff; margin-right: 6px; display: inline-block;">Diffusion Language Models</span><span style="background-color: #f1f8ff; color: #0366d6; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; border: 1px solid #c8e1ff; margin-right: 6px; display: inline-block;">Reasoning</span><span style="background-color: #f1f8ff; color: #0366d6; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; border: 1px solid #c8e1ff; margin-right: 6px; display: inline-block;">Self-Verification</span></div>
- **BMC** introduces a geometric perspective to reasoning in Diffusion Language Models. By framing verifiable trajectories as stable paths on a high-density manifold, it provides an unsupervised mechanism for logical self-verification, empowering models to dynamically verify generation steps and self-evolve.
</div>
</div>

<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2025</div><img src='images/2025_09_GOOD/GOOD.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[GOOD: Training-Free Guided Diffusion Sampling for Out-of-Distribution Detection](https://arxiv.org/pdf/2510.17131)

**Xin Gao**, Jiyao Liu, Guanghao Li, Yueming Lyu, Jianxiong Gao, Weichen Yu, Ningsheng Xu, Liang Wang, Caifeng Shan, Ziwei Liu, Chenyang Si

<div style="margin-top: 8px;"><span style="background-color: #f1f8ff; color: #0366d6; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; border: 1px solid #c8e1ff; margin-right: 6px; display: inline-block;">Diffusion Models</span><span style="background-color: #f1f8ff; color: #0366d6; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; border: 1px solid #c8e1ff; margin-right: 6px; display: inline-block;">Diffusion Sampling</span><span style="background-color: #f1f8ff; color: #0366d6; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; border: 1px solid #c8e1ff; margin-right: 6px; display: inline-block;">Out-of-distribution</span></div>
- **GOOD** is a training-free diffusion guidance framework that shapes a robust OOD/ID classification boundary. It steers sampling with image-level and feature-level gradients to systematically generate diverse, controllable OOD examples for robust decision-making.
</div>
</div>

<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2025 Workshop</div><img src='images/2025_09_Loong/Loong.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Loong: Synthesize Long Chain-of-Thoughts at Scale through Verifiers](https://arxiv.org/abs/2509.03059)

Xingyue Huang, Rishabh, Gregor Franke, Ziyi Yang, Jiamu Bai, Weijie Bai, Jinhe Bi, Zifeng Ding, Yiqun Duan, Chengyu Fan, Wendong Fan, **Xin Gao** et al.

<div style="margin-top: 8px;"><span style="background-color: #f1f8ff; color: #0366d6; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; border: 1px solid #c8e1ff; margin-right: 6px; display: inline-block;">LLM</span><span style="background-color: #f1f8ff; color: #0366d6; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; border: 1px solid #c8e1ff; margin-right: 6px; display: inline-block;">Reasoning</span><span style="background-color: #f1f8ff; color: #0366d6; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; border: 1px solid #c8e1ff; margin-right: 6px; display: inline-block;">RLVR</span></div>
[![GitHub Stars](https://img.shields.io/github/stars/camel-ai/loong?style=social)](https://github.com/camel-ai/loong)
[![GitHub Forks](https://img.shields.io/github/forks/camel-ai/loong?style=social)](https://github.com/camel-ai/loong)
[[Project page]](https://github.com/camel-ai/loong)

- **Loong** is an open-source framework for scalable, verifiable Chain-of-Thought (CoT) reasoning data generation. It pairs a large benchmark with a modular generator forming an agent–environment loop for broad-domain reasoning training and verification.
</div>
</div>

<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICCV 2025</div><a href='images/2025_06_DarkISP/framework.png' aria-label="View the full-size Dark-ISP framework"><img src='images/2025_06_DarkISP/framework.png' alt="Dark-ISP framework: (a) task-driven RAW image processing, (b) adaptive linear component, and (c) nonlinear component" width="100%"></a></div></div>
<div class='paper-box-text' markdown="1">

[Dark-ISP: Enhancing RAW Image Processing for Low-Light Object Detection](https://openaccess.thecvf.com/content/ICCV2025/html/Guo_Dark-ISP_Enhancing_RAW_Image_Processing_for_Low-Light_Object_Detection_ICCV_2025_paper.html)

Jiasheng Guo<sup>#</sup>, **Xin Gao**<sup>#</sup>, Yuxiang Yan, Guanghao Li, Jian Pu

<div style="margin-top: 8px;"><span style="background-color: #f1f8ff; color: #0366d6; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; border: 1px solid #c8e1ff; margin-right: 6px; display: inline-block;">Image Processing</span><span style="background-color: #f1f8ff; color: #0366d6; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; border: 1px solid #c8e1ff; margin-right: 6px; display: inline-block;">Physics Priors</span><span style="background-color: #f1f8ff; color: #0366d6; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; border: 1px solid #c8e1ff; margin-right: 6px; display: inline-block;">Object Detection</span></div>

- **Dark-ISP** learns to process RAW sensor data for downstream detection rather than visual enhancement alone. It combines adaptive, physics-informed linear and nonlinear modules with self-boost regularization to improve low-light object detection in a lightweight, end-to-end pipeline.
</div>
</div>

<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2025</div><img src='images/2025_09_order/order.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Learning Spatial-Aware Manipulation Ordering](https://arxiv.org/pdf/2510.25138)

Yuxiang Yan, Zhiyuan Zhou, **Xin Gao**, Guanghao Li, Shenglin Li, Jiaqi Chen, Qunyan Pu, Jian Pu

<div style="margin-top: 8px;"><span style="background-color: #f1f8ff; color: #0366d6; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; border: 1px solid #c8e1ff; margin-right: 6px; display: inline-block;">Spatial Reasoning</span><span style="background-color: #f1f8ff; color: #0366d6; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; border: 1px solid #c8e1ff; margin-right: 6px; display: inline-block;">Vision-Language Models</span></div>
- **OrderMind** is a spatial-aware manipulation ordering framework that learns object priorities from local geometry via a kNN spatial graph and a lightweight module, supervised by VLM-distilled situational knowledge for robotic embodied tasks.
</div>
</div>

<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2026</div><img src='images/2026_01_IVQ/IVQ.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Escaping Low-Rank Traps: Interpretable Visual Concept Learning via Implicit Vector Quantization](https://openreview.net/pdf?id=9M2VrpAtR1)

Shujian Gao, Yuan Wang, Chenglong Ma, **Xin Gao**, Jiangtao Yan, Junzhi Ning, Cheng Tang, Changkai Ji, Huihui Xu, Wei Li, Ziyan Huang et al.

<div style="margin-top: 8px;"><span style="background-color: #f1f8ff; color: #0366d6; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; border: 1px solid #c8e1ff; margin-right: 6px; display: inline-block;">Visual Concept Learning</span><span style="background-color: #f1f8ff; color: #0366d6; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; border: 1px solid #c8e1ff; margin-right: 6px; display: inline-block;">Representation Learning</span></div>
- **IVQ** acts as a structural regularizer to address representational collapse in Concept Bottleneck Models (CBMs). It anchors patch features to learned semantic prototypes continuously, preserving a high-rank, explainable representation space for visual concept learning.
</div>
</div>

<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2026</div><img src='images/2026_01_Artdeco/Artdeco.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[ARTDECO: Toward High-Fidelity On-the-Fly Reconstruction with Hierarchical Gaussian Structure and Feed-Forward Guidance](https://arxiv.org/pdf/2510.08551)

 Guanghao Li, Kerui Ren, Linning Xu, Zhewen Zheng, Changjian Jiang, **Xin Gao**, Bo Dai, Jian Pu, Mulin Yu, Jiangmiao Pang

<div style="margin-top: 8px;"><span style="background-color: #f1f8ff; color: #0366d6; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; border: 1px solid #c8e1ff; margin-right: 6px; display: inline-block;">Scene Reconstruction</span><span style="background-color: #f1f8ff; color: #0366d6; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; border: 1px solid #c8e1ff; margin-right: 6px; display: inline-block;">3D Foundation Models</span></div>
[![GitHub Stars](https://img.shields.io/github/stars/InternRobotics/ARTDECO?style=social)](https://github.com/InternRobotics/ARTDECO)
[![GitHub Forks](https://img.shields.io/github/forks/InternRobotics/ARTDECO?style=social)](https://github.com/InternRobotics/ARTDECO)
[[Project page]](https://city-super.github.io/artdeco/)

- **ARTDECO** unifies feed-forward 3D foundation priors with SLAM-style global optimization. It utilizes a hierarchical 3D Gaussian scene representation to achieve efficient, robust, and high-fidelity on-the-fly monocular 3D reconstruction.
</div>
</div>

# 👨‍💼 Academic Service
- Conference Reviewer: NeurIPS 2025, 2026; ICLR 2026, 2027; ICML 2026 (Silver Reviewer); ICCV 2025; AAAI 2027; WACV 2027

# 💻 Internships
- *2026.02 - 2026.09*, [Microsoft Research Asia](https://www.microsoft.com/en-us/research/), Beijing, China.
- *2025.05 - 2025.12*, [Shanghai AIlab](https://www.shlab.org.cn/), Shanghai, China.


# 📚 Learning Materials

😁 If you want the following material without watermarks, please contact me using the email address and specify your intended use.  

## Material 1: [Frontiers in Diffusion Model Technologies (1)](1-diffusion-page)

<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <img src='images/materials/diffusion.png' alt="Material 1 Image" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
    
  This document provides an overview of key concepts related to diffusion models, particularly focusing on the theoretical foundations, development timeline, and recent advancements in the field. The content includes detailed discussions on **VAE, DDPM, DDIM, SDE, and ODE, as well as conditional guidance**. It also covers the evolution of stable diffusion, including topics like **Latent Diffusion, VQ-VAE, and DiT**. Lastly, the document highlights the latest methodology, **IC-Light**, set to be presented at [ICLR 2025](https://openreview.net/forum?id=u1cQYxRI1H).
  
  </div>
</div>


## Material 2: [Tutorial of Information Geometry and t3-VAE](2-t3VAE-page)

<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <img src='images/materials/t3VAE.png' alt="Material 2 Image" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
    
  This document introduces the t3-Variational Autoencoder ([ICLR 2024](https://openreview.net/pdf?id=RzNlECeoOB)), which uses **Student's t-distributions to model heavy-tailed data distributions** and improve latent variable representations. It also explores the framework of **Information Geometry**, focusing on how generative models can be understood through **statistical manifolds, divergences, and Riemannian metrics**, providing a deeper understanding of probability distributions and their applications in machine learning, signal processing, and neuroscience.
  
  </div>
</div>


## Material 3: [EM Algorithm and X-metric](3-xmetric-page)

<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <img src='images/materials/xmetric.png' alt="Material 3 Image" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">

  This document introduces the X-metric framework ([PAMI 2023](https://ieeexplore.ieee.org/document/9965747)), an **N-dimensional information-theoretic approach** designed for groupwise registration and deep combined computing, with applications in advanced machine learning tasks. It also covers the theoretical foundations, including **entropy, mutual information, and the MLE algorithm**, alongside the framework's modifications for deep computing and network training.

  </div>
</div>







{% include pixel-cats.html %}
