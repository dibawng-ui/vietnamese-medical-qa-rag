# Experiment Guide

## Overview

So sánh 4 cấu hình LLM:

```
                Không RAG    Có RAG
LLM gốc            A            B
Fine-tuned         C            D
```

## Setup Experiments

### Configuration A: Base LLM, No RAG

- **Model**: Llama 2 base (không fine-tune)
- **RAG**: Không sử dụng
- **Inference**: Direct generation

### Configuration B: Base LLM, With RAG

- **Model**: Llama 2 base
- **RAG**: Có retrieval
- **Inference**: Retrieval + generation

### Configuration C: Fine-tuned LLM, No RAG

- **Model**: Llama 2 fine-tuned với LoRA
- **RAG**: Không sử dụng
- **Inference**: Direct generation

### Configuration D: Fine-tuned LLM, With RAG

- **Model**: Llama 2 fine-tuned với LoRA
- **RAG**: Có retrieval
- **Inference**: Retrieval + generation

## Running Experiments

See: `notebooks/02_experiments.ipynb`

## Evaluation

See: `docs/evaluation_guide.md`
