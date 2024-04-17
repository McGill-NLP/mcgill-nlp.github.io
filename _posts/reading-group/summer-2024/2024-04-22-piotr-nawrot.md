---
title: "Dynamic Memory Compression: Retrofitting LLMs for Accelerated Inference"
venue: University of Edinburgh
names: Piotr Nawrot
author: Piotr Nawrot
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

The [NLP Reading Group]({% link _pages/reading-group.md %}) is delighted to have [Piotr Nawrot](https://piotrnawrot.github.io/) give a talk about "Dynamic Memory Compression: Retrofitting LLMs for Accelerated Inference".

## Talk Description

Transformers have emerged as the backbone of large language models (LLMs). However, generation remains inefficient due to the need to store in memory a cache of key-value representations for past tokens, whose size scales linearly with the input sequence length and batch size. As a solution, we propose Dynamic Memory Compression (DMC), a method for on-line key-value cache compression at inference time. Most importantly, the model learns to apply different compression rates in different heads and layers. We retrofit pre-trained LLMs such as Llama 2 (7B, 13B and 70B) into DMC Transformers, achieving up to ~3.7x throughput increase in auto-regressive inference on a NVIDIA H100 GPU. DMC is applied via continued pre-training on a negligible percentage of the original data without adding any extra parameters. We find that DMC preserves the original downstream performance with up to 4x cache compression, outperforming up-trained grouped-query attention (GQA). GQA and DMC can be even combined to obtain compounded gains. As a result DMC fits longer contexts and larger batches within any given memory budget.

## Speaker Bio

Piotr Nawrot is a second-year PhD student at the University of Edinburgh advised by Edoardo Maria Ponti and Ivan Titov. His research focuses broadly on improving the efficiency of neural models. More specifically, he is interested in learnable strategies to compress a sequence of tokens which could pave the way for tokenisation-free architectures and more compute-optimal models.

## Logistics

*TBA*