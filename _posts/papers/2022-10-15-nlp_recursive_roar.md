---
title: "Evaluating the Faithfulness of Importance Measures in NLP by Recursively Masking Allegedly Important Tokens and Retraining" # Add official title
author: Andreas Madsen # Add name to show profile in sidebar
categories: Publications # Used to list all posts about publications in /publications/
names: "Andreas Madsen, Nicholas Meade, Vaibhav Adlakha, Siva Reddy" # names of all authors
link: https://arxiv.org/abs/2110.08412 # link to paper
code: https://github.com/AndreasMadsen/nlp-roar-interpretability # link to code (optional)
twitter: https://twitter.com/andreas_madsen/status/1450832033282932741  # link to twitter thread (optional)
thumbnail: /assets/images/papers/2021-nlp-recursive-roar.svg  # link to a thumbnail (optional)
venue: EMNLP Findings # venue and year of the paper
tags: EMNLP # tag of the paper (exclude year, use shorthand)layout: paper
---

*{{ page.names }}*

**{{ page.venue }}**

{% include display-publication-links.html pub=page %}

## Abstract

To explain NLP models a popular approach is to use importance measures, such as attention, which inform input tokens are important for making a prediction. However, an open question is how well these explanations accurately reflect a model's logic, a property called faithfulness.

To answer this question, we propose Recursive ROAR, a new faithfulness metric. This works by recursively masking allegedly important tokens and then retraining the model. The principle is that this should result in worse model performance compared to masking random tokens. The result is a performance curve given a masking-ratio. Furthermore, we propose a summarizing metric using relative area-between-curves (RACU), which allows for easy comparison across papers, models, and tasks.

We evaluate 4 different importance measures on 8 different datasets, using both LSTM-attention models and RoBERTa models. We find that the faithfulness of importance measures is both model-dependent and task-dependent. This conclusion contradicts previous evaluations in both computer vision and faithfulness of attention literature.
