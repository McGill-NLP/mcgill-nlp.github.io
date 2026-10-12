---
category: information-integrity
paper_date: 2026-08-09  # date of the most recent paper; entries are listed newest first
pip: credigraph
links:
  - label: Domain query API docs
    url: https://credinet.readthedocs.io/en/latest/
    type: docs
  - label: Dataset
    url: https://huggingface.co/datasets/ComplexDataLab/CrediBench
    type: dataset
  - label: Paper (KDD 2026)
    url: https://dl.acm.org/doi/10.1145/3770855.3817476
    type: paper
---

## [CrediBench](https://dl.acm.org/doi/10.1145/3770855.3817476)

<div class="clearfix" markdown="1">
[![image-left](/assets/images/tech_transfer/credibench.webp){: .align-left}](https://dl.acm.org/doi/10.1145/3770855.3817476)

The CrediBench dataset is a temporal benchmark that consists of monthly webgraph snapshots built from Common Crawl, where each node is a web domain with its textual page content. Each monthly snapshot contains dozens of millions of domains and over a billion edges (hyperlink relations between them). The optimized graph construction pipeline is open-sourced. Trained on this data, we make available the reliability predictions by our graph- and text-based model. We also released a new large-scale set of labelled data spanning web categories.
</div>
