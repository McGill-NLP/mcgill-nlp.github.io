---
title: Benchmark
layout: splash
category: temporal-graph-learning
order: 1
header:
    overlay_filter: linear-gradient(rgba(0, 0, 0, 0.3), rgba(0, 0, 0, 0.5))
    overlay_image: /assets/images/research_directions/temporal-graph-learning/TGB.jpg
    overlay_size: contain
one-liner: How to realistically, reproducibly, and robustly evaluate machine learning models on temporal graphs?
excerpt: ""
parent: Temporal Graph Learning

---

{% include breadcrumbs.html %}


The Temporal Graph Benchmark (TGB) is a comprehensive collection of datasets designed for the realistic, reproducible, and robust evaluation of machine learning models on temporal graphs. These datasets are large-scale, span multiple years, and cover various domains such as social networks, trade networks, transaction networks, and transportation networks. They include both node and edge-level prediction tasks, providing a diverse set of challenges for researchers.

The follow-up work TGB 2.0 is a new benchmarking framework designed to evaluate methods for predicting future links on Temporal Knowledge Graphs (TKGs) and Temporal Heterogeneous Graphs (THGs). This framework extends the original Temporal Graph Benchmark by focusing on large-scale datasets, which are significantly larger than existing datasets in terms of nodes, edges, or timestamps. 

TGB offers an automated machine learning pipeline that facilitates reproducible and accessible research. This pipeline includes tools for data loading, experiment setup, and performance evaluation. The benchmark is regularly maintained and updated, and it welcomes feedback from the community to ensure its continued relevance and improvement.

Temporal Graph Benchmark Website [link](https://tgb.complexdatalab.com/)


# Selected Publications

{% include posts-highlighted-publications.html taxonomy="TGB" %}