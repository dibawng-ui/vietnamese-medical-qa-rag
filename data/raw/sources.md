# Sources for Medical Documents

## Nguồn tài liệu Y tế Phổ thông

Hãy thu thập tài liệu từ các nguồn uy tín sau:

### 1. Trang web chính thức
- **Bộ Y tế Việt Nam**: https://moh.gov.vn/
- **Trung tâm Kiểm soát bệnh tật Việt Nam**: https://vncdc.gov.vn/
- **Viện Vệ sinh Dịch tễ Trung ương**: https://nihe.gov.vn/
- **Hospital.com.vn**: https://hospital.com.vn/

### 2. Kiến thức y tế
- **Wikipedia - Danh mục Y học**: Các bài về bệnh, điều trị
- **Sách y tế**: Sách hướng dẫn sơ cấp cấp cứu, kiến thức y tế gia đình
- **Tài liệu WHO**: Hướng dẫn phòng chống bệnh

### 3. Lĩnh vực cần tập trung (Priority)
- Bệnh thường gặp (cúm, viêm phổi, tiêu chảy, etc.)
- Phòng chống bệnh (vệ sinh, vắc xin, hygiene)
- Sơ cấp cứu cơ bản (vết thương, chuyển dạ, sốc)
- Dinh dưỡng và sức khỏe
- Phòng chống nhiễm trùng

### 4. Format tài liệu cần lưu
- Lưu dưới dạng `.txt` hoặc `.pdf` trong thư mục `data/raw/documents/`
- Đặt tên file rõ ràng: `benh_cum.txt`, `so_cap_cuu.txt`, etc.
- Tối thiểu 20 tài liệu, tổng ≥ 100,000 từ

### 5. Ví dụ cấu trúc tài liệu

```
--- source: benh_cum_thong_thuong.txt ---
Tiêu đề: Bệnh Cúm Thông Thường

1. Định nghĩa
Bệnh cúm (influenza) là bệnh do virus gây ra...

2. Triệu chứng
- Sốt cao
- Ho
- Mệt mỏi

3. Cách phòng chống
...

4. Khi nào cần đến bác sĩ
...
```

## Tạo QA Pairs từ tài liệu

Sau khi có tài liệu, tạo QA pairs theo template:

```json
{
  "question": "Bệnh cúm là gì?",
  "answer": "Bệnh cúm (influenza) là bệnh do virus gây ra...",
  "source_document": "benh_cum_thong_thuong.txt",
  "category": "definition"
}
```

**Hạng mục QA cần tạo:**
1. Definition - Định nghĩa
2. Symptoms - Triệu chứng
3. Prevention - Phòng chống
4. Treatment - Điều trị
5. When to see doctor - Khi nào cần đến bác sĩ
6. Risk factors - Yếu tố nguy hiểm
7. Complications - Biến chứng
8. First aid - Sơ cấp cứu
