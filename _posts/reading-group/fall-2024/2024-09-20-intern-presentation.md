---
title: "Intern Presentations"
venue: McGill + Mila
names: Fabian David Schmidt, Ada Tur, Steven Koniaev, Nathan Zeweniuk
author: Fabian David Schmidt, Ada Tur, Steven Koniaev, Nathan Zeweniuk
tags:
- NLP RG
categories:
    - Reading-Group
    - Fall-2024
layout: archive
classes:
    - wide
    - no-sidebar
---

*{{ page.names }}*

**{{ page.venue }}**

{% include display-publication-links.html pub=page %}

The [NLP Reading Group]({% link _pages/reading-group.md %}) is thrilled to showcase the work of our McGill NLP interns who will each be giving 10 minute talks (5 minutes of QA) to the group. The speakers will be [Fabian David Schmidt](https://fdschmidt93.github.io/), [Ada Tur](https://adadtur.github.io/), [Steven Koniaev](https://steven-koniaev.vercel.app/) and [Nathan Zeweniuk](https://mila.quebec/en/directory/nathan-zeweniuk).

More information about each talk below.

# Fabian David Schmidt

## Talk Description

LLMs have become a go-to solution not just for text generation, but also for natural language understanding (NLU) tasks. Acquiring extensive knowledge through language modeling on web-scale corpora, they excel on English NLU, yet struggle to extend their NLU capabilities to underrepresented languages. In contrast, machine translation models (MT) produce excellent multilingual representations, resulting in strong translation performance even for low-resource languages. MT encoders, however, lack the knowledge necessary for comprehensive NLU that LLMs obtain through language modeling training on immense corpora. In this work, we get the best both worlds by integrating MT encoders directly into LLM backbones via sample-efficient self-distillation. The resulting MT-LLMs preserve the inherent multilingual representational alignment from the MT encoder, allowing lower-resource languages to tap into the rich knowledge embedded in English-centric LLMs for successful cross-linugal transfer at scale. We further sketch how MT decoders and generative LLMs may be interleaved to enable high-quality natural language generation for underrepresented languages.

## Bio

Fabian David Schmidt is a fourth year PhD student at University of Würzburg. He is broadly interested in building multilingual NLP systems that robustly scale to lower-resource languages. He is currently doing a research internship on massively multilingual causal language models with David Adelani.

# Ada Tur: Constituent Movement with Large Language Models

## Talk Description

Though English sentences are typically flexible vis-a-vis word order, post-verbal constituents often show far more variability in ordering. One prominent theory presents the notion that constituent ordering is directly correlated with constituent weight: a measure of the constituent's length or complexity. Such theories are interesting in the context of natural language processing (NLP), because while recent advances in natural language processing (NLP) have led to significant gains in the performance of large language models (LLMs), much remains unclear about how these models process language, and how this compares to human language processing. In particular, the question of if LLMs display the same patterns with post-verbal constituent shifting remains, and may provide insights into existing theories on when and how the shift occurs in human language.

## Bio

Ada Tur is a third year Computer Science and Linguistics student at McGill University in Montreal, QC, and an undergraduate researcher at McGill University/MILA in Professor Siva Reddy's NLP lab.

# Steven Koniaev

## Talk Description

The vast volume of text generated in recent years has resulted in a growing demand for effective summarization methods. Consequently, various approaches have been introduced for this purpose, achieving commendable evaluation scores. However, despite the success of these models in summarizing most texts, they still exhibit lower scores for certain cases.  his observation leads to the hypothesis that some texts pose greater challenges for summarization. In this project, our aim is to develop a model that takes a document as input and predicts its summarization difficulty accurately. By utilizing this model and analyze its results, we can understand in which cases the text becomes more challenging to summarize, and apply this to certain NLP tasks such as Multidocument Summarization. 

## Bio

Steven is a current undergraduate researcher at McGill University under Prof. Jackie Cheung working alongside Ori Ernst.

# Nathan Zeweniuk

## Talk Description

Summarization has become an important part of making large amounts of information more accessible to readers. Summarization methods are commonly described as either 'extractive', where salient text is copied directly from the source, or 'abstractive', where the source information can be reworded or altered. Previous attempts to describe a level of abstractiveness have been based on simple lexical measures, such as novel n-grams, which can fail to capture important semantic differences between sources and summaries. In this project, we analyze the levels of abstractiveness in human written summaries based on differences of information between the source and summary. Using this analysis, we are able to show that summarization systems struggle to generate reference summary content with the same level of abstractiveness.

## Bio

Nathan recently graduated from McGill University where he worked on research with Ori Ernst under Prof. Jackie Cheung. He is currently pursuing a master's degree at the University of Alberta.

# Logistics

Date: September 20th<br>
Time: 11:30AM <br>
Location: Auditorium 2 or via Zoom (See email)
