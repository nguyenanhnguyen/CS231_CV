# Lộ trình ôn thi cuối kỳ CS231

Cơ sở: đề mẫu `dethi/Dethi.CS231.Q2.2026.pdf` (mới có 1 đề, kỳ này có thể ra khác) và slide T1–T12.
Mỗi buổi 60–90 phút: học trọng tâm → tự làm trên giấy → bắt lỗi cài sẵn → chấm, ghi lỗi.

| Buổi | Nội dung | Slide | Trong đề mẫu | Trạng thái |
|---|---|---|---|---|
| 1 | Confusion matrix, Accuracy, Precision, Recall, F1, macro/weighted | T4 | Câu 2, 8 (3.0đ) | Đang học |
| 2 | CNN: kích thước đầu ra, số tham số, số phép nhân, softmax/sigmoid | T8 | Câu 3 (2.0đ) | |
| 3 | TGMT là gì, ảnh số, lấy mẫu, lượng tử hóa, dung lượng, không gian màu | T1, T2 | Câu 1a, 1b | |
| 4 | Histogram, color moment, correlogram, khoảng cách; feature/embedding, global/local | T2, T3 | Câu 4–7 (2.5đ) | |
| 5 | Phát biểu bài toán (Input/Output), phân loại ảnh, KNN, linear classifier; đồ án | T4, T5, T13 | Câu 1c (1.0đ) | |
| 6 | Cạnh: Sobel, Prewitt, Canny (tính tay) | T6 | | |
| 7 | HOG: gradient, cell, block, số chiều | T7 | | |
| 8 | Localization, IoU, NMS, Detection, mAP | T9–T11 | Câu 9 (0.5đ) | |
| 9 | Phân đoạn ảnh: ngưỡng, gom cụm, độ đo | T12 | | |
| 10 | Thi thử có cài lỗi, hoàn thiện tài liệu mang vào phòng thi | Tất cả | Cả đề | |

Nếu còn ít hơn 10 ngày: ưu tiên buổi 1, 2, 4, 3, 5, 8.

## Quy tắc đọc đề (chống bẫy)
1. Kiểm tra một lớp có bị gọi bằng hai tên không (Cá/Fish, Cua/Crab).
2. Câu phụ thuộc MSSV: 24521185 → chữ số đầu là 2 (conv2, fc2). Đọc lại xem đề hỏi chữ số đầu hay cuối.
3. Ma trận: xác định hàng là ground truth hay prediction trước khi tính.
4. Cộng kiểm tra: tổng các hàng = tổng các cột = tổng số mẫu.
5. Thấy đề có chỗ sai hoặc mơ hồ: ghi rõ chỗ đó, sửa lại, nêu giả định rồi mới làm.

## Cảnh báo về file `CS231_note.docx` (tự giải đề)
- Câu 1b: ghi ảnh 4x3 là 4 hàng, 3 cột. Slide T2 ghi kích thước ảnh theo **rộng × cao** (800 x 600),
  vậy ảnh 4x3 là **4 cột, 3 hàng**. (Ký hiệu ma trận thì là hàng × cột.) Khi làm bài nên ghi rõ quy ước.
- Câu 5, 6: cần đối chiếu lại (sẽ sửa ở buổi 4).
- Các phần khác chưa được kiểm tra hết.

## Nhật ký lỗi
(ghi sau mỗi buổi)
