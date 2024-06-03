---
title: "LLMs as Text Encoders"
venue: McGill University
names: Vaibhav Adlakha
author: Vaibhav Adlakha
tags:
- NLP RG
categories:
    - Reading-Group
    - Summer-2024
layout: archive
classes:
    - wide
    - no-sidebar
---

*{{ page.names }}*

**{{ page.venue }}**

{% include display-publication-links.html pub=page %}

The [NLP Reading Group]({% link _pages/reading-group.md %}) is happy to have [Vaibhav Adlakha]([https://tianbaoxie.com/](https://vaibhavad.github.io/)) give a talk about "LLM2Vec: Large Language Models Are Secretly Powerful Text Encoders".

## Talk Description

Large decoder-only language models (LLMs) are the state-of-the-art models on most of today's NLP tasks and benchmarks. Yet, the community is only slowly adopting these models for text embedding tasks, which require rich contextualized representations. In this work, we introduce LLM2Vec, a simple unsupervised approach that can transform any decoder-only LLM into a strong text encoder. LLM2Vec consists of three simple steps: 1) enabling bidirectional attention, 2) masked next token prediction, and 3) unsupervised contrastive learning. We demonstrate the effectiveness of LLM2Vec by applying it to 3 popular LLMs ranging from 1.3B to 7B parameters and evaluate the transformed models on English word- and sequence-level tasks. We outperform encoder-only models by a large margin on word-level tasks and reach a new unsupervised state-of-the-art performance on the Massive Text Embeddings Benchmark (MTEB). Moreover, when combining LLM2Vec with supervised contrastive learning, we achieve state-of-the-art performance on MTEB among models that train only on publicly available data. Our strong empirical results and extensive analysis demonstrate that LLMs can be effectively transformed into universal text encoders in a parameter-efficient manner without the need for expensive adaptation or synthetic GPT-4 generated data.

## Speaker Bio

Vaibhav Adlakha is a PhD student at McGill University and Mila and a Visiting Researcher at ServiceNow Research, advised by Prof Siva Reddy. He is interested in the interplay of knowledge and language in LLMs. His recent research focuses on improving text representations, specifically for retrieval-augmented generation (RAG) applications. Before McGill, he was a research assistant at NLP Group, Indian Institute of Technology Delhi (IIT-Delhi) and a software developer at Samsung Research Institute. He obtained B.Tech in Mathematics and Computing from Indian Institute of Technology Guwahati (IIT-Guwahati).

## Logistics

Date: June 3rd <br>
Time: 11:00AM <br>
Location: J09 or via Zoom (See email)
