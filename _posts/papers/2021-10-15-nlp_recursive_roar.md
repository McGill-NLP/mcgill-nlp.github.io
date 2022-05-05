---
title: "Evaluating the Faithfulness of Importance Measures in NLP by Recursively Masking Allegedly Important Tokens and Retraining" # Add official title
author: Andreas Madsen # Add name to show profile in sidebar
categories: Publications # Used to list all posts about publications in /publications/
names: "Andreas Madsen, Nicholas Meade, Vaibhav Adlakha, Siva Reddy" # names of all authors
link: https://arxiv.org/abs/2110.08412 # link to paper
code: https://github.com/AndreasMadsen/nlp-roar-interpretability # link to code (optional)
twitter: https://twitter.com/andreas_madsen/status/1450832033282932741  # link to twitter thread (optional)
thumbnail: /assets/images/papers/2021-nlp-recursive-roar.svg  # link to a thumbnail (optional)
venue: ArXiv pre-print  # venue and year of the paper
tags: pre-print # tag of the paper (exclude year, use shorthand)
---

*{{ page.names }}*

**{{ page.venue }}**

{% include display-publication-links.html pub=page %}

## Abstract

To explain NLP models, many methods inform which inputs tokens are important for a prediction. However, an open question is if these methods accurately reflect the model's logic, a property often called faithfulness. In this work, we adapt and improve a recently proposed faithfulness benchmark from computer vision called ROAR (RemOve And Retrain), by Hooker et al. (2019).
We improve ROAR by recursively removing dataset redundancies, which otherwise interfere with ROAR. We adapt and apply ROAR, to popular NLP importance measures, namely attention, gradient, and integrated gradients. Additionally, we use mutual information as an additional baseline. Evaluation is done on a suite of classification tasks often used in the faithfulness of attention literature. Finally, we propose a scalar faithfulness metric, which makes it easy to compare results across papers.
We find that, importance measures considered to be unfaithful for computer vision tasks perform favorably for NLP tasks, the faithfulness of an importance measure is task-dependent, and the computational overhead of integrated gradient is rarely justified.
