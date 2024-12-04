---
title: Toxicity & Online Games
layout: splash
category: research-directions
order: 4
header:
    overlay_filter: linear-gradient(rgba(255, 255, 255, 0.1), rgba(0, 0, 0, 0.4))
    overlay_image: /assets/images/research_directions/online-toxicity/dystopian_city.webp
excerpt: "Our team collaborates with game companies like Ubisoft to develop responsible, real-time, human-in-the-loop AI systems for chat toxicity detection, creating safer online gaming communities."
logo_image_path: /assets/images/home/TOG_logo-light.png
logo_dark_image_path: /assets/images/home/TOG_logo-dark.png
one-liner: "Building real-time, human-in-the-loop systems to foster healthier gaming communities, partnering with industry leaders to deploy scalable solutions that adapt to emerging challenges."

projects:
  - title: "Game on, Hate off"
    alt: "Game on, Hate off"
    image_path: /assets/images/research_directions/online-toxicity/game-on-hate-off.jpg
    excerpt: "While game companies are addressing the call to reduce toxicity and promote player health, the need to understand toxicity trends across time is important. With a reliable toxicity detection model (average precision of 0.95), we apply our model to eight months’ worth of in-game chat data, offering visual insights into toxicity trends for Rainbow Six Siege and For Honor, two games developed by Ubisoft. Ultimately, this study serves as a foundation for future research in creating more inclusive and enjoyable online gaming experiences."
    url: https://dl.acm.org/doi/10.1145/3675805
  - title: "ToxBuster"
    alt: "ToxBuster"
    image_path: /assets/images/research_directions/online-toxicity/toxbuster.jpg
    excerpt: "A simple and scalable model that reliably detects toxic content in real-time for a line of chat by including chat history and metadata. ToxBuster consistently outperforms conventional toxicity models across popular multiplayer games, including Rainbow Six Siege, For Honor, and DOTA 2. We conduct an ablation study to assess the importance of each model component and explore ToxBuster’s transferability across the datasets. Furthermore, we showcase ToxBuster’s efficacy in post-game moderation, successfully flagging 82.1% of chat-reported players at a precision level of 90.0%. Additionally, we show how an additional 6% of unreported toxic players can be proactively moderated."
    url: "https://aclanthology.org/2023.findings-emnlp.663/"
  - title: "ToxPlainer"
    alt: "ToxPlainer"
    image_path: /assets/images/research_directions/online-toxicity/toxplainer.jpg
    excerpt: "Identity biases arise commonly from annotated datasets, can be propagated in language models and can cause further harm to marginal groups. Existing bias benchmarking datasets are mainly focused on gender or racial biases and are made to pinpoint which class the model is biased towards. They also are not designed for the gaming industry, a concern for models built for toxicity detection in videogames’ chat."
    url: https://aclanthology.org/2023.emnlp-industry.26/

logos:
  - image: /assets/images/logo/ubisoft-la-forge.png
    name: Ubisoft La Forge
  - image: /assets/images/logo/CIFAR.png
    name: CIFAR
  - image: /assets/images/logo/NSERC.png
    name: NSERC
  - image: /assets/images/logo/mitacs.png
    name: Mitacs
---


# Why should we care?"

Toxic and harmful speech online is more than just unpleasant; it has widespread social and economic repercussions, particularly as it permeates social media and gaming platforms. In gaming, where toxicity affects 75% of young players, this behavior harms mental health, alienates communities, and even reduces player engagement and spending, which impacts the industry’s bottom line. Beyond financial losses, unchecked toxicity risks fostering real-world violence and inciting harmful social behaviors. Despite advances in detection methods, including AI-driven moderation, the ever-evolving nature of toxic language poses significant challenges to companies and communities alike. Addressing this problem isn’t just about improving user experience—it’s essential for maintaining safe, inclusive, and healthy online spaces.


# Projects

{% include feature_row id="projects"%}

# Core Team Members

{% include team-gallery.html authors=site.data.authors research_direction="online-toxicity" render_current_role=true %}


# Funding

We acknowledge funding from Ubisoft, the Canadian Institute for Advanced Research (CIFAR AI Chair Program), Natural Sciences and Engineering Research Council of Canada (NSERC) Postgraduate Scholarship-Doctoral (PGS D) Award. Funding from Ubisoft is governed through the Mitacs Accelerate Program.

{% include logo-grid.html id="logos" %}
