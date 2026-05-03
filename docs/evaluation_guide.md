# Evaluation Guide

## Metrics

### 1. Định lượng Metrics

#### BLEU Score
- Đo sự giống nhau giữa output và reference
- Range: 0-1 (cao hơn tốt hơn)
- Tính toán: Dựa trên n-gram overlap

#### ROUGE-L Score
- Longest Common Subsequence
- Range: 0-1 (cao hơn tốt hơn)
- Phù hợp cho summarization & QA

#### BERTScore
- Dựa trên semantic similarity
- Sử dụng BERT embeddings
- Range: 0-1 (cao hơn tốt hơn)

### 2. Retrieval Metrics

#### Recall@5
- Tỉ lệ câu hỏi có gold document trong top-5 retrieved
- Range: 0-1 (cao hơn tốt hơn)

### 3. Human Evaluation

Một người đánh giá 50 câu hỏi dựa trên:
- Accuracy: Câu trả lời có đúng không?
- Relevance: Câu trả lời liên quan đến câu hỏi không?
- Fluency: Câu trả lời có tự nhiên không?

Thang điểm: 1-5

## Running Evaluation

See: `notebooks/03_evaluation.ipynb`
