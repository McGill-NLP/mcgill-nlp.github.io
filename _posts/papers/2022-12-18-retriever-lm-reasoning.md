---
title: Can Retriever-Augmented Language Models Reason? The Blame Game Between the
  Retriever and the Language Model
author: Parishad BehnamGhader
names: Parishad BehnamGhader, Santiago Miret, Siva Reddy
venue: ArXiv
link: https://arxiv.org/abs/2212.09146
tags:
- ArXiv
code: https://github.com/McGill-NLP/retriever-lm-reasoning
thumbnail: /assets/images/papers/retriever-lm-reasoning.jpg
categories: Publications

---

*{{ page.names }}*

**{{ page.venue }}**

{% include display-publication-links.html pub=page %}

## Abstract

The emergence of large pretrained models has enabled language models to achieve superior performance in common NLP tasks, including language modeling and question answering, compared to previous static word representation methods. Augmenting these models with a retriever to retrieve the related text and documents as supporting information has shown promise in effectively solving NLP problems in a more interpretable way given that the additional knowledge is injected explicitly rather than being captured in the models' parameters. In spite of the recent progress, our analysis on retriever-augmented language models shows that this class of language models still lack reasoning over the retrieved documents. In this paper, we study the strengths and weaknesses of different retriever-augmented language models such as REALM, kNN-LM, FiD, ATLAS, and Flan-T5 in reasoning over the selected documents in different tasks. In particular, we analyze the reasoning failures of each of these models and study how the models' failures in reasoning are rooted in the retriever module as well as the language model.