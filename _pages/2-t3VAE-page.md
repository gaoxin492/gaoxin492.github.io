---
layout: compress
title: "Material 1 - Full PDF"
excerpt: ""
author_profile: true
permalink: /2-t3VAE-page/
redirect_from: 
  - /2-t3VAE-page.html
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

# Tutorial of Information Geometry and t3-VAE

This document introduces the t3-Variational Autoencoder (<a href="https://openreview.net/pdf?id=RzNlECeoOB" target="_blank">ICLR 2023</a>), which uses Student’s t-distributions to model heavy-tailed data distributions and improve latent variable representations. It also explores the framework of Information Geometry, focusing on how generative models can be understood through statistical manifolds, divergences, and Riemannian metrics, providing a deeper understanding of probability distributions and their applications in machine learning, signal processing, and neuroscience.

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
        source: "/pdfs/2024-04-27_JC-t3VAE.pdf",  
        tabs: [
        {title: "Section 1", page: 2, color: "orange"},
        ]
    });
    });
</script>
