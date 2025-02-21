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

I am a PhD student at the Institute of Science and Technology for Brain-inspired Intelligence (ISTBI) at Fudan University. I obtained my Bachelor's degree from the School of Aerospace Engineering at Xiamen University. 

My research focuses on Visual Simultaneous Localization and Mapping (VSLAM) and volumetric rendering techniques, particularly Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS). In the future, I aim to develop an efficient and robust SLAM system based on volumetric rendering. Feel free to reach out if you'd like to **learn more about my work**, **chat**, or explore potential **collaborations**.

<!-- I have published more than 100 papers at the top international AI conferences with total <a href='https://scholar.google.com/citations?user=DhtAFkwAAAAJ'>google scholar citations <strong><span id='total_cit'>260000+</span></strong></a> (You can also use google scholar badge <a href='https://scholar.google.com/citations?user=DhtAFkwAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>). -->


# 🔥 News
- *2024.03*: 🎉 [VPL-SLAM](https://ieeexplore.ieee.org/document/10461980) is accepted by **IEEE Transactions on Intelligent Transportation Systems**. Congrats to Qi.
- *2024.01*: 🎉 [Multi-Lio](https://ieeexplore.ieee.org/document/10611257) is accepted by **ICRA 2024**. Congrats to Qi.
<!-- Honored to collaborate with them on these promising projects. -->

# 📝 Publications 


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Arxiv preprint</div><img src='images/2024_09_PAPL_SLAM/PAPL_SLAM.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[PAPL-SLAM: Principal Axis-Anchored Monocular Point-Line SLAM](https://arxiv.org/pdf/2410.12324)

 **Guanghao Li**, Yu Cao, Qi Chen, Yifan Yang, Jian Pu

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=6nkKQDIAAAAJ&citation_for_view=6nkKQDIAAAAJ:9yKSN-GCB0IC) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>

- PAPL-SLAM is a point-line SLAM system that efficiently integrates line structural information and optimization by anchoring lines to a principal axis, reducing the number of parameters, and utilizing probabilistic data association, enabling robust, rapid, and accurate mapping and tracking in both indoor and outdoor environments.
</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Arxiv preprint</div><img src='images/2023_12_EC_SLAM/EC_SLAM.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[EC-SLAM: Real-time Dense Neural RGB-D SLAM System with Effectively Constrained Global Bundle Adjustment](https://ui.adsabs.harvard.edu/abs/2024arXiv240413346L/abstract)

 **Guanghao Li\***, Qi Chen\*, Yuxiang Yan, Jian Pu

[![GitHub Stars](https://img.shields.io/github/stars/Lightingooo/EC-SLAM?style=social)](https://github.com/Lightingooo/EC-SLAM)
[![GitHub Forks](https://img.shields.io/github/forks/Lightingooo/EC-SLAM?style=social)](https://github.com/Lightingooo/EC-SLAM)
[[Project page]](https://github.com/Lightingooo/EC-SLAM)

- EC-SLAM is a real-time dense RGB-D SLAM system that leverages Neural Radiance Fields (NeRF) for enhanced pose optimization, using sparse parametric encodings, TSDF, and a globally constrained Bundle Adjustment strategy to improve tracking accuracy and reconstruction performance in real-time.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICRA 2024</div><img src='images/2024_01_Multi_lio/Multi_lio.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Multi-LIO: A Lightweight Multiple LiDAR-Inertial Odometry System](https://ieeexplore.ieee.org/abstract/document/10611257)

Qi Chen\*, **Guanghao Li\***, Xiangyang Xue, Jian Pu

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=6nkKQDIAAAAJ&citation_for_view=6nkKQDIAAAAJ:d1gkVwhDpl0C) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- Multi-LIO is a real-time, computationally efficient multiple LiDAR-inertial odometry system that enhances accuracy and scalability, using parallel state updates, voxelized maps, and point-wise uncertainty estimation to improve scan-to-map registration in large-scale, complex environments.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TITS</div><img src='images/2024_03_VPL-SLAM/under00_frame.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[VPL-SLAM: A Vertical Line Supported Point Line Monocular SLAM System](https://ieeexplore.ieee.org/document/10461980)

Qi Chen, Yu Cao, Jiawei Hou, **Guanghao Li**, Bo Chen, Xiangyang Xue, Hong Lu, Jian Pu

[**Project**](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=6nkKQDIAAAAJ&citation_for_view=6nkKQDIAAAAJ:u5HHmVD_uO8C) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- VPL-SLAM is a monocular SLAM system that improves localization and mapping in complex environments by integrating structural vertical lines with point-line features.
</div>
</div>


<!-- - [Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet](https://github.com), A, B, C, **CVPR 2020** -->

# 🎖 Honors and Awards
- 2022.09 Fudan University Zhicheng Freshman Second Prize Scholarship (Top 5%)
- 2022.05 Outstanding Graduates of Fujian Province and Xiamen University

# 👨‍💼 Academic Service
- Journal Reviewer: RA-L
- Conference Reviewer: ICME2025
- Teaching assistant: Embodied Intelligence

# 📖 Educations
- *2022.08 - 2027.06 (now)*, Ph.D., Fudan University, Shanghai, China.
- *2018.09 - 2022.06*, Bachelor of Automation, Xiamen Univeristy, Xiamen, China.

# 💬 Invited Talks
<!-- - *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/) -->

# 💻 Internships
<!-- - *2019.05 - 2020.02*, [Lorem](https://github.com/), China. -->