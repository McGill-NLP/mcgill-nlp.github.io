---
permalink: /
title: Complex Data Lab
layout: splash
header:
    overlay_image: /assets/images/logo/logo.png
    overlay_css: "background-size&#58; contain; background-repeat&#58; no-repeat;"
excerpt: "A research group focusing on developing techniques for analyzing complex data from online societies, with applications to enhance the health and safety of online spaces."

# Homepage funders strip: logos are collected from the research directions' `logos`;
# `exclude` drops some (by image path) and `extra` adds funders not listed on a research page.
funders:
  exclude:
    - /assets/images/logo/GOOGLE.png
    - /assets/images/logo/SAMSUNG.png
  extra:
    - image: /assets/images/logo/FLI.png
      name: Future of Life Institute

research_links:
  - title: "Tools & Resources"
    url: /tools-and-resources/
    icon: "fas fa-toolbox"
  - title: "Publications"
    url: /publications/
    icon: "fas fa-book-open"
  - title: "STAMINA Reading Group"
    url: /stamina/
    icon: "fas fa-users"

row_research:
  - image_path: /assets/images/home/group-photo-2.webp
    url: /publications
    alt: "Poster Presentation"
    title: "Research"
    btn_label: "Publications"
    btn_class: "btn--primary"
    excerpt: "We work on various topics and present our works in ML and NLP conferences and journals."

---

{% include research-directions.html category="research-directions"%}

{% include research-links.html %}

{% include feature_row id="row_research" type="left" %}

{% include funders-carousel.html %}
