---
title: "From Summarization Evaluation to Digital Agents"
venue: McGill NLP
names: Ori Ernst and Xing Han Lù
author: Ehud Reiter
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

The [NLP Reading Group]({% link _pages/reading-group.md %}) is excited to host our very own Ori Ernst and Xing Han Lù both from the McGill NLP group. They will each be giving 30 minute presentations on summarization evaluation and digital agents respectively, leaving time for questions and discussion. Here are more details on each of the talks.

## What is the "best" way to measure summaries? Not what you think.

**Talk description:** The common practice for assessing automatic evaluation metrics is to measure the correlation between their induced system rankings and those obtained by reliable human evaluation, where a higher correlation indicates a better metric. In this talk, I will challenge the soundness of this methodology when multiple Quality Criteria (QCs) are involved, concretely for the summarization case. First, I will show that the allegedly best metrics for certain QCs actually do not perform well, failing to detect even drastic summary corruptions with respect to the considered QC. To explain this, I will show that some of the high correlations obtained in the multi-QC setup are spurious. Finally, I will propose a procedure that may help detecting this effect. Overall, these findings highlight the need for further investigating metric evaluation methodologies for the multiple-QC case.

**Speaker bio:** Ori is a postdoctoral researcher and an IVADO fellow at McGill University and Mila AI institute under the guidance of Prof. Jackie Cheung. He earned his Ph.D at the Natural Language Processing Lab at Bar-Ilan University, under the supervision of Prof. Ido Dagan and Prof. Jacob Goldberger. His research focuses on multi-document summarization and text generation. In addition, Ori served in several research-oriented industrial positions, including Amazon, IBM and Intel.

## WebLINX: Real-World Website Navigation with Multi-Turn Dialogue

**Talk description:** We propose the problem of conversational web navigation, where a digital agent controls a web browser and follows user instructions to solve real-world tasks in a multi-turn dialogue fashion. To support this problem, we introduce WEBLINX - a large-scale benchmark of 100K interactions across 2300 expert demonstrations of conversational web navigation. Our benchmark covers a broad range of patterns on over 150 real-world websites and can be used to train and evaluate agents in diverse scenarios. Due to the magnitude of information present, Large Language Models (LLMs) cannot process entire web pages in real-time. To solve this bottleneck, we design a retrieval-inspired model that efficiently prunes HTML pages by ranking relevant elements. We use the selected elements, along with screenshots and action history, to assess a variety of models for their ability to replicate human behavior when navigating the web. Our experiments span from small text-only to proprietary multimodal LLMs. We find that smaller finetuned decoders surpass the best zero-shot LLMs (including GPT-4V), but also larger finetuned multimodal models which were explicitly pretrained on screenshots. However, all finetuned models struggle to generalize to unseen websites. Our findings highlight the need for large multimodal models that can generalize to novel settings. Our code, data and models are available for research: this https URL

**Speaker bio:** Xing Han is a PhD student at McGill University and Mila, where he works on conversational web navigation under the supervision of Dr. Siva Reddy. During his studies, he has visited ServiceNow Research, where he has worked with Dr. Harm de Vries on conversational table retrieval. Previously, he lead various ML initiatives and developed open-source libraries at Plotly, worked on summarization engines at Deloitte, and researched ML for taxation policy at the McGill Clinical and Health Informatics lab.

## Logistics

Date: May 6th <br>
Time: 11:00AM <br>
Location: F01 or via Zoom (See email)