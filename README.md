# Vietnamese Medical Q&A System with RAG and Fine-tuned LLM

## 🏥 Project Overview

Xây dựng hệ thống hỏi đáp tiếng Việt trong domain **Y tế phổ thông**, kết hợp:
- 📚 **RAG (Retrieval-Augmented Generation)**: Vector store + semantic search
- 🤖 **Fine-tuned LLM**: Llama 2 với LoRA trên Colab Free
- 📊 **Evaluation**: BLEU, ROUGE-L, BERTScore, Human Eval

## 📋 Requirements

### Phase 1: Data Collection ✅
- ≥ 300 QA pairs cho fine-tuning (thủ công)
- ≥ 50 QA pairs test set (golden standard)
- Tài liệu y tế từ các nguồn uy tín

### Phase 2: Fine-tuning 🔄
- LLM: Llama 2 (7B or 13B)
- Method: LoRA/QLoRA
- Platform: Google Colab Free

### Phase 3: RAG Pipeline 🚀
- Chunking + Embedding
- Vector Store: Chroma hoặc FAISS
- Retriever: Top-K semantic search

### Phase 4: Experiments 📈
So sánh 4 cấu hình:
```
                Không RAG    Có RAG
LLM gốc            A            B
Fine-tuned         C            D
```

### Phase 5: Evaluation 📋
- Định lượng: BLEU, ROUGE-L, BERTScore
- Retrieval: Recall@5
- Human eval: 50 câu

### Phase 6: Demo 🎨
- Streamlit app
- Giao diện thân thiện

## 📁 Project Structure

```
.
├── README.md
├── requirements.txt
├── config/
│   └── config.yaml
├── data/
│   ├── raw/
│   │   ├── documents/
│   │   └── sources.md
│   ├── processed/
│   └── embeddings/
├── src/
│   ├── data_preparation/
│   ├── rag/
│   ├── evaluation/
│   └── utils/
├── experiments/
├── notebooks/
├── demo/
└── docs/
```

## 🚀 Quick Start

### 1. Setup Environment
```bash
git clone https://github.com/dibawng-ui/vietnamese-medical-qa-rag.git
cd vietnamese-medical-qa-rag
pip install -r requirements.txt
```

### 2. Data Collection
- Đọc: `docs/data_collection.md`
- Tạo QA pairs và lưu vào `data/processed/`

### 3. Fine-tuning (Colab)
- Mở notebook: `notebooks/01_finetuning_llama2_colab.ipynb`
- Chạy trên Google Colab Free

### 4. RAG Pipeline
```bash
python src/rag/build_vector_store.py
python src/rag/rag_pipeline.py
```

### 5. Run Experiments
```bash
python experiments/run_all_configs.py
```

### 6. Demo
```bash
streamlit run demo/app.py
```

## 📚 Documentation

- [Setup Guide](docs/setup_guide.md) - Hướng dẫn setup chi tiết
- [Data Collection](docs/data_collection.md) - Thu thập & tạo QA pairs
- [Experiment Guide](docs/experiment_guide.md) - Chạy experiments
- [Evaluation Guide](docs/evaluation_guide.md) - Đánh giá kết quả

## 🏃 Timeline

| Phase | Timeline | Status |
|-------|----------|--------|
| Data Collection | Week 1-2 | ⏳ TODO |
| Fine-tuning | Week 2-3 | ⏳ TODO |
| RAG Pipeline | Week 3 | ⏳ TODO |
| Experiments | Week 4 | ⏳ TODO |
| Evaluation | Week 4-5 | ⏳ TODO |
| Demo | Week 5 | ⏳ TODO |

## 👤 Author

dibaung-ui

## 📝 License

MIT License
