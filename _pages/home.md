---
permalink: /
title: ""
layout: splash
header:
    overlay_filter: rgba(221, 0, 118, 0.3)
    overlay_image: /assets/images/trottier.webp
    actions:
        - label: "GitHub"
          url: "https://github.com/ComplexData-MILA"
        - label: "Twitter"
          url: "https://x.com/complexDataLab"
        - label: "LinkedIn"
          url: "https://www.linkedin.com/company/complex-data-lab-mcgill-mila"

excerpt: "A research group focusing on developing techniques for analyzing complex data from online societies, with applications to enhance the health and safety of online spaces."

row_research:
  - image_path: /assets/images/home/group-photo-1.webp
    url: /publications
    alt: "Poster Presentation"
    title: "Research"
    btn_label: "Publications"
    btn_class: "btn--primary"
    excerpt: "We work on various topics and present our works in ML and NLP conferences and journals."

research_topics:
  - image_path: /assets/images/home/research-direction-default.png
    url: /
    alt: "Temporal Graph Learning"
    title: "Temporal Graph Learning"
    excerpt: Advancing the frontier of machine learning on time-evolving graphs to better model and predict dynamic real-world networks and relationships.
  - image_path: /assets/images/home/research-direction-default.png
    url: /
    alt: "Crime & Online Markets"
    title: "Crime & Online Markets"
    excerpt: Developing responsible AI solutions to detect and analyze suspicious online patterns, supporting law enforcement and organizations in protecting vulnerable individuals from exploitation
  - image_path: /assets/images/home/research-direction-default.png
    url: /poli-sci/
    alt: "Politics & Online Media"
    title: "Politics & Online Media"
    excerpt: "Investigating how digital platforms and emerging AI technologies shape political discourse, social polarization, and information ecosystems through data-driven computational social science"
  - image_path: /assets/images/home/research-direction-default.png
    url: /
    alt: "Toxicity & Online Games"
    title: "Toxicity & Online Games"
    excerpt: Building real-time, human-in-the-loop systems to foster healthier gaming communities, partnering with industry leaders to deploy scalable solutions that adapt to emerging challenges.

---
{% comment %}
Based on: https://raw.githubusercontent.com/mmistakes/minimal-mistakes/master/docs/_pages/splash-page.md
{% endcomment %}


{% include research-directions.html id="research_topics"%}

{% include feature_row id="row_research" type="left" %}
