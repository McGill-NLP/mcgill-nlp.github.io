---
title: "Robust Reward Modeling via Causal Rubrics"
venue: UC Berkeley
names: Harman Singh
author: Harman Singh
tags:
- NLP RG
categories:
    - Reading-Group
    - Fall-2025
layout: archive
classes:
    - wide
    - no-sidebar
---

*{{ page.names }}*

**{{ page.venue }}**

{% include display-publication-links.html pub=page %}

The [NLP Reading Group]({% link _pages/reading-group.md %}) is delighted to host [Harman Singh](https://harmandotpy.github.io/) who will be giving a talk **remotely** on "Robust Reward Modeling via Causal Rubrics".

## Talk Description
Reward models (RMs) are fundamental to aligning Large Language Models (LLMs) via human feedback, yet they often suffer from reward hacking. They tend to latch on to superficial or spurious attributes, such as response length or formatting, mistaking these cues learned from correlations in training data for the true causal drivers of quality (e.g., factuality, relevance). This occurs because standard training objectives struggle to disentangle these factors, leading to brittle RMs and misaligned policies. 
We introduce CROME (Causally Robust Reward Modeling), a novel framework grounded in an explicit causal model designed to mitigate reward hacking. CROME employs the following synthetic targeted augmentations during training: (1) Causal Augmentations, which are pairs that differ along specific causal attributes, to enforce sensitivity along each causal attribute individually, and (2) Neutral Augmentations, which are tie-label pairs varying primarily in spurious attributes, to enforce invariance along spurious attributes. Notably, our augmentations are produced without any knowledge of spurious factors, via answer interventions only along causal rubrics, that are identified by querying an oracle LLM. Empirically, CROME outperforms standard baselines on RewardBench, with significant gains on safety and reasoning. It also shows consistent robustness under Best-of-N and DPO alignment settings.

## Speaker Bio

Harman Singh is a PhD student at UC Berkeley, advised by Kurt Keutzer. His current research spans reasoning and diffusion-based language models. Previously, he was a researcher at Google DeepMind, where he contributed to the development of Gemini 2.5 and Gemma 3 models focusing on large-scale multimodal and multilingual modeling, alignment, and reasoning.

## Logistics

Date: October 31st<br>
Time: 2:00PM <br>
Location: H04 or via Google Meet (See email)
