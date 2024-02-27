---
title: 'MAGNIFICo: Evaluating the In-Context Learning Ability of Large Language Models
  to Generalize to Novel Interpretations'
author: Arkil Patel
names: Arkil Patel, Satwik Bhattamishra, Siva Reddy, Dzmitry Bahdanau
venue: EMNLP
link: https://arxiv.org/abs/2310.11634
tags:
- EMNLP
- LLMs
- In-context learning
- Evaluation
code: https://github.com/McGill-NLP/MAGNIFICo
webpage: https://mcgill-nlp.github.io/MAGNIFICo
thumbnail: /assets/images/papers/magnifico.jpg
categories: Publications

---

*{{ page.names }}*

**{{ page.venue }}**

{% include display-publication-links.html pub=page %}

## Abstract

Humans possess a remarkable ability to assign novel interpretations to linguistic expressions, enabling them to learn new words and understand community-specific connotations. However, Large Language Models (LLMs) have a knowledge cutoff and are costly to finetune repeatedly. Therefore, it is crucial for LLMs to learn novel interpretations in-context. In this paper, we systematically analyse the ability of LLMs to acquire novel interpretations using in-context learning. To facilitate our study, we introduce MAGNIFICo, an evaluation suite implemented within a text-to-SQL semantic parsing framework that incorporates diverse tokens and prompt settings to simulate real-world complexity. Experimental results on MAGNIFICo demonstrate that LLMs exhibit a surprisingly robust capacity for comprehending novel interpretations from natural language descriptions as well as from discussions within long conversations. Nevertheless, our findings also highlight the need for further improvements, particularly when interpreting unfamiliar words or when composing multiple novel interpretations simultaneously in the same example. Additionally, our analysis uncovers the semantic predispositions in LLMs and reveals the impact of recency bias for information presented in long contexts.
