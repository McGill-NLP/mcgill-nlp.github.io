---
title: The Curious Case of Absolute Position Embeddings
author: Amirhossein Kazemnejad # Add name to show profile in sidebar
categories: Publications # Used to list all posts about publications in /publications/
names: "Koustuv Sinha, Amirhossein Kazemnejad, Siva Reddy, Joelle Pineau, Dieuwke Hupkes, Adina Williams"
link: https://arxiv.org/abs/2210.12574 # link to paper
code: https://github.com/kazemnejad/lm_pos_investigations  # link to code (optional)
twitter: https://twitter.com/koustuvsinha/status/1584928673463169025
thumbnail: /assets/images/papers/lm_pos_investigation.jpg
venue: EMNLP 2022 Findings
tags: EMNLP
---


*{{ page.names }}*

**{{ page.venue }}**

{% include display-publication-links.html pub=page %}

## Abstract

Transformer language models encode the notion of word order using positional information. Most commonly, this positional information is represented by absolute position embeddings (APEs), that are learned from the pretraining data. However, in natural language, it is not absolute position that matters, but relative position, and the extent to which APEs can capture this type of information has not been investigated. In this work, we observe that models trained with APE over-rely on positional information to the point that they break-down when subjected to sentences with shifted position information. Specifically, when models are subjected to sentences starting from a non-zero position (excluding the effect of priming), they exhibit noticeably degraded performance on zero to full-shot tasks, across a range of model families and model sizes. Our findings raise questions about the efficacy of APEs to model the relativity of position information, and invite further introspection on the sentence and word order processing strategies employed by these models.
