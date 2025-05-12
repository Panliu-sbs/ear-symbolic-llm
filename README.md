# Algebraic vs. LLM-Based Reasoning Dataset

This repository contains the benchmark dataset and evaluation results for the paper:

**Algebraic Knowledge Graph Reasoning for Interpretable LLM Inference**  
*Pan Liu¹, Yihao Li²*  
¹Shanghai Business School, ²Ludong University

---

## 📘 Overview

This dataset supports comparative evaluation of symbolic–neural reasoning with large language models (LLMs). It includes structured algebraic inputs derived from knowledge graphs (EAR model), standard LLM prompts, CoT-style prompts, and corresponding ground-truth answers. The evaluation covers 310 tasks spanning four major reasoning types.

---

## 📂 Repository Structure

```
📁 /data
│
├── Generated_EAR_vs_LLM_Prompts.xlsx     # Full benchmark (EAR, standard LLM, CoT inputs)
├── type.xlsx                             # Reasoning type annotation per task (A/B/C/D/mixed)
├── Experimental Result.xlsx              # Raw accuracy, faithfulness, constraint satisfaction
├── Result analysis.xlsx                  # Aggregated and per-type evaluation summary
```

---

## 🧠 Reasoning Types

| Type  | Description                                 | Count |
|-------|---------------------------------------------|--------|
| A     | Structural reasoning (hierarchy, inclusion) | 123    |
| B     | Constraint-based algebraic reasoning        | 140    |
| C     | Multimodal abstraction (charts/tables)      | 44     |
| D     | Ambiguity resolution and coreference        | 49     |
| A+B+  | Composite (multi-type) tasks                | 46     |
|       | **Total**                                   | **310**|

---

## 🧪 Experimental Setup

- **Models Used**: GPT-4o (May 2024)
- **Input Formats**:  
  - EAR + Algebraic Expression Input  
  - Standard LLM Prompt  
  - CoT Prompt ("Please step by step")
- **Evaluation Metrics**:
  - Answer Accuracy  
  - Trace Faithfulness  
  - Constraint Satisfaction Rate  
  - User Interpretability Rating

---

## 📊 Files Description

| File Name                         | Description |
|----------------------------------|-------------|
| `Generated_EAR_vs_LLM_Prompts.xlsx` | Each row contains EAR–Algebraic input, plain LLM input, CoT input, and ground truth. Sheet0–32 are organized by task batch. |
| `type.xlsx`                      | Reasoning type annotations per task (Sheet1). |
| `Experimental Result.xlsx`       | Per-task scores for accuracy, faithfulness, constraint compliance, and interpretability. |
| `Result analysis.xlsx`           | Aggregated results, comparisons by type (A/B/C/D), and visualization references. |

---

## 📎 Citation

If you use this dataset in your work, please cite:

```bibtex
@article{liu2025algebraic,
  title={Algebraic Knowledge Graph Reasoning for Interpretable LLM Inference},
  author={Pan Liu and Yihao Li},
  journal={To appear},
  year={2025}
}
```

---

## 📬 Contact

For questions or collaboration, please contact:

- Pan Liu – panl008@163.com  
- Yihao Li – yihao.li@ldu.edu.cn
