# Data Collection Guide

## Overview

Bạn cần tạo:
- ≥ 300 QA pairs cho **fine-tuning** LLM
- ≥ 50 QA pairs cho **test set** (golden standard)
- Tài liệu y tế từ các nguồn uy tín

## Step 1: Thu thập Tài liệu Y tế

### 1.1 Các nguồn đề xuất

| Nguồn | URL | Loại tài liệu |
|-------|-----|---------------|
| Bộ Y tế VN | https://moh.gov.vn/ | Chính thức |
| Wikipedia Y tế | https://vi.wikipedia.org/wiki/Y_h%E1%BB%8Dc | Tổng hợp |
| Tâm Lý Xã hội | Các bài viết về sức khỏe | Khoa học |
| Sách Y tế | Kiến thức y tế gia đình | Sách |

### 1.2 Quy trình thu thập

1. **Tìm tài liệu** từ các nguồn trên
2. **Copy nội dung** vào file `.txt`
3. **Đặt tên rõ ràng**: `benh_cum.txt`, `so_cap_cuu_phan_ung_soc.txt`
4. **Lưu vào**: `data/raw/documents/`

### 1.3 Tiêu chí tài liệu tốt

✅ **Tốt:**
- Rõ ràng, cụ thể
- Có cấu trúc (tiêu đề, phần con)
- Ngôn ngữ chuyên ngành nhưng dễ hiểu
- Có đủ thông tin chi tiết

❌ **Tệ:**
- Quá chung chung
- Ngôn ngữ phức tạp
- Thiếu thông tin
- Lỗi chính tả

### 1.4 Mục tiêu thu thập

**Tối thiểu:**
- 20 tài liệu
- ~100,000 từ (tổng cộng)
- Bao gồm các lĩnh vực: bệnh, điều trị, phòng chống, sơ cấp cứu

**Tối ưu:**
- 30-50 tài liệu
- 200,000+ từ
- Đa dạng các chủ đề

## Step 2: Tạo QA Pairs

### 2.1 Template QA

Cối file `data/processed/qa_pairs_finetuning.jsonl` với định dạng:

```json
{
  "question": "Bệnh cúm là gì?",
  "answer": "Bệnh cúm (influenza) là bệnh nhiễm trùng đường hô hấp do virus gây ra. Nó có thể gây triệu chứng nhẹ đến nặng như sốt cao, ho, mệt mỏi.",
  "source_document": "benh_cum.txt",
  "category": "definition",
  "difficulty": "easy"
}
```

### 2.2 Các hạng mục QA (Categories)

Tạo đa dạng các loại câu hỏi:

#### a) **Definition** (Định nghĩa)
```
Q: Viêm phổi là gì?
A: Viêm phổi là bệnh lây nhiễm gây viêm túi khí (alveoli) trong phổi...
```

#### b) **Symptoms** (Triệu chứng)
```
Q: Triệu chứng của bệnh cúm là gì?
A: Các triệu chứng chính bao gồm:
- Sốt cao (≥ 38°C)
- Ho khô
- Đau cơ...
```

#### c) **Prevention** (Phòng chống)
```
Q: Làm thế nào để phòng chống cúm?
A: Có thể phòng chống cúm bằng:
- Tiêm vắc xin hàng năm
- Rửa tay thường xuyên...
```

#### d) **Treatment** (Điều trị)
```
Q: Bệnh cúm được điều trị như thế nào?
A: Điều trị cúm thường bao gồm:
- Nghỉ ngơi đầy đủ
- Uống nước nhiều...
```

#### e) **When to see doctor** (Khi nào cần đến bác sĩ)
```
Q: Khi nào tôi nên đến bác sĩ vì bệnh cúm?
A: Bạn nên đến bác sĩ ngay nếu:
- Sốt cao không giảm sau 3 ngày
- Khó thở...
```

#### f) **Risk Factors** (Yếu tố nguy hiểm)
```
Q: Những ai có nguy cơ cao mắc cúm nặng?
A: Những người có nguy cơ cao bao gồm:
- Người già (≥ 65 tuổi)
- Trẻ em dưới 2 tuổi...
```

#### g) **Complications** (Biến chứng)
```
Q: Biến chứng của cúm là gì?
A: Các biến chứng có thể bao gồm:
- Viêm phổi
- Viêm cơ tim...
```

#### h) **First Aid** (Sơ cấp cứu)
```
Q: Sơ cấp cứu cho người bị sốc phản vệ?
A: Sơ cấp cứu bao gồm:
1. Nằm cấp cứu, nâng chân lên
2. Gọi cấp cứu 115 ngay
3. Có thể tiêm epinephrine nếu có sẵn...
```

### 2.3 Tiêu chí câu hỏi tốt

✅ **Tốt:**
- Rõ ràng, cụ thể
- Không quá dài
- Tự nhiên (như người hỏi thực)
- Câu trả lời được trích từ tài liệu

❌ **Tệ:**
- Mơ hồ
- Quá chuyên biệt (chỉ AI biết)
- Câu trả lời không có trong tài liệu

### 2.4 Phân bố QA pairs

Chọn khoảng:

```
Tổng 300+ QA pairs:
- Definition: 40 (13%)
- Symptoms: 50 (17%)
- Prevention: 50 (17%)
- Treatment: 50 (17%)
- When to see doctor: 30 (10%)
- Risk factors: 20 (7%)
- Complications: 20 (7%)
- First aid: 40 (13%)
```

## Step 3: Tạo Test Set

### 3.1 Golden Standard Test Set

Tạo ≥ 50 QA pairs **riêng biệt** cho test set.

**Format:** `data/processed/qa_pairs_test.jsonl`

```json
{
  "question": "Làm thế nào để nhận biết dấu hiệu sốc?",
  "answer": "Dấu hiệu sốc bao gồm: da nhợt nhạt, mạch nhanh (>100 lần/phút), huyết áp thấp, người bệnh lơ mơ hoặc mất ý thức.",
  "source_document": "so_cap_cuu.txt",
  "category": "first_aid"
}
```

### 3.2 Chuẩn bị test set

- **Độc lập**: Không trùng lặp với training set
- **Đa dạng**: Bao gồm tất cả categories
- **Chuẩn bị bởi người khác** nếu có thể
- **Gold standard**: Câu trả lời được xác nhận bởi người chuyên môn

## Step 4: Format Cuối cùng

### 4.1 JSONL Format

Mỗi dòng là một JSON object:

```jsonl
{"question": "Q1", "answer": "A1", "source_document": "doc1.txt", "category": "definition", "difficulty": "easy"}
{"question": "Q2", "answer": "A2", "source_document": "doc2.txt", "category": "symptoms", "difficulty": "medium"}
```

### 4.2 Kiểm tra dữ liệu

```python
import json

with open('data/processed/qa_pairs_finetuning.jsonl', 'r', encoding='utf-8') as f:
    qa_pairs = [json.loads(line) for line in f]
    print(f"Total QA pairs: {len(qa_pairs)}")
    
    # Check categories distribution
    categories = {}
    for qa in qa_pairs:
        cat = qa.get('category', 'unknown')
        categories[cat] = categories.get(cat, 0) + 1
    print("Categories distribution:")
    for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat}: {count}")
```

## Step 5: Validation

Trước khi bắt đầu fine-tuning, kiểm tra:

- ✅ Ít nhất 300 QA pairs cho fine-tuning
- ✅ Ít nhất 50 QA pairs cho test
- ✅ Tất cả JSON đúng format
- ✅ Không có duplicates
- ✅ Câu trả lời rõ ràng và chính xác
- ✅ Đa dạng categories

## Timeline

| Task | Duration | Deadline |
|------|----------|----------|
| Thu thập 20+ tài liệu | 2-3 days | |
| Tạo 300+ QA pairs | 3-5 days | |
| Tạo 50+ test QA | 1-2 days | |
| Validation & cleanup | 1 day | |
| **Tổng** | **1-2 weeks** | |
