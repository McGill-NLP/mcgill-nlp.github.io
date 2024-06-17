---
title: "Inductive Biases and Concept-based Explainability"
venue: University of Edinburgh and Technological Research Institute (IRT) Saint Exupéry
names: Matthias Lindermann and Fanny Jourdan
author: Matthias Lindermann and Fanny Jourdn
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



The [NLP Reading Group]({% link _pages/reading-group.md %}) is happy to host two consecutive talks on Monday, June 10th at 11AM EST in Auditorium 1.

- 11AM EST: 
[Matthias Lindermann](https://namednil.github.io/), a PhD student at the University of Edinburgh will be speaking remotely on "Structural Inductive Biases for Better Systematic Generalization with Sequence-to-Sequence Models".

- 12PM EST:
Pizza lunch!

- 12:30PM EST:
[Fanny Jourdan](https://fanny-jourdan.github.io/),  a researcher at Technological Research Institute (IRT) Saint Exupéry, France, will be speaking in person on " Unsupervised concepts based XAI for Natural Language Processing".

## Structural Inductive Biases for Better Systematic Generalization with Sequence-to-Sequence Models

**Talk description:** Sequence-to-sequence models have been hugely popular in NLP and have been applied to tasks ranging from grapheme-to-phoneme conversion to semantic parsing. However, even with pre-training, standard sequence-to-sequence models often lack structural inductive biases to generalize systematically outside of the distribution they are trained/fine-tuned on. For example, they have been shown to struggle with longer inputs or unseen combinations of seen tokens/phrases. In this talk, I'm going to present two approaches to introducing stronger structural inductive biases that help with systematic generalization.

In the first half of the talk, I focus on semantic parsing and propose a neural architecture that decomposes the seq2seq problem into predicting small fragments of the output and then permuting them into the correct order. One of the technical challenges I address is training the model without supervision for what the fragments are. Despite not having an explicit notion of (syntax) trees, this approach performs well on generalization to deeper recursion than seen during training.

In the second half, I focus on the inductive bias of Finite State Transducers (FSTs), which have been used traditionally in areas such as phonology and morphology. Given a representation of an automatically generated FST and an input string, I propose to pre-train a Transformer to predict the output of the FST on the given input. The experiments show that this leads to a better inductive bias for downstream FST-like tasks. Empirically, the pre-training also makes the model simulate transitions between FST states in its hidden representations - without the model being explicitly trained to do so.


**Speaker bio:** Matthias is a fourth-year PhD student at the University of Edinburgh working with Ivan Titov and Alexander Koller. His work focuses on inductive biases for structural generalization and won an Outstanding Paper award at ACL 2023. Before starting his PhD, Matthias completed a Bachelor’s and Master’s in Computational Linguistics at Saarland University.

## Unsupervised concepts based XAI for Natural Language Processing

**Talk description:** Concept-based explainability in Natural Language Processing (NLP) addresses the challenges of transparency and fairness in complex machine learning models. By focusing on the latent representations of concepts within text encoders, researchers aim to bridge the gap between model decisions and human-understandable concepts. This approach not only enhances trust in NLP systems but also facilitates the detection and mitigation of biases, promoting fairer and more ethical AI. By manipulating these latent representations, concept-based explainability provides a more nuanced and actionable understanding of model behavior, crucial for advancing responsible AI practices.

 

The presentation will be in 3 parts:

A method to do unsupervised concept based XAI for NLP: COCKATIEL [1]
Used unsupervised concept based XAI to do Fairness: TaCo [2]
A framework to evaluate unsupervised concept based XAI for NLP [Future Work]
[1] Fanny Jourdan, Agustin Picard, Thomas Fel, Laurent Risser, Jean-Michel Loubes, Nicholas Asher, "COCKATIEL: COntinuous Concept ranKed ATtribution with Interpretable ELements for explaining neural net classifiers on NLP tasks" the Findings of the Association for Computational Linguistics (ACL 2023).

[2] Fanny Jourdan, Louis Bethune, Agustin Picard, Laurent Risser, Nicholas Asher, "TaCo: Targeted Concept Removal in Output Embeddings for NLP via Information Theory and Explainability" under the review.

**Speaker bio:** Fanny Jourdan is a researcher at Technological Research Institute (IRT) Saint Exupéry at Toulouse, France. She is finishing her PhD at Artificial and Natural Intelligence Toulouse Institute (ANITI) on Fairness and Explainability (XAI) for Natural Language Processing (NLP) under the supervision of Nicholas Asher.She will be at MILA from June 3 to 12, and will give a presentation on June 10 at 12:30PM. Fanny will present her research on concept-based explicability methods, then introduce a future research project between France and Quebec on reliable LLMs (to find partners within MILA).

## Logistics

Date: June 10th <br>
Time: 11:00AM <br>
Location: Auditorium 1 or via Zoom (See email)
