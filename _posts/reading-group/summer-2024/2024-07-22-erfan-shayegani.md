---
title: Cross-Modality Safety Alignment in Multi-Modal LLMs
venue: UC Riverside
names: Erfan Shayegani
author: Erfan Shayegani
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

The [NLP Reading Group]({% link _pages/reading-group.md %}) is excited to receive [Erfan Shayegani](https://erfanshayegani.github.io/) who will be giving a talk on his recent work in "Cross-Modality Safety Alignment in Multi-Modal LLMs".

## Paper Abstract

We introduce new jailbreak attacks on vision language models (VLMs), which use aligned LLMs and are resilient to text-only jailbreak attacks. Specifically, we develop cross-modality attacks on alignment where we pair adversarial images going through the vision encoder with textual prompts to break the alignment of the language model. Our attacks employ a novel compositional strategy that combines an image, adversarially targeted towards toxic embeddings, with generic prompts to accomplish the jailbreak. Thus, the LLM draws the context to answer the generic prompt from the adversarial image. The generation of benign-appearing adversarial images leverages a novel embedding-space-based methodology, operating with no access to the LLM model. Instead, the attacks require access only to the vision encoder and utilize one of our four embedding space targeting strategies. By not requiring access to the LLM, the attacks lower the entry barrier for attackers, particularly when vision encoders such as CLIP are embedded in closed-source LLMs. The attacks achieve a high success rate across different VLMs, highlighting the risk of cross-modality alignment vulnerabilities, and the need for new alignment approaches for multi-modal models.

[https://arxiv.org/abs/2307.14539](https://arxiv.org/abs/2307.14539)

## Speaker Bio

Erfan Shayegani (He/Him) is a 2nd year PhD student at UCR in Computer Science and is advised by Prof. Nael Abu-Ghazaleh and Prof. Yue Dong[^1]. Erfan’s research interests span AI Safety, Multi-Modal Understanding, and AR/VR Security & Privacy, and he has been working on Cross-Modality Safety Alignment issues of Multi-Modal Large Language Models (MLLMs) and potential alignment approaches such as unlearning. His works have been published in prestigious venues such as ICLR Spotlight, USENIX Security and ACL including  a Best Paper award at SoCalNLP2023. In this talk, he will be presenting his work on Cross-Modality Safety Alignment in Multi-Modal models and discusses potential mitigations. 

[^1]: Prof. Yue Dong is a former McGill NLP member! In fact, she was once an organizer for the NLP reading group 🔥

## Logistics

Date: July 22nd<br>
Time: 11:00AM <br>
Location: F01 or via Zoom (See email)
