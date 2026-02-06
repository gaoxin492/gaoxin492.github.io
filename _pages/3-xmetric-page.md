---
layout: compress
title: "Material 1 - Full PDF"
excerpt: ""
author_profile: true
permalink: /3-xmetric-page/
redirect_from: 
  - /3-xmetric-page.html
---

<!-- Add the necessary meta tags and styles -->
<meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
<link href="/assets/css/jquery.touchPDF.css" rel="stylesheet" media="screen" />

<style>
  body, html {
    background-color: #ffffff;
    height: 100%;
    padding: 0;
    margin: 0;
  }

  #myPDF {
    height: 80%;
    width: 80%;
    margin: 20px auto;
    border: 1px solid #ddd;
    background-color: #f4f4f4;
  }
</style>

<div class="material-layout" markdown="1">

# EM Algorithm and X-metric

This document introduces the X-metric framework (<a href="https://ieeexplore.ieee.org/document/9965747" target="_blank">PAMI 2023</a>), an N-dimensional information-theoretic approach designed for groupwise registration and deep combined computing, with applications in advanced machine learning tasks. It also covers the theoretical foundations, including entropy, mutual information, and the MLE algorithm, alongside the framework's modifications for deep computing and network training.

</div>

<div class="material-viewer">
  <div class="material-viewer-label">Interactive PDF (scroll, zoom, and swipe through the slides)</div>
  <div id="myPDF" style="height: 80%; width: 80%; margin: auto;"></div>
</div>

<script type="text/javascript" src="/assets/js/pdf.compatibility.js"></script>
<script type="text/javascript" src="/assets/js/pdf.js"></script>
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
<script type="text/javascript" src="/assets/js/jquery.touchSwipe.js"></script>
<script type="text/javascript" src="/assets/js/jquery.touchPDF.js"></script>
<script type="text/javascript" src="/assets/js/jquery.panzoom.js"></script>
<script type="text/javascript" src="/assets/js/jquery.mousewheel.js"></script>

<!-- TouchPDF initialization script -->
<script type="text/javascript">
    $(function() {
    $("#myPDF").pdf({
        source: "/pdfs/2023-12-21_xmetric.pdf",  
        tabs: [
        {title: "Section 1", page: 2, color: "orange"},
        ]
    });
    });
</script>
