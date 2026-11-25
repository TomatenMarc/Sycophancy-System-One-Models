# Sycophancy in System-One Decision Models<br>"Should the model change its decision simply because the user is confident?"

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

### Trivia Question Anwering

![Total Accuracy Across Input Variations](./results/plots/trivia_qa.png)

### Truthful Question Anwering

![Accuracy Delta vs. Neutral Baseline by Model and Prompt Variation](./results/plots/truthful_qa.png)

### Trivia Question Anwering (I am really sure - Ablation)

![Total Accuracy Across Input Variations (Ablation)](./results/plots/trivia_qa_ablation.png)

### Truthful Question Anwering (I am really sure - Ablation)

![Accuracy Delta vs. Neutral Baseline by Model and Prompt Variation (Ablation)](./results/plots/truthful_qa_ablation.png)
