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


I am currently a second-year Master’s student in Applied Mathematics at Fudan University. My research focuses on artificial intelligence and machine learning, with particular emphasis on probability distribution modeling, generative models (especially diffusion models), as well as the multimodal representation learning. **I will apply for a PhD in Fall 2026 and seek advisors and collaborators with a mathematics background who share an interest in AI. I believe mathematics is the key to solving fundamental AI challenges.**

Feel free to reach out if you’d like to learn more about my work, chat, or explore potential collaborations.


# 🔥 News
- *2025.09*：🎉 [GOOD](https://neurips.cc/virtual/2025/poster/116282) is accepted by **Neurips 2025**. See you in San Diego!
- *2025.09*：🎉 [OrderMind](https://neurips.cc/virtual/2025/poster/116565) is accepted by **Neurips 2025**. Congrats to Yuxiang!
- *2025.09*：🎉 [Loong](https://arxiv.org/abs/2509.03059) is accepted by **Neurips 2025 workshop**. Great work from the Camel-AI team!!
- *2025.06*：🎉 [Dark-ISP](https://openreview.net/forum?id=7Z3G2ScIwN) is accepted by **ICCV 2025**. Congrats to Jiasheng! Hope to see you in Hawaii!
- *2025.05*：🎉 Start my internship in shanghai AIlab with [Jie Fu](https://bigaidream.github.io/)! Do you have Big AI Dream~
- *2025.01*: 🎉 [MVP](https://openreview.net/forum?id=s4MwstmB8o) is accepted by **ICLR 2025**. See you in Singapore!
- *2024.12*：🎉 Start my internship with prof [Chenyang Si](https://chenyangsi.top/) and [Ziwei Liu](https://liuziwei7.github.io/)~
- *2024.05*: 🎉 [evi-CEM](https://link.springer.com/chapter/10.1007/978-3-031-72117-5_29) is accepted by **MICCAI 2024**. Congrats to Yibo.
<!-- Honored to collaborate with them on these promising projects. -->

# 📝 Publications 


<!-- <div class='paper-box'><div class='paper-box-image'><div><div class="badge">Arxiv preprint</div><img src='images/2024_09_PAPL_SLAM/PAPL_SLAM.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[PAPL-SLAM: Principal Axis-Anchored Monocular Point-Line SLAM](https://arxiv.org/pdf/2410.12324)

 **Guanghao Li**, Yu Cao, Qi Chen, Yifan Yang, Jian Pu

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=6nkKQDIAAAAJ&citation_for_view=6nkKQDIAAAAJ:9yKSN-GCB0IC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>

- PAPL-SLAM is a point-line SLAM system that efficiently integrates line structural information and optimization by anchoring lines to a principal axis, reducing the number of parameters, and utilizing probabilistic data association, enabling robust, rapid, and accurate mapping and tracking in both indoor and outdoor environments.
</div>
</div> -->


<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2025</div><img src='images/2025_01_MVP/MVP_Pipeline.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MVP: Deep Incomplete Multi-view Learning via Cyclic Permutation of VAEs](https://openreview.net/pdf?id=s4MwstmB8o)

 **Xin Gao**, Jian Pu

[![GitHub Stars](https://img.shields.io/github/stars/gaoxin492/MVP?style=social)](https://github.com/gaoxin492/MVP)
[![GitHub Forks](https://img.shields.io/github/forks/gaoxin492/MVP?style=social)](https://github.com/gaoxin492/MVP)
[[Project page]](https://github.com/gaoxin/MVP)

- **MVP** introduces a novel approach to incomplete multi-view representation learning by leveraging latent space correspondences in Variational Auto-Encoders, enabling the inference of missing views and enhancing the consistency of multi-view data even with irregularly missing information.
</div>
</div>

<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Neurips 2025</div><img src='images/2025_09_GOOD/GOOD.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[GOOD: Training-Free Guided Diffusion Sampling for Out-of-Distribution Detection](https://neurips.cc/virtual/2025/poster/116282)

**Xin Gao**, Jiyao Liu, Guanghao Li, Yueming Lyu, Jianxiong Gao, Weichen Yu, Ningsheng Xu, Liang Wang, Caifeng Shan, Ziwei Liu, Chenyang Si

- **GOOD** is a training-free diffusion guidance framework that shapes a robust OOD/ID decision boundary. It steers sampling with two gradients—image-level toward low-density regions and feature-level toward sparse zones—to generate diverse, controllable OOD examples.
</div>
</div>

<!-- ========================================================================================================================== -->


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICCV 2025</div><img src='images/2025_06_DarkISP/DarkISP.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Dark-ISP: Enhancing RAW Image Processing for Low-Light Object Detection](https://openreview.net/forum?id=7Z3G2ScIwN)

**Jiasheng Guo#**, **Xin Gao#**, Yuxiang Yan, Guanghao Li, Jian Pu

- **Dark-ISP** is a lightweight, self-adaptive ISP plugin that enhances low-light object detection by processing Bayer RAW images. It breaks down traditional ISP pipelines into optimized linear and nonlinear sub-modules, using physics-informed priors for automatic RAW-to-RGB conversion. 
</div>
</div>


<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Neurips 2025</div><img src='images/2025_09_order/order.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Learning Spatial-Aware Manipulation Ordering](https://neurips.cc/virtual/2025/poster/116565)

Yuxiang Yan, Zhiyuan Zhou, **Xin Gao**, Guanghao Li, Shenglin Li, Jiaqi Chen, Qunyan Pu, Jian Pu 

- This paper introduces **OrderMind**, a spatial-aware manipulation ordering framework that learns object priorities from local geometry via a kNN spatial graph and a lightweight temporal module, supervised by VLM-distilled spatial priors. It also presents the **Manipulation Ordering Benchmark** (163k+ samples) for cluttered scenes.
</div>
</div>

<!-- ========================================================================================================================== -->


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Neurips 2025 workshop</div><img src='images/2025_09_Loong/Loong.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Loong: Synthesize Long Chain-of-Thoughts at Scale through Verifiers](https://arxiv.org/abs/2509.03059)

Xingyue Huang, Rishabh, Gregor Franke, Ziyi Yang, Jiamu Bai, Weijie Bai, Jinhe Bi, Zifeng Ding, Yiqun Duan, Chengyu Fan, Wendong Fan, **Xin Gao** et al.

[![GitHub Stars](https://img.shields.io/github/stars/camel-ai/loong?style=social)](https://github.com/camel-ai/loong)
[![GitHub Forks](https://img.shields.io/github/forks/camel-ai/loong?style=social)](https://github.com/camel-ai/loong)
[[Project page]](https://github.com/camel-ai/loong)

- **Loong** is an open-source framework for scalable, verifiable reasoning data. It pairs **LoongBench** (8,729 human-vetted, code-checkable examples across 12 domains) with **LoongEnv**, a modular generator forming an agent–environment loop for RL with verifiable rewards and broad-domain CoT training.
</div>
</div>


<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">MICCAI 2024</div><img src='images/2024_10_evi_cem/EVI_CEM.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Evidential concept embedding models: Towards reliable concept explanations for skin disease diagnosis](https://ui.adsabs.harvard.edu/abs/2024arXiv240413346L/abstract)

Yibo Gao, Zheyao Gao, **Xin Gao**, Yuanye Liu, Bomin Wang, Xiahai Zhuang

[![GitHub Stars](https://img.shields.io/github/stars/obiyoag/evi-CEM?style=social)](https://github.com/obiyoag/evi-CEM)
[![GitHub Forks](https://img.shields.io/github/forks/obiyoag/evi-CEM?style=social)](https://github.com/obiyoag/evi-CEM)
[[Project page]](https://github.com/obiyoag/evi-CEM)

- **evi-CEM** introduces an evidential learning approach to enhance the reliability of concept predictions in Concept Bottleneck Models, addressing concept misalignments in medical image analysis and improving performance in both supervised and label-efficient settings.
</div>
</div>


# 🎖 Honors and Awards
- 2023.09 Fudan University Zhicheng Freshman Second Prize Scholarship (Top 5%)
- 2023.06 Outstanding Graduate of Shanghai
- 2022.11 Second Prize in the Chinese Mathematics Competitions (Category A)
- 2021.12 National Scholarship, China
- 2021.09 National Second Prize in the China Undergraduate Mathematical Contest in Modeling
- 2020.12 Shanghai Scholarship

# 👨‍💼 Academic Service
- Conference Reviewer: Neurips 2025, ICCV 2025, ICLR 2026

# 📖 Educations
- *2023.09 - 2026.06 (now)*, Master of Applied Mathematics, Fudan University, Shanghai, China.
- *2019.09 - 2023.06*, Bachelor of Mathematics, Donghua Univeristy, Shanghai, China.

# 💻 Internships
- *2025.05 - Now*, [Shanghai Alab](https://www.shlab.org.cn/), Shanghai, China.
- *2023.03 - 2023.07*, [Winning AI Lab](https://www.winning.com.cn/solution-detail.html?id=40), Shanghai, China.


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
    
  This document introduces the t3-Variational Autoencoder ([ICLR 2024](https://openreview.net/pdf?id=RzNlECeoOB)), which uses **Student’s t-distributions to model heavy-tailed data distributions** and improve latent variable representations. It also explores the framework of **Information Geometry**, focusing on how generative models can be understood through **statistical manifolds, divergences, and Riemannian metrics**, providing a deeper understanding of probability distributions and their applications in machine learning, signal processing, and neuroscience.
  
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



