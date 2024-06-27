---
permalink: /
title: "McGill Natural Language Processing"
layout: splash
header:
    overlay_filter: rgba(237, 27, 47, 0.3)
    overlay_image: /assets/images/trottier.webp
    actions:
        - label: "GitHub"
          url: "https://github.com/McGill-NLP"
        - label: "Twitter"
          url: "https://twitter.com/McGill_NLP"

excerpt: "McGill NLP is a research group within McGill University and Mila focusing on various topics in natural language processing."

row_research:
  - image_path: /assets/images/home/poster-1.webp
    url: /publications
    alt: "Poster Presentation"
    title: "Research"
    btn_label: "Publications"
    btn_class: "btn--primary"
    excerpt: "We work on various topics, including semantic parsing, question answering, reading comprehension, and conversational systems. We present our works in Computational Linguistics, NLP and ML conferences and journals."

row_code:
  - image_path: /assets/images/home/github.webp
    url: https://github.com/McGill-NLP
    alt: "Our GitHub page"
    title: "Open-Source Code"
    btn_label: "GitHub"
    btn_class: "btn--primary"
    excerpt: "We publish code for our models and datasets on GitHub to make it easier for researchers and developers to reproduce and build upon our work. We welcome pull requests and issues on active projects from the community."
  
row_about_us:
  - image_path: /assets/images/home/retreat-2023.webp
  - image_path: /assets/images/home/lunch-1.webp
  - image_path: /assets/images/home/jackie-axes-2019.webp
  - image_path: /assets/images/home/park-1.webp
  - image_path: /assets/images/home/coffee-acl-2022.webp
  - image_path: /assets/images/home/michaela-acl-2022.webp
  - image_path: /assets/images/home/zichao-acl-2022.webp
  - image_path: /assets/images/home/benno-acl-2022.webp
  - image_path: /assets/images/home/nick-acl-2022.webp
  - image_path: /assets/images/home/vaibhav-acl-2022.webp


---
{% comment %}
Based on: https://raw.githubusercontent.com/mmistakes/minimal-mistakes/master/docs/_pages/splash-page.md
{% endcomment %}


{% include feature_row id="row_research" type="left" %}

{% include feature_row id="row_code" type="right" %}

# Join Us
{: .text-center}

We accept graduate students (Masters or PhD) through official Mila and McGill application channels. For internship opportunities and other positions, please apply using our <a href="https://forms.gle/3SA5K6pJxe4dAyhM7">Google Form</a>.
{: .text-center}
<br/>


# About Us
{: .text-center}

We are a group of faculty members, researchers and students affiliated with McGill University and Mila Quebec AI Institute, both located in Montreal, Canada. We often collaborate with researchers around the world.
{: .text-center}

{% include feature_row id="row_about_us" %}

