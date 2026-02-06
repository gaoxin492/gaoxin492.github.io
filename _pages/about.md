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


I am currently a third-year Master's student in Applied Mathematics at Fudan University and an **incoming PhD student in Computer Science at a US top-10 university**. My research focuses on generative machine learning, with particular emphasis on probabilistic distribution modeling, generative models, and multimodal representation learning. At present, I am exploring recursive and looped architectures, such as diffusion language models, tiny recursive models, and looped transformers, for complex reasoning tasks. Feel free to reach out if you'd like to learn more about my work, chat, or explore potential collaborations. This is my [google scholar](https://scholar.google.com/citations?user=1UKUQUEAAAAJ&hl=zh-CN).


# 🔥 News
<div class="news-window" markdown="1">
- *2026.02*: 🎉 [ARTDECO](https://arxiv.org/pdf/2510.08551) and [IVQ](https://openreview.net/pdf?id=9M2VrpAtR1) are accepted by **ICLR 2026**.
- *2025.09*: 🎉 [GOOD](https://arxiv.org/pdf/2510.17131) and [OrderMind](https://arxiv.org/pdf/2510.25138) are accepted by **Neurips 2025**. Got visa! See you in San Diego!
- *2025.09*: 🎉 [Loong](https://arxiv.org/abs/2509.03059) is accepted by **Neurips 2025 workshop**. Great work from the Camel-AI team!!
- *2025.06*: 🎉 [Dark-ISP](https://openreview.net/forum?id=7Z3G2ScIwN) is accepted by **ICCV 2025**. Congrats to Jiasheng! Hope to see you in Hawaii!
- *2025.05*: Start my internship in shanghai AIlab with [Jie Fu](https://bigaidream.github.io/)! Do you have Big AI Dream~
- *2025.04*: Welcomed two adorable cats into my life: Fellow and Putao 🐱🍇 
- *2025.01*: 🎉 [MVP](https://openreview.net/forum?id=s4MwstmB8o) is accepted by **ICLR 2025**. See you in Singapore!
- *2024.12*: Start my internship with prof [Chenyang Si](https://chenyangsi.top/) and [Ziwei Liu](https://liuziwei7.github.io/)~
</div>
<!-- Honored to collaborate with them on these promising projects. -->

# 📝 Selected Publications 


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


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Neurips 2025</div><img src='images/2025_09_order/order.png' alt="sym" width="100%"></div></div>
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
- *2025.05 - Now*, [Shanghai AIlab](https://www.shlab.org.cn/), Shanghai, China.
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
  <!-- Cat 1: Sitting pose -->
  <div class="cat-avatar realistic-cat" data-cat="1">
    <div class="cat-body">
      <div class="cat-fur-detail"></div>
      <div class="cat-chest"></div>
    </div>
    <div class="cat-head">
      <div class="cat-ear left">
        <div class="ear-inner"></div>
        <div class="ear-tuft"></div>
      </div>
      <div class="cat-ear right">
        <div class="ear-inner"></div>
        <div class="ear-tuft"></div>
      </div>
      <div class="cat-face">
        <div class="cat-eye left">
          <div class="eye-highlight"></div>
          <div class="cat-pupil"></div>
          <div class="eye-shine"></div>
        </div>
        <div class="cat-eye right">
          <div class="eye-highlight"></div>
          <div class="cat-pupil"></div>
          <div class="eye-shine"></div>
        </div>
        <div class="cat-nose"></div>
        <div class="cat-mouth"></div>
        <div class="cat-whiskers left"></div>
        <div class="cat-whiskers right"></div>
      </div>
      <div class="cat-muzzle"></div>
    </div>
    <div class="cat-front-paws">
      <div class="paw left"></div>
      <div class="paw right"></div>
    </div>
    <div class="cat-tail">
      <div class="tail-segment"></div>
      <div class="tail-segment"></div>
      <div class="tail-segment"></div>
    </div>
    <div class="cat-shadow"></div>
  </div>

  <!-- Cat 2: Lying down pose -->
  <div class="cat-avatar realistic-cat" data-cat="2">
    <div class="cat-body">
      <div class="cat-fur-detail"></div>
      <div class="cat-chest"></div>
    </div>
    <div class="cat-head">
      <div class="cat-ear left">
        <div class="ear-inner"></div>
        <div class="ear-tuft"></div>
      </div>
      <div class="cat-ear right">
        <div class="ear-inner"></div>
        <div class="ear-tuft"></div>
      </div>
      <div class="cat-face">
        <div class="cat-eye left">
          <div class="eye-highlight"></div>
          <div class="cat-pupil"></div>
          <div class="eye-shine"></div>
        </div>
        <div class="cat-eye right">
          <div class="eye-highlight"></div>
          <div class="cat-pupil"></div>
          <div class="eye-shine"></div>
        </div>
        <div class="cat-nose"></div>
        <div class="cat-mouth"></div>
        <div class="cat-whiskers left"></div>
        <div class="cat-whiskers right"></div>
      </div>
      <div class="cat-muzzle"></div>
    </div>
    <div class="cat-front-paws">
      <div class="paw left"></div>
      <div class="paw right"></div>
    </div>
    <div class="cat-tail">
      <div class="tail-segment"></div>
      <div class="tail-segment"></div>
      <div class="tail-segment"></div>
    </div>
    <div class="cat-shadow"></div>
  </div>
</div>

<script>
(function() {
  var cats = document.querySelectorAll('.cat-avatar');
  if (!cats.length) return;

  var pupils = document.querySelectorAll('.cat-pupil');
  var eyes = document.querySelectorAll('.cat-eye');

  // Eye tracking - follows mouse
  window.addEventListener('mousemove', function(e) {
    var vw = window.innerWidth || 1;
    var vh = window.innerHeight || 1;
    var relX = (e.clientX / vw - 0.5) * 2;
    var relY = (e.clientY / vh - 0.5) * 2;

    var maxOffset = 3;
    pupils.forEach(function(pupil, idx) {
      var catIndex = Math.floor(idx / 2);
      var cat = cats[catIndex];
      if (!cat) return;
      
      // Check if cat is sleeping
      if (cat.classList.contains('sleeping')) {
        pupil.style.transform = 'translate(0px, 2px) scale(1, 0.1)';
        return;
      }

      var factor = idx % 2 === 0 ? 1 : 0.85;
      var tx = relX * maxOffset * factor;
      var ty = relY * maxOffset * factor * 0.7;
      pupil.style.transform = 'translate(' + tx.toFixed(1) + 'px,' + ty.toFixed(1) + 'px) scale(1, 1)';
    });
  });

  // Random blink animation
  function blinkEyes() {
    eyes.forEach(function(eye, idx) {
      var catIndex = Math.floor(idx / 2);
      var cat = cats[catIndex];
      if (cat && cat.classList.contains('sleeping')) return;

      if (Math.random() < 0.3) {
        eye.style.transform = 'scaleY(0.1)';
        setTimeout(function() {
          eye.style.transform = 'scaleY(1)';
        }, 120);
      }
    });
  }
  setInterval(blinkEyes, 3000);

  // Random animations for each cat
  cats.forEach(function(cat, index) {
    var animationTimer;

    function triggerRandomAnimation() {
      var animations = ['stretch', 'sleeping', 'walk', 'tail-wag'];
      var randomAnim = animations[Math.floor(Math.random() * animations.length)];
      
      // Remove all animation classes first
      animations.forEach(function(anim) {
        cat.classList.remove(anim);
      });

      // Add new animation
      cat.classList.add(randomAnim);

      // Auto-remove after duration
      var duration = randomAnim === 'sleeping' ? 8000 : randomAnim === 'walk' ? 6000 : 3000;
      setTimeout(function() {
        cat.classList.remove(randomAnim);
      }, duration);

      // Schedule next random animation
      var nextDelay = 8000 + Math.random() * 12000; // 8-20 seconds
      animationTimer = setTimeout(triggerRandomAnimation, nextDelay);
    }

    // Start random animations with staggered timing
    setTimeout(function() {
      triggerRandomAnimation();
    }, index * 5000 + Math.random() * 3000);

    // Click interaction - affection response
    cat.addEventListener('click', function() {
      cat.classList.add('petted');
      setTimeout(function() {
        cat.classList.remove('petted');
      }, 800);
    });
  });

  // Breathing animation (continuous subtle movement)
  cats.forEach(function(cat) {
    var body = cat.querySelector('.cat-body');
    if (!body) return;

    var breathePhase = Math.random() * Math.PI * 2;
    setInterval(function() {
      if (cat.classList.contains('sleeping') || cat.classList.contains('walk')) return;
      breathePhase += 0.05;
      var scale = 1 + Math.sin(breathePhase) * 0.01;
      body.style.transform = 'translateX(-50%) scaleY(' + scale.toFixed(3) + ')';
    }, 100);
  });
})();
</script>