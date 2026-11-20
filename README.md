# Sycophancy in System-One Decision Models

This repository benchmarks whether small, fast **System-One-Decision-Models** are sycophantic. A System-One-style model is expected to produce a quick, direct answer instead of deliberately revising it. This project applies that setting to a basic and measurable sycophancy test: does a model keep a stated answer when a user pushes it to agree, and does it change its answer when presented with an authority cue or user preference?

The work is motivated by [“Towards Understanding Sycophancy in Language Models”](https://proceedings.iclr.cc/paper_files/paper/2024/hash/0105f7972202c1d4fb817da9f21a9663-Abstract-Conference.html) (ICLR 2024). The [paper's evaluation repository](https://github.com/meg-tong/sycophancy-eval) contains several ways of measuring model behavior under social pressure.

## Why answer sycophancy?

**Answer sycophancy** measures whether a model changes a correct or previously selected answer because a user expresses doubt, disagreement, or a preference. It is an appropriate basic test for System-One models because it requires only a short decision followed by a single-user interaction: the model answers a question and then is asked whether it wants to revise that answer.

This does not prove general sycophancy. It isolates one easy-to-observe failure mode—agreement-seeking in answer choices—without requiring a model to produce long-form reasoning or moral judgments. The result is therefore useful as an initial check on whether a model values user agreement more than task correctness.

## Benchmark coverage

| Benchmark/test from the paper | Status in this repository | Short description |
|---|---|---|
| Answer sycophancy | **Implemented** | Asks a model to answer a question, then introduces user disagreement or preference and checks whether the answer changes. |
| Feedback sycophancy | Not yet implemented | Measures whether praise or criticism changes the model's assessment of its own output or subsequent behavior. |
| Mimicry / style matching | Not yet implemented | Checks whether a model reproduces a user's stated view or preferences. |
| Other paper evaluations | Not yet implemented | Additional settings from the paper have not yet been added here. |

## Implemented test

The repository currently implements the **answer benchmark**. It compares a model's initial answer with its response after follow-up pressure, for example when the user says that the answer is wrong or that a different answer is preferred. A change toward the user's preference is counted as potentially sycophantic; a model that preserves the correct answer is counted as resisting that pressure.

Exact prompts, datasets, and evaluation criteria are documented alongside the implementation in this repository.

## Answer Sycophancy

### Total Accuracy Across Input Variations
|                                                            |   Neutral |   Correct belief |   Correct rejection |   Incorrect belief |
|:-----------------------------------------------------------|----------:|-----------------:|--------------------:|-------------------:|
| ('cloudflare_clef', 'trivia_qa')                           |      97.7 |             97.7 |                94.9 |               97.7 |
| ('cloudflare_clef', 'truthful_qa')                         |      81.7 |             86.0 |                71.4 |               82.2 |
| ('cloudflare_clef-flash', 'trivia_qa')                     |      97.5 |             98.1 |                91.9 |               96.8 |
| ('cloudflare_clef-flash', 'truthful_qa')                   |      76.0 |             83.6 |                67.9 |               77.7 |
| ('jev-1.14', 'trivia_qa')                                  |      98.7 |             99.6 |                98.4 |               98.7 |
| ('jev-1.14', 'truthful_qa')                                |      89.2 |             94.6 |                82.1 |               85.2 |
| ('liquid_d1.2', 'trivia_qa')                               |      98.4 |             99.1 |                98.7 |               98.4 |
| ('liquid_d1.2', 'truthful_qa')                             |      81.4 |             85.2 |                79.2 |               79.3 |
| ('liquid_d1.2-ultra', 'trivia_qa')                         |      98.3 |             98.8 |                98.1 |               98.3 |
| ('liquid_d1.2-ultra', 'truthful_qa')                       |      79.8 |             87.0 |                74.9 |               75.5 |
| ('microsoft_microsoft-decision-1.1', 'trivia_qa')          |      98.8 |             98.6 |                98.7 |               98.7 |
| ('microsoft_microsoft-decision-1.1', 'truthful_qa')        |      87.1 |             85.9 |                85.0 |               87.5 |
| ('perplexity_pplx-decider-flash-v1.3:free', 'trivia_qa')   |      94.7 |             96.1 |                89.0 |               95.1 |
| ('perplexity_pplx-decider-flash-v1.3:free', 'truthful_qa') |      65.6 |             74.3 |                43.1 |               65.6 |
| ('perplexity_pplx-decider-v1.3:free', 'trivia_qa')         |      97.0 |             98.1 |                97.3 |               97.5 |
| ('perplexity_pplx-decider-v1.3:free', 'truthful_qa')       |      81.6 |             85.5 |                71.9 |               79.2 |

### Accuracy Delta vs. Neutral Baseline by Model and Prompt Variation
|                                                            |   Correct belief |   Correct rejection |   Incorrect belief |
|:-----------------------------------------------------------|-----------------:|--------------------:|-------------------:|
| ('cloudflare_clef', 'trivia_qa')                           |             +0.0 |                -2.7 |               +0.0 |
| ('cloudflare_clef', 'truthful_qa')                         |             +4.3 |               -10.3 |               +0.5 |
| ('cloudflare_clef-flash', 'trivia_qa')                     |             +0.6 |                -5.6 |               -0.7 |
| ('cloudflare_clef-flash', 'truthful_qa')                   |             +7.6 |                -8.1 |               +1.7 |
| ('jev-1.14', 'trivia_qa')                                  |             +0.9 |                -0.3 |               +0.0 |
| ('jev-1.14', 'truthful_qa')                                |             +5.4 |                -7.1 |               -4.0 |
| ('liquid_d1.2', 'trivia_qa')                               |             +0.7 |                +0.3 |               +0.0 |
| ('liquid_d1.2', 'truthful_qa')                             |             +3.8 |                -2.2 |               -2.1 |
| ('liquid_d1.2-ultra', 'trivia_qa')                         |             +0.6 |                -0.1 |               +0.0 |
| ('liquid_d1.2-ultra', 'truthful_qa')                       |             +7.2 |                -4.9 |               -4.3 |
| ('microsoft_microsoft-decision-1.1', 'trivia_qa')          |             -0.3 |                -0.1 |               -0.1 |
| ('microsoft_microsoft-decision-1.1', 'truthful_qa')        |             -1.2 |                -2.1 |               +0.4 |
| ('perplexity_pplx-decider-flash-v1.3:free', 'trivia_qa')   |             +1.4 |                -5.6 |               +0.4 |
| ('perplexity_pplx-decider-flash-v1.3:free', 'truthful_qa') |             +8.7 |               -22.4 |               +0.0 |
| ('perplexity_pplx-decider-v1.3:free', 'trivia_qa')         |             +1.2 |                +0.3 |               +0.6 |
| ('perplexity_pplx-decider-v1.3:free', 'truthful_qa')       |             +3.9 |                -9.7 |               -2.5 |