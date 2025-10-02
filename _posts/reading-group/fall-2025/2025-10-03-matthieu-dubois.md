---
title: "Towards Robust Detection of AI-generated Text: Sampling Pitfalls and Ensemble Resilience"
venue: Sorbonne Université
names: Matthieu Dubois
author: Matthieu Dubois
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

The [NLP Reading Group]({% link _pages/reading-group.md %}) is excited to receive [Matthieu Dubois](https://baggerofwords.github.io/) who will be giving a talk **in-person at Mila** on "Towards Robust Detection of AI-generated Text: Sampling Pitfalls and Ensemble Resilience".

## Talk Description

This presentation addresses two complementary lines of research on the challenges of detecting machine-generated text. First, it investigates how decoding strategies, such as temperature, top-k or nucleus sampling, impact detector performance. Through systematic experiments, it demonstrates that even subtle adjustments to a model's output distribution can cause AUROC scores to collapse from above 99 % to almost zero, shedding light on the inner workings of current detectors and revealing blind spots in recent benchmarks. Second, it introduces MOSAIC, an ensemble-based detection algorithm designed to overcome domain shifts and brittleness inherent in current unsupervised approaches. By combining multiple LLMs across diverse generator models, MOSAIC consistently achieves superior discrimination performance and robustness to distributional changes. Together, these studies chart a path toward more reliable, principled detection systems and underscore the urgent need for evaluation protocols that reflect the full spectrum of modern text-generation practices.

References: MOSAIC: Multiple Observers Spotting AI Content (ACL 2025) [https://arxiv.org/pdf/2409.07615](https://arxiv.org/pdf/2409.07615)

## Speaker Bio

Matthieu is a Doctoral Candidate at ISIR lab in Sorbonne University in Paris, supervised by Pablo Piantanida (ILLS, MILA) and François Yvon (ISIR). His thesis is about understanding and detecting content written by Large Language Models. Outside of the lab, he enjoys bouldering and reading. Favourite books are The Great Gatsby and L'étranger.
 
## Logistics

Date: October 3rd<br>
Time: 2:00PM <br>
Location: H04 or via Google Meet (See email)
