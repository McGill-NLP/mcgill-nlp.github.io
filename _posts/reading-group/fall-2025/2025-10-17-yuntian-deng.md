---
title: "Implicit Chain-of-Thought: Internalizing Reasoning in Language Models"
venue: University of Waterloo
names: Yuntian Deng
author: Yuntian Deng
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

The [NLP Reading Group]({% link _pages/reading-group.md %}) is delighted to host [Prof. Yuntian Deng](https://yuntiandeng.com/) who will be giving a talk **remotely** on "Implicit Chain-of-Thought: Internalizing Reasoning in Language Models".


## Recording

<iframe width="560" height="315" src="https://youtu.be/F6e5MztlFhQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Talk Description
When leveraging language models for reasoning tasks, generating explicit chain-of-thought (CoT) steps is often crucial for high accuracy. In this work, drawing inspiration from how the human brain transitions from explicit, conscious, deliberate reasoning (System 2) to implicit, automatic, intuitive thinking (System 1), we seek to internalize explicit CoT reasoning within a model that directly produces the final answer, which we define as the implicit CoT paradigm.
 
To realize implicit CoT, we found a simple yet effective method: starting with a model trained for explicit CoT reasoning, we gradually remove the intermediate steps and finetune the model. This approach enables a finetuned GPT-2 Small model to solve 20-by-20 multiplication with up to 99.5% accuracy, whereas standard training cannot solve beyond 4-by-4 multiplication.
 
You can try our demo at https://huggingface.co/spaces/yuntian-deng/gpt2-multiplication

## Speaker Bio

Yuntian Deng is an assistant professor at the University of Waterloo and a visiting professor at NVIDIA under Prof. Yejin Choi. He was previously a postdoc at AI2, also advised by Prof. Choi. He received his PhD from Harvard University under Prof. Alexander Rush and Prof. Stuart Shieber. His recent works include NeuralOS, Interactive Training, WildChat, and Implicit Chain-of-Thought.

## Logistics

Date: October 17th<br>
Time: 2:00PM <br>
Location: H04 or via Google Meet (See email)
