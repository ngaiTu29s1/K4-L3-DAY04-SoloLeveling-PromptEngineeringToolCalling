# TEAM — Day04, K4-L3B

**Làm nhóm / Cá nhân.** Mỗi người tự viết và commit phần INDIVIDUAL của mình.

## Thông tin bài nộp

- Tên nhóm: Solo Leveling
- Người đại diện / MSSV: Trần Tuấn Tú / 2A202602840
- Tên repo: `K4-L3-DAY04-TranTuanTu-2A202602840-PromptEngineeringToolCalling`
- URL repo, nhánh nộp, commit chốt: `https://github.com/ngaiTu29s1/K4-L3-DAY04-TranTuanTu-2A202602840-PromptEngineeringToolCalling` (nhánh main)
- Deadline áp dụng và link thông báo đổi hạn nếu có: 23:59 ngày làm lab

## Thành viên

| Họ và tên | MSSV | GitHub | Vai trò và công việc | File/commit/PR |
|---|---|---|---|---|
| Trần Tuấn Tú | 2A202602840 | ngaiTu29s1 | Toàn bộ dự án: Thiết kế prompt v0-v3, tối ưu tool schema, benchmark evaluation, viết 10 case nhóm, kiểm thử an toàn, xây dựng UI chat và báo cáo | `artifacts/*`, `data/eval_group.json`, `tools/*` |

## Nhận xét chung

- Kết quả và bằng chứng: Hoàn thành đầy đủ các version từ v0 đến v3, đạt accuracy cao trên cả bộ eval base (30 cases) và adversarial (12 cases).
- Thay đổi hiệu quả nhất: Tinh chỉnh system prompt phân định ranh giới rõ ràng giữa kiểm tra máy cụ thể và dịch vụ chung, quy định bắt buộc clarify khi thiếu thông tin và cơ chế xác nhận trước khi thực hiện hành động ghi dữ liệu.
- Giới hạn còn lại: Một số câu hỏi đa lượt phức tạp đòi hỏi ngữ cảnh dài cần quản lý memory tốt hơn.
- Cách phân công và tích hợp: Làm độc lập toàn bộ các khâu từ setup, thiết kế, chạy benchmark, audit security đến viết báo cáo.

## INDIVIDUAL

### Trần Tuấn Tú — 2A202602840

- Phần việc và file/commit/PR:
  - Cấu hình provider Groq (hỗ trợ `qwen/qwen3.8-27b`) và tích hợp adapter.
  - Xây dựng và tối ưu `system_prompt.md` và `tools.yaml` qua 4 phiên bản (v0 -> v1 -> v2 -> v3).
  - Soạn thảo 10 case kiểm thử độc lập cho nhóm trong `data/eval_group.json`.
  - Chạy và phân tích benchmark toàn diện: eval base, eval group, và eval adversarial.
  - Hoàn thiện báo cáo kỹ thuật `REPORT.md` và tài liệu nộp bài.
- Quyết định, khó khăn và cách xử lý:
  - Khó khăn: Model dễ bị nhầm lẫn giữa `check_service_status` và `inspect_device` khi người dùng nhắc đến cả tên dịch vụ và tên máy trong cùng một câu hoặc qua nhiều lượt nói.
  - Xử lý: Đưa ra quy tắc rõ ràng trong prompt và mô tả tool schema: nếu yêu cầu nhắc đến mã tài sản cụ thể (`asset_id`) thì ưu tiên `inspect_device`, nếu nói về hạ tầng chung thì dùng `check_service_status`, nếu so sánh hoặc nhắc cả hai thì kích hoạt song song.
- Điều đã học: Hiểu sâu về cơ chế Function Calling / Tool Calling của LLM, cách thiết kế Schema chặt chẽ để model không hallucinate tham số, và cách phòng thủ trước prompt injection / role spoofing.
- AI/công cụ đã dùng và cách kiểm tra: Sử dụng Antigravity CLI hỗ trợ kiểm tra đối chiếu code và phân tích kết quả run tự động. Tự chạy kiểm thử với `run_eval.py` để verify metric thực tế.
- Thời điểm đã tự nộp URL repo chung trên VLearn: Đã cập nhật và sẵn sàng nộp URL repo.
