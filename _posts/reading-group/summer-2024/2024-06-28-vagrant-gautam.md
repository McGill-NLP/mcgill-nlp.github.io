---
title: "Are LLMs Reasoning, Repeating or Just Biased? A Case Study with English Pronouns"
venue: Saarland University
names: Vagrant Gautam
author: Vagrant Gautam
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

The [NLP Reading Group]({% link _pages/reading-group.md %}) is happy to have [Vagrant Gautam](https://dippedrusk.com/) who will be giving a talk about "Are LLMs Reasoning, Repeating or Just Biased? A Case Study with English Pronouns".

## Talk Description

Using pronouns as a testbed to disentangle reasoning, repetition and bias in large language models, my most recent work introduces the task of pronoun fidelity: given a context introducing a co-referring entity and pronoun, the task is to reuse the correct pronoun later, independent of potential distractor sentences discussing other people. This allows us to simultaneously measure two important downstream goals for LLMs: robust, faithful and harm-free pronoun use for individuals, as well as robust reasoning about pronouns and coreference. We introduce RUFF, a dataset with a simple yet naturalistic version of the task, where humans achieve nearly 100% accuracy. Our behavioural analysis of 37 large language models across architectures (encoder-only, decoder-only and encoder-decoder), and scales (11M-70B parameters) reveals that models perform well with no distractors, but poorly with distractors, indicating overall that models are not "reasoning" at all. Additionally, we see interesting differences across architectures, with encoder-only models making increasingly more bias errors, and decoder-only models making increasingly more distraction errors. The gaps we show raise concerns about how we evaluate (and talk about) model reasoning, and has implications for misgendering people.

## Speaker Bio

Mx. Vagrant Gautam (xe/they) is a computer scientist, linguist and birder. They are currently a computer science PhD candidate at Saarland University, where they work on measuring and improving the robustness of natural language processing (NLP) systems. Before this, they worked on speech recognition at Dialpad, and on discourse processing and experimental phonology at Simon Fraser University. Their current research focuses on question answering and fairness, and they are interested in both the social and technical aspects of NLP.

## Logistics

Date: June 28th <br>
Time: 10:30 AM <br>
Location: F01 or via Zoom (See email)

