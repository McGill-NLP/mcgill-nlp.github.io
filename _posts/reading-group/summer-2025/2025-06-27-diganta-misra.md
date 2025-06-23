---
title: "Using Shapley interactions to understand how models use structure"
venue: UdeM / Mila
names: Diganta Misra
author: Diganta Misra
tags:
- NLP RG
categories:
    - Reading-Group
    - Summer-2025
layout: archive
classes:
    - wide
    - no-sidebar
---

*{{ page.names }}*

**{{ page.venue }}**

{% include display-publication-links.html pub=page %}

The [NLP Reading Group]({% link _pages/reading-group.md %}) is excited to host [Diganta Misra](https://digantamisra98.github.io/) who will be presenting his work **[Using Shapley interactions to understand how models use structure](https://arxiv.org/abs/2403.13106)**.

## Logistics
Date: Friday June 27 <br>
Time: 1PM <br>
Location: on Zoom, to be screencast at Mila in A14 <br>

## Abstract
Language is an intricately structured system, and a key goal of NLP interpretability is to provide methodological insights for understanding how language models represent this structure internally. In this paper, we use Shapley Taylor interaction indices (STII) in order to examine how language and speech models internally relate and structure their inputs. Pairwise Shapley interactions measure how much two inputs work together to influence model outputs beyond if we linearly added their independent influences, providing a view into how models encode structural interactions between inputs. We relate the interaction patterns in models to three underlying linguistic structures: syntactic structure, non-compositional semantics, and phonetic coarticulation. We find that autoregressive text models encode interactions that correlate with the syntactic proximity of inputs, and that both autoregressive and masked models encode nonlinear interactions in idiomatic phrases with non-compositional semantics. Our speech results show that inputs are more entangled for pairs where a neighboring consonant is likely to influence a vowel or approximant, showing that models encode the phonetic interaction needed for extracting discrete phonemic representations.

## Speaker Bio
Diganta is a ELLIS x IMPRS-IS x Amazon Phd Fellow at the MPI-IS Tübingen supervised by Antonio Orvieto (MPI-IS) and Volkan Cevher (EPFL). His primary research focus revolves around code generation models, novel architecture designs (MoE, HyperNetworks), and holistic evaluations of LLMs. He's a strong advocate for open and transparent AI systems. An ex-Mila graduate, outside of work, he is extremely enthusiastic of soccer, mounain climbing and reading Naoki Urasawa mangas. 
