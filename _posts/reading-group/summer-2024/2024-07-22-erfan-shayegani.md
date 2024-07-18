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

Recent studies reveal that integrating new modalities into Large Language Models (LLMs), such as Vision-Language Models (VLMs), creates a new attack surface that bypasses existing safety training techniques like Supervised Fine-tuning (SFT) and Reinforcement Learning with Human Feedback (RLHF). While further SFT and RLHF-based safety training can be conducted in multi-modal settings, collecting multi-modal training datasets poses a significant challenge. Inspired by the structural design of recent multi-modal models, where, regardless of the combination of input modalities, all inputs are ultimately fused into the language space, we aim to explore whether unlearning solely in the textual domain can be effective for cross-modality safety alignment. Our evaluation across six datasets empirically demonstrates the transferability—textual unlearning in VLMs significantly reduces the Attack Success Rate (ASR) to less than 8% and in some cases, even as low as nearly 2% for both text-based and vision-text-based attacks, alongside preserving the utility. Moreover, our experiments show that unlearning with a multi-modal dataset offers no potential benefits but incurs significantly increased computational demands, possibly up to 6 times higher.

[https://arxiv.org/html/2406.02575v1](https://arxiv.org/html/2406.02575v1)

## Speaker Bio

Erfan Shayegani (He/Him) is a 2nd year PhD student at UCR in Computer Science and is advised by Prof. Nael Abu-Ghazaleh and Prof. Yue Dong[^1]. Erfan’s research interests span AI Safety, Multi-Modal Understanding, and AR/VR Security & Privacy, and he has been working on Cross-Modality Safety Alignment issues of Multi-Modal Large Language Models (MLLMs) and potential alignment approaches such as unlearning. His works have been published in prestigious venues such as ICLR Spotlight, USENIX Security and ACL including  a Best Paper award at SoCalNLP2023. In this talk, he will be presenting his work on Cross-Modality Safety Alignment in Multi-Modal models and discusses potential mitigations. 

[^1]: Prof. Yue Dong is a former McGill NLP member! In fact, she was once an organizer for the NLP reading group 🔥

## Logistics

Date: July 22nd<br>
Time: 11:00AM <br>
Location: F01 or via Zoom (See email)
