---
title: "A Modular Approach for Clinical SLMs Driven by Synthetic Data with Pre-Instruction Tuning, Model Merging, and Clinical Alignment"
venue: Microsoft
names: Jean-Philippe Corbeil
author: Jean-Philippe Corbeil
tags:
- NLP RG
categories:
    - Reading-Group
    - Winter-2025
layout: archive
classes:
    - wide
    - no-sidebar
---

*{{ page.names }}*

**{{ page.venue }}**

{% include display-publication-links.html pub=page %}

The [NLP Reading Group]({% link _pages/reading-group.md %}) is excited to host [Jean-Philippe Corbeil](https://www.linkedin.com/in/jpcorb20/), a Senior Research Scientist at Microsoft, who will be discussing their work on developing clinical small language models with synthetic data and pre-instruction tuning. The talk will happen on Zoom and in A14 on Friday April 11th at 1PM.
## Talk Description

High computation costs and latency of large language models such as GPT-4 have limited their deployment in clinical settings. Small language models (SLMs) offer a cost-effective alternative, but their limited capacity requires biomedical domain adaptation, which remains challenging. An additional bottleneck is the unavailability and high sensitivity of clinical data. To address these challenges, we propose a novel framework for adapting SLMs into high-performing clinical models. We introduce the MediPhi collection of 3.8B-parameter SLMs developed with our novel framework: pre-instruction tuning of experts on relevant medical and clinical corpora (PMC, Medical Guideline, MedWiki, etc.), model merging, and clinical alignment. To cover most clinical tasks, we extended the CLUE benchmark to CLUE+, doubling its size. Our expert models deliver relative improvements on this benchmark over the base model without any task-specific fine-tuning: 64.3% on medical entities, 49.5% on radiology reports, and 44% on ICD-10 coding (outperforming GPT-4-0125 by 14%). We unify the expert models into MediPhi via model merging, preserving gains across benchmarks. Furthermore, we built the MediFlow collection, a synthetic dataset of 2.5 million high-quality instructions on 14 medical NLP tasks, 98 fine-grained document types, and JSON format support. Alignment of MediPhi using supervised fine-tuning and direct preference optimization achieves further gains of 18.9% on average.

## Speaker Bio

Jean-Philippe Corbeil is a Senior Research Scientist at Microsoft Health & Life Sciences, where he focuses on leveraging language models to improve the working conditions of healthcare providers. Prior to joining Microsoft, he held a similar role at Nuance Communications (2022–2023), specializing in enterprise natural language understanding. From 2021 to 2022, he played a key role in building Bell Canada's NLP team as a Senior NLP Specialist. Jean-Philippe holds a background in Physics Engineering (Mathematics Option) from Polytechnique Montréal.

## Logistics

Date: April 11th<br>
Time: 1PM <br>
Location: A14 or Zoom (See email)
