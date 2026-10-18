---
layout: compress
title: "Material 1 - Full PDF"
excerpt: ""
author_profile: true
permalink: /1-diffusion-page/
redirect_from: 
  - /1-diffusion-page.html
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

# Frontiers in Diffusion Model Technologies (1)

This document provides an overview of key concepts related to diffusion models, particularly focusing on the theoretical foundations, development timeline, and recent advancements in the field. The content includes detailed discussions on VAE, DDPM, DDIM, SDE, and ODE, as well as conditional guidance. It also covers the evolution of stable diffusion, including topics like Latent Diffusion, VQ-VAE, and DiT. Lastly, the document highlights the latest methodology, IC-Light, set to be presented at ICLR 2025.

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
        source: "/pdfs/2024-12-08_diffusion.pdf",  
        tabs: [
        {title: "Section 1", page: 2, color: "orange"},
        ]
    });
    });
</script>
