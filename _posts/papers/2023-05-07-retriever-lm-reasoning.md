---
title: Can Retriever-Augmented Language Models Reason? The Blame Game Between the
  Retriever and the Language Model
author: Parishad BehnamGhader
names: Parishad BehnamGhader, Santiago Miret, Siva Reddy
venue: EMNLP Findings
link: https://arxiv.org/abs/2212.09146
tags:
- EMNLP
code: https://github.com/McGill-NLP/retriever-lm-reasoning
thumbnail: /assets/images/papers/retriever-lm-reasoning-2.jpg
categories: Publications

---

*{{ page.names }}*

**{{ page.venue }}**

{% include display-publication-links.html pub=page %}

## Abstract

Augmenting pretrained language models with retrievers has shown promise in effectively solving common NLP problems, such as language modeling and question answering. In this paper, we evaluate the strengths and weaknesses of popular retriever-augmented language models, namely kNN-LM, REALM, DPR + FiD, Contriever + ATLAS, and Contriever + Flan-T5, in reasoning over retrieved statements across different tasks. Our findings indicate that the simple similarity metric employed by retrievers is insufficient for retrieving all the necessary statements for reasoning. Additionally, the language models do not exhibit strong reasoning even when provided with only the required statements. Furthermore, when combined with imperfect retrievers, the performance of the language models becomes even worse, e.g., Flan-T5's performance drops by 28.6% when retrieving 5 statements using Contriever. While larger language models improve performance, there is still a substantial room for enhancement. Our further analysis indicates that multihop retrieve-and-read is promising for large language models like GPT-3.5, but does not generalize to other language models like Flan-T5-xxl.
