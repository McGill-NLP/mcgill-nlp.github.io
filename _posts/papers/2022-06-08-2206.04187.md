---
title: Few-shot Question Generation for Personalized Feedback in Intelligent Tutoring
  Systems
venue: PAIS@ECAI
names: Devang Kulshreshtha, Muhammad Shayan, Robert Belfer, Siva Reddy, Iulian Serban,
  E. Kochmar
tags:
- PAIS@ECAI
link: https://arxiv.org/abs/2206.04187
author: Devang Kulshreshtha
categories: Publications

---

*{{ page.names }}*

**{{ page.venue }}**

{% include display-publication-links.html pub=page %}

## Abstract

Existing work on generating hints in Intelligent Tutoring Systems (ITS) focuses mostly on manual and non-personalized feedback. In this work, we explore automatically generated questions as personalized feedback in an ITS. Our personalized feedback can pinpoint correct and incorrect or missing phrases in student answers as well as guide them towards correct answer by asking a question in natural language. Our approach combines cause–effect analysis to break down student answers using text similarity-based NLP Transformer models to identify correct and incorrect or missing parts. We train a few-shot Neural Question Generation and Question Re-ranking models to show questions addressing components missing in the student’s answers which steers students towards the correct answer. Our model vastly outperforms both simple and strong baselines in terms of student learning gains by 45% and 23% respectively when tested in a real dialogue-based ITS. Finally, we show that our personalized corrective feedback system has the potential to improve Generative Question Answering systems.