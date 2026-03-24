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

<p style="font-size: 1.1em;">
I am a Master's student in Applied Math at Fudan University and an incoming CS Ph.D. student at Yale University, advised by Prof. [Rex Ying](https://scholar.google.cat/citations?user=6fqNXooAAAAJ&hl=ca). **My research focuses on the reliability and verification of multimodal AI**, aiming to build systems that integrate explicit structures with dynamic reasoning capabilities to ensure safe, verifiable, and logically sound outputs. Currently, I am exploring verifiable multimodal code generation and principled human-in-the-loop (HITL) mechanisms for error-aware autonomous agents. Feel free to reach out if you'd like to learn more about my work, chat, or explore potential collaborations. You can find my publications on my [google scholar](https://scholar.google.com/citations?user=1UKUQUEAAAAJ&hl=zh-CN).
</p>

<p style="font-size: 0.85em; font-style: italic; color: #888;">(Note: The early Medical AI publications on my profile stem from first-year rotations exploring trustworthiness and interpretability, where I gained valuable exposure to probabilistic modeling and uncertainty estimation. While I maintain close ties with my brilliant former colleagues, my research is now entirely focused on domain-agnostic multimodal systems.)</p>


# 🔥 News
<div class="news-window" markdown="1">
- *2026.03*: Two papers ([MacTok](https://arxiv.org/abs/TBD) and [GIFT](https://arxiv.org/abs/TBD)) accepted to **CVPR 2026**.
- *2026.02*: Joined Microsoft Research Asia (MSRA) as a Research Intern.
- *2026.02*: Two papers ([ARTDECO](https://arxiv.org/pdf/2510.08551) and [IVQ](https://openreview.net/pdf?id=9M2VrpAtR1)) accepted to **ICLR 2026**.
- *2025.09*: Two papers ([GOOD](https://arxiv.org/pdf/2510.17131) and [OrderMind](https://arxiv.org/pdf/2510.25138)) accepted to **NeurIPS 2025**.
- *2025.09*: [Loong](https://arxiv.org/abs/2509.03059) accepted to **NeurIPS 2025 Workshop**.
- *2025.06*: [Dark-ISP](https://openreview.net/forum?id=7Z3G2ScIwN) accepted to **ICCV 2025**.
- *2025.05*: Joined Shanghai AILab as a Research Intern, working with [Jie Fu](https://bigaidream.github.io/).
- *2025.04*: Welcomed two cats into my life: Fellow and Putao 🐱🍇
- *2025.01*: [MVP](https://openreview.net/forum?id=s4MwstmB8o) accepted to **ICLR 2025**.
- *2024.12*: Joined as a Research Intern, working with Prof. [Chenyang Si](https://chenyangsi.top/) and Prof. [Ziwei Liu](https://liuziwei7.github.io/).
</div>
<!-- Honored to collaborate with them on these promising projects. -->

# 📝 Selected Publications

My research primarily focus on two directions: **Robust Representation in Complex Environments** and **Safety and Verification in AI Systems**.

## Robust Representation in Complex Environments

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

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CVPR 2026</div><img src='images/2026_02_MacTok/mactok.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MacTok: Robust Continuous Tokenization for Image Generation](https://arxiv.org/abs/TBD)

**Hengyu Zeng#**, **Xin Gao#**, Guanghao Li, Yuxiang Yan, Jiaoyang Ruan, Junpeng Ma, Haoyu Albert Wang, Jian Pu

- **MacTok** identifies and mitigates the severe "posterior collapse" failure in continuous image tokenizers. We formulate tokenization as a rigorous information preservation task by introducing DINO-guided semantic masking and multi-level representation alignment, forcing the model to infer robust semantics from incomplete visual evidence. This prevents structural degradation and yields state-of-the-art generation fidelity (gFID 1.52 at 512x512) with up to 64x fewer tokens.
</div>
</div>

<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2026</div><img src='images/2026_01_IVQ/IVQ.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Escaping Low-Rank Traps: Interpretable Visual Concept Learning via Implicit Vector Quantization](https://openreview.net/pdf?id=9M2VrpAtR1)

Shujian Gao, Yuan Wang, Chenglong Ma, **Xin Gao**, Jiangtao Yan, Junzhi Ning, Cheng Tang, Changkai Ji, Huihui Xu, Wei Li, Ziyan Huang et al.

- **IVQ** addresses representational collapse in Concept Bottleneck Models (CBMs), where vision-concept alignment degrades under low-rank feature traps. Rather than imposing a hard, lossy bottleneck, IVQ acts as a structural regularizer that anchors patch features to learned semantic prototypes without quantizing the forward pass, preserving high-rank and structured representations for robust, interpretable concept learning.
</div>
</div>

<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2025</div><img src='images/2025_09_order/order.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Learning Spatial-Aware Manipulation Ordering](https://arxiv.org/pdf/2510.25138)

Yuxiang Yan, Zhiyuan Zhou, **Xin Gao**, Guanghao Li, Shenglin Li, Jiaqi Chen, Qunyan Pu, Jian Pu

- This paper introduces **OrderMind**, a spatial-aware manipulation ordering framework that learns object priorities from local geometry via a kNN spatial graph and a lightweight temporal module, supervised by VLM-distilled spatial priors. It also presents the **Manipulation Ordering Benchmark** (163k+ samples) for cluttered scenes.
</div>
</div>

<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2026</div><img src='images/2026_01_Artdeco/Artdeco.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[ARTDECO: Toward High-Fidelity On-the-Fly Reconstruction with Hierarchical Gaussian Structure and Feed-Forward Guidance](https://arxiv.org/pdf/2510.08551)

 Guanghao Li, Kerui Ren, Linning Xu, Zhewen Zheng, Changjian Jiang, **Xin Gao**, Bo Dai, Jian Pu, Mulin Yu, Jiangmiao Pang

[![GitHub Stars](https://img.shields.io/github/stars/InternRobotics/ARTDECO?style=social)](https://github.com/InternRobotics/ARTDECO)
[![GitHub Forks](https://img.shields.io/github/forks/InternRobotics/ARTDECO?style=social)](https://github.com/InternRobotics/ARTDECO)
[[Project page]](https://city-super.github.io/artdeco/)

- **ARTDECO** unifies feed-forward 3D foundation priors with SLAM-style global optimization, and introduces a hierarchical 3D Gaussian scene representation with LoD-aware rendering to achieve efficient, robust, and high-fidelity on-the-fly monocular 3D reconstruction.

</div>
</div>


## Safety and Verification in AI Systems

<!-- ========================================================================================================================== -->

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2025</div><img src='images/2025_09_GOOD/GOOD.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[GOOD: Training-Free Guided Diffusion Sampling for Out-of-Distribution Detection](https://arxiv.org/pdf/2510.17131)

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

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2025 Workshop</div><img src='images/2025_09_Loong/Loong.png' alt="sym" width="100%"></div></div>
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



<!-- # Why PhD?

**And I've been thinking a lot recently - why PhD?**

I was originally admitted to Fudan University as a direct PhD student after my undergraduate studies. At the time, most of the available research directions in my department focused on interdisciplinary topics between neuroscience and AI. They were interesting, but they did not fully match my core interests. I have always been more fascinated by the algorithmic and mathematical foundations of intelligence.

Coming from a pure mathematics background, I also realized that I had not yet received systematic training in scientific research, especially in AI and machine learning. Before committing to a long and challenging PhD journey, I wanted to go through a complete and rigorous master’s program. I needed to learn how to ask meaningful questions, design experiments, and build research intuition.

Fortunately, during this process, I discovered the genuine joy of research. I found excitement in turning abstract ideas into working systems, bridging theoretical insights with practical models, and spending long hours on an equation until it finally made sense. Research became more than a requirement. It became a way of thinking.

That is why I now seek a PhD, not as an academic credential, but as a natural continuation of my intellectual curiosity. I want to push the boundary between representation structure and generative intelligence. I want to explore how reasoning and understanding can emerge from learning systems. I also want to work with mentors and peers who share this fascination. To me, a PhD represents the freedom and responsibility to create something that did not exist before. I am ready for that challenge. -->


# 🎖 Honors and Awards
- 2023.09 Fudan University Zhicheng Freshman Second Prize Scholarship (Top 5%)
- 2023.06 Outstanding Graduate of Shanghai
- 2022.11 Second Prize in the Chinese Mathematics Competitions (Category A)
- 2021.12 National Scholarship, China
- 2021.09 National Second Prize in the China Undergraduate Mathematical Contest in Modeling
- 2020.12 Shanghai Scholarship

# 👨‍💼 Academic Service
- Conference Reviewer: Neurips 2025, ICCV 2025, ICLR 2026, ICML 2026

# 📖 Educations
- *2023.09 - 2026.06 (now)*, Master of Applied Mathematics, Fudan University, Shanghai, China.
- *2019.09 - 2023.06*, Bachelor of Mathematics, Donghua Univeristy, Shanghai, China.

# 💻 Internships
- *2026.02 - present*, [Microsoft Research Asia](https://www.microsoft.com/en-us/research/), Beijing, China.
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







<div class="cat-park">
  <div class="cat-avatar" data-pose="sitting" onclick="interact(this)">
    <div class="cat-tail"><div class="tail-fluff"></div></div>
    <div class="cat-body"><div class="chest-ruff"></div></div>
    <div class="cat-head">
      <div class="ear-container">
        <div class="cat-ear left"><div class="ear-inner"></div></div>
        <div class="cat-ear right"><div class="ear-inner"></div></div>
      </div>
      <div class="cheek-fluff left"></div><div class="cheek-fluff right"></div>
      <div class="cat-face">
        <div class="cat-eye left"><div class="pupil"></div><div class="shine"></div></div>
        <div class="cat-eye right"><div class="pupil"></div><div class="shine"></div></div>
        <div class="cat-muzzle">
          <div class="nose"></div>
          <div class="mouth">
             <div class="lip left"></div><div class="lip right"></div>
             <div class="tongue"></div><div class="fangs"></div>
          </div>
          <div class="whisker-pad left">
             <div class="whisker w1"></div><div class="whisker w2"></div><div class="whisker w3"></div>
          </div>
          <div class="whisker-pad right">
             <div class="whisker w1"></div><div class="whisker w2"></div><div class="whisker w3"></div>
          </div>
        </div>
      </div>
    </div>
    <div class="cat-paws"><div class="paw left"></div><div class="paw right"></div></div>
  </div>

<div class="cat-avatar" data-pose="lying" onclick="interact(this)">
    <div class="cat-tail"><div class="tail-fluff"></div></div>
    <div class="cat-body"></div>
    
    <div class="cat-head">
      <div class="ear-container">
        <div class="cat-ear left"><div class="ear-inner"></div></div>
        <div class="cat-ear right"><div class="ear-inner"></div></div>
      </div>
      <div class="cheek-fluff left"></div><div class="cheek-fluff right"></div>
      <div class="cat-face">
        <div class="cat-eye left"><div class="pupil"></div><div class="shine"></div></div>
        <div class="cat-eye right"><div class="pupil"></div><div class="shine"></div></div>
        <div class="cat-muzzle">
          <div class="nose"></div>
          <div class="mouth">
             <div class="lip left"></div><div class="lip right"></div>
             <div class="tongue"></div><div class="fangs"></div>
          </div>
          <div class="whisker-pad left">
             <div class="whisker w1"></div><div class="whisker w2"></div><div class="whisker w3"></div>
          </div>
          <div class="whisker-pad right">
             <div class="whisker w1"></div><div class="whisker w2"></div><div class="whisker w3"></div>
          </div>
        </div>
      </div>
      
      <div class="cat-paws lying-paws">
          <div class="paw left"></div>
          <div class="paw right"></div>
      </div>
      
  </div>
  </div>

<script>
function interact(el) {
    if(el.classList.contains('grooming')) return;
    el.classList.add('grooming');
    setTimeout(() => el.classList.remove('grooming'), 2500);
}

(function() {
  const cats = document.querySelectorAll('.cat-avatar');

  // Eye Tracking
  document.addEventListener('mousemove', (e) => {
    cats.forEach(cat => {
      if (cat.classList.contains('sleeping') || cat.classList.contains('grooming')) return;
      
      const pupils = cat.querySelectorAll('.pupil');
      const rect = cat.getBoundingClientRect();
      const cx = rect.left + rect.width/2;
      const cy = rect.top + rect.height/2;
      const dx = (e.clientX - cx) / window.innerWidth;
      const dy = (e.clientY - cy) / window.innerHeight;
      
      const x = Math.max(-5, Math.min(5, dx * 25));
      const y = Math.max(-3, Math.min(5, dy * 20));
      
      pupils.forEach(p => p.style.transform = `translate(-50%,-50%) translate(${x}px, ${y}px)`);
    });
  });

  // Blinking Loop
  const blink = (cat) => {
      if(!cat.classList.contains('sleeping')) {
          cat.classList.add('blinking');
          setTimeout(() => cat.classList.remove('blinking'), 200);
      }
      setTimeout(() => blink(cat), 3000 + Math.random() * 4000);
  };
  cats.forEach(cat => blink(cat));

  // Random Behavior AI
  cats.forEach((cat, i) => {
      const actions = ['sleeping', 'stretching', 'idle'];
      const act = () => {
          cat.classList.remove(...actions);
          const r = Math.random();
          let next = 'idle';
          let time = 4000;
          
          if(r < 0.25) { next = 'sleeping'; time = 8000; }
          else if(r < 0.4) { next = 'stretching'; time = 3000; }
          
          if(next !== 'idle') cat.classList.add(next);
          setTimeout(act, time + Math.random() * 5000);
      };
      setTimeout(act, 1000 + i * 3000);
  });
})();
</script>
