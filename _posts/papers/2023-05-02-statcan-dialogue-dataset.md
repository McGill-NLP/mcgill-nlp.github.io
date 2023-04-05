---
title: 'The StatCan Dialogue Dataset: Retrieving Data Tables through Conversations
  with Genuine Intents'
author: Xing Han Lu
names: Xing Han Lu, Siva Reddy, Harm de Vries
venue: EACL
link: https://arxiv.org/abs/2304.01412
tags:
- EACL
code: https://github.com/McGill-NLP/statcan-dialogue-dataset
webpage: https://mcgill-nlp.github.io/statcan-dialogue-dataset/
thumbnail: /assets/images/papers/statcan-dialogue-dataset.png
categories: Publications

---

*{{ page.names }}*

**{{ page.venue }}**

{% include display-publication-links.html pub=page %}

## Abstract

We introduce the StatCan Dialogue Dataset consisting of 19,379 conversation turns between agents working at Statistics Canada and online users looking for published data tables. The conversations stem from genuine intents, are held in English or French, and lead to agents retrieving one of over 5000 complex data tables. Based on this dataset, we propose two tasks: (1) automatic retrieval of relevant tables based on a on-going conversation, and (2) automatic generation of appropriate agent responses at each turn. We investigate the difficulty of each task by establishing strong baselines. Our experiments on a temporal data split reveal that all models struggle to generalize to future conversations, as we observe a significant drop in performance across both tasks when we move from the validation to the test set. In addition, we find that response generation models struggle to decide when to return a table. Considering that the tasks pose significant challenges to existing models, we encourage the community to develop models for our task, which can be directly used to help knowledge workers find relevant tables for live chat users.