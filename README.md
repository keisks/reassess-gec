# Reassessing the Goals of Grammatical Error Correction

Data and scripts used in 2016 TACL paper, "Reassessing the Goals of Grammatical Error Correction: Fluency Instead of Grammaticality"

- Keisuke Sakaguchi
- Courtney Napoles
- Matt Post
- Joel Tetreault

Last updated: May 2nd, 2016

- - -

This repository contains data and scripts in the following paper:

    @article{TACL800,
            author = {Sakaguchi, Keisuke  and Napoles, Courtney  and Post, Matt
    and Tetreault, Joel },
            title = {Reassessing the Goals of Grammatical Error Correction:
    Fluency Instead of Grammaticality},
            journal = {Transactions of the Association for Computational
    Linguistics},
            volume = {4},
            year = {2016},
            keywords = {},
            abstract = {The field of grammatical error correction (GEC) has
    grown substantially in recent years, with research directed at both
    evaluation metrics and improved system performance against those metrics.
    One unvisited assumption, however, is the reliance of GEC evaluation on
    error-coded corpora, which contain specific labeled corrections. We examine
    current practices and show that GEC’s reliance on such corpora unnaturally
    constrains annotation and automatic evaluation, resulting in (a) sentences
    that do not sound acceptable to native speakers and (b) system rankings that
    do not correlate with human judgments. In light of this, we propose an
    alternate approach that jettisons costly error coding in favor of
    unannotated, whole-sentence rewrites. We compare the performance of existing
    metrics over different gold-standard annotations, and show that automatic
    evaluation with our new annotation scheme has very strong correlation with
    expert rankings (ρ = 0.82). As a result, we advocate for a fundamental and
    necessary shift in the goal of GEC, from correcting small, labeled error
    types, to producing text that has native fluency.},
            issn = {2307-387X},
            url =
    {https://tacl2013.cs.columbia.edu/ojs/index.php/tacl/article/view/800},
            pages = {169--182}
    }


## Data

    .
    ├── README.md  # this file
    ├── annotations # fluency and minimal edits by experts and non-experts
    ├── inter_annotator_agreements # human judgments
    ├── metric_scores # system-level scores by all metric-reference pairs
    └── trueskill_rankings # scripts for get the ranking by human


## Questions
 - Please e-mail to Keisuke Sakaguchi (keisuke[at]cs.jhu.edu) and Courtney Napoles (courtneyn[at]jhu.edu).
