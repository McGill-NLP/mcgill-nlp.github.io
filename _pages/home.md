---
permalink: /
title: "Complex Data Lab @ McGill / Mila"
layout: splash
header:
    overlay_filter: rgba(237, 27, 47, 0.3)
    overlay_image: /assets/images/trottier.webp
    actions:
        - label: "GitHub"
          url: "https://github.com/ComplexData-MILA"
        - label: "Twitter"
          url: "https://x.com/complexDataLab"
        - label: "LinkedIn"
          url: "https://www.linkedin.com/company/complex-data-lab-mcgill-mila"

excerpt: "Complex Data Lab is a research group within McGill University and Mila focusing on network science and applied machine learning."

row_research:
  - image_path: /assets/images/home/group-photo-1.webp
    url: /publications
    alt: "Poster Presentation"
    title: "Research"
    btn_label: "Publications"
    btn_class: "btn--primary"
    excerpt: "We work on various topics, including algorithms analyzing temporal graphs, applying machine learning on the health of online societies (crime & online markets, politics & online media, toxicity & online games). We present our works in ML and NLP conferences and journals."

row_code:
  - image_path: /assets/images/home/github.webp
    url: https://github.com/ComplexData-MILA
    alt: "Our GitHub page"
    title: "Open-Source Code"
    btn_label: "GitHub"
    btn_class: "btn--primary"
    excerpt: "We publish code for our models and datasets on GitHub to make it easier for researchers and developers to reproduce and build upon our work. We welcome pull requests and issues on active projects from the community."

row_about_us:
  - image_path: /assets/images/home/misinfo_gov_outreach.webp
  - image_path: /assets/images/home/web_retrieval_mila_outreach.webp
  - image_path: /assets/images/home/web_retrieval_colm_outreach.webp

---
{% comment %}
Based on: https://raw.githubusercontent.com/mmistakes/minimal-mistakes/master/docs/_pages/splash-page.md
{% endcomment %}


{% include feature_row id="row_research" type="left" %}

{% include feature_row id="row_code" type="right" %}

# Join Us
{: .text-center}

Complex Data Lab welcomes graduate students, interns, and researchers at various levels. We have opportunities for Masters and PhD students, postdocs, research assistants, and visiting researchers. 
{: .text-center}

For detailed information on how to apply and join our lab, please visit our [Join Us](/join-us) page.
{: .text-center}
<br/>


# About Us
{: .text-center}

We are a group of faculty members, researchers and students affiliated with McGill University and Mila Quebec AI Institute, both located in Montreal, Canada. We often collaborate with researchers around the world.
{: .text-center}

{% include feature_row id="row_about_us" %}

