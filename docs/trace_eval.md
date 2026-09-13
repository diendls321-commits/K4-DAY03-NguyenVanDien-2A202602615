# **BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)**

\> **Họ và Tên Học viên:** Nguyễn Văn Điền

\> **Mã Sinh Viên / Mã Học viên:** 2A202602615

\> **Chủ đề Lựa chọn:** Trợ lý Nhân sự thông minh (HR Assistant)

## ---

**1\. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)**

| Tiêu chí Đánh giá | Mức độ (1 \- 5\) | Giải trình chi tiết lý do chọn điểm&nbsp;&nbsp; |
| :---- | :---- | :---- |
| **1\. Multi-step Reasoning** | 4 / 5 | Để tạo đơn nghỉ phép, Agent cần thực hiện chuỗi logic: Nhận diện ý định \-\> Tra cứu ngày phép \-\> So sánh quỹ phép \-\> Trích xuất thông tin (ngày, lý do) \-\> Tạo đơn. |
| **2\. Tool Interaction** | 5 / 5 | Bắt buộc gọi API/MCP kết nối với hệ thống quản trị nhân sự (HRIS/ERP) để kiểm tra phép, ghi nhận đơn và truy xuất RAG để đọc chính sách bảo hiểm nội bộ. |
| **3\. Dynamic Decision** | 4 / 5 | Hành động tiếp theo phụ thuộc kết quả tra cứu. Nếu hết phép, Agent phải gợi ý nghỉ không lương. Nếu xin nghỉ ốm dài ngày, Agent phải yêu cầu bổ sung giấy tờ y tế. |
| **4\. Long Horizon Goal** | 4 / 5 | Agent phải duy trì tiến trình thu thập thông tin (ngày đi, ngày về, lý do) qua nhiều lượt chat, ngay cả khi bị ngắt quãng bởi các câu hỏi phụ về chính sách bảo hiểm. |
| **TỔNG ĐIỂM AGENTIC FIT** | **17 / 20** | *Nếu tổng điểm \> 12/20: Bài toán rất phù hợp triển khai Agentic System.* |

## ---

**2\. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)**

\> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp .env điền GEMINI\_API\_KEY (hoặc OPENAI\_API\_KEY) để kết nối LLM thật trước khi thực thi python src/app.py \--all. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file docs/trace\_waterfall.json sinh ra từ phản hồi LLM API thật:

`[`  
  `{`  
    `"step": 1,`  
    `"query": "Tôi (Mã NV: VF12345) muốn xin nghỉ ốm từ ngày 01/11 đến 03/11/2026. Hãy kiểm tra xem tôi còn đủ ngày phép ốm hưởng nguyên lương không, nếu còn hãy tạo đơn giúp tôi.",`  
    `"action_type": "TOOL_EXECUTION",`  
    `"tool_name": "check_leave_balance",`  
    `"arguments": {`  
      `"employee_id": "VF12345"`  
    `},`  
    `"observation": {`  
      `"status": "SUCCESS",`  
      `"employee_id": "VF12345",`  
      `"data": {`  
        `"full_name": "Nguyễn Văn A",`  
        `"department": "Khối Sản xuất - Xưởng Pin",`  
        `"position": "Kỹ sư tự động hóa",`  
        `"email": "a.nv@vinfast.vn",`  
        `"status": "Đang làm việc",`  
        `"leave_balance": {`  
          `"annual_leave": 12,`  
          `"sick_leave": 5,`  
          `"unpaid_leave": 30`  
        `}`  
      `}`  
    `},`  
    `"latency_ms": 1531.05`  
  `},`  
  `{`  
    `"step": 2,`  
    `"query": "Tôi (Mã NV: VF12345) muốn xin nghỉ ốm từ ngày 01/11 đến 03/11/2026. Hãy kiểm tra xem tôi còn đủ ngày phép ốm hưởng nguyên lương không, nếu còn hãy tạo đơn giúp tôi.",`  
    `"action_type": "TOOL_EXECUTION",`  
    `"tool_name": "create_leave_request",`  
    `"arguments": {`  
      `"leave_type": "Nghỉ ốm",`  
      `"end_date": "03/11/2026",`  
      `"employee_id": "VF12345",`  
      `"reason": "Nghỉ ốm điều trị bệnh",`  
      `"start_date": "01/11/2026"`  
    `},`  
    `"observation": {`  
      `"status": "SUCCESS",`  
      `"request_id": "REQ-LEAVE-VF12345-99",`  
      `"employee_id": "VF12345",`  
      `"leave_type": "Nghỉ ốm",`  
      `"start_date": "01/11/2026",`  
      `"end_date": "03/11/2026",`  
      `"reason": "Nghỉ ốm điều trị bệnh",`  
      `"message": "Tạo đơn 'Nghỉ ốm' thành công cho nhân viên VF12345 từ ngày 01/11/2026 đến 03/11/2026."`  
    `},`  
    `"latency_ms": 1571.75`  
  `},`  
  `{`  
    `"step": 3,`  
    `"query": "Tôi (Mã NV: VF12345) muốn xin nghỉ ốm từ ngày 01/11 đến 03/11/2026. Hãy kiểm tra xem tôi còn đủ ngày phép ốm hưởng nguyên lương không, nếu còn hãy tạo đơn giúp tôi.",`  
    `"action_type": "FINAL_ANSWER",`  
    `"thought": "Gemini phản hồi trực tiếp bằng văn bản (không cần gọi công cụ).",`  
    ``"output": "Chào anh Nguyễn Văn A,\n\nTôi đã hoàn tất việc kiểm tra quỹ phép và tạo đơn nghỉ phép cho anh trên hệ thống nhân sự VinFast. Dưới đây là chi tiết kết quả:\n\n1. **Kiểm tra quỹ ngày phép:**\n   - Số ngày phép ốm hiện tại của anh còn lại: **5 ngày** (đủ điều kiện nghỉ từ ngày 01/11/2026 đến 03/11/2026, tổng cộng 3 ngày).\n\n2. **Kết quả tạo đơn:**\n   - **Mã đơn:** `REQ-LEAVE-VF12345-99`\n   - **Loại hình:** Nghỉ ốm\n   - **Thời gian:** Từ ngày 01/11/2026 đến 03/11/2026\n   - **Lý do:** Nghỉ ốm điều trị bệnh\n   - **Trạng thái:** Tạo đơn thành công trên hệ thống.\n\nAnh vui lòng nộp giấy chứng nhận nghỉ việc hưởng bảo hiểm xã hội (hoặc giấy khám bệnh của cơ sở y tế) về bộ phận Nhân sự theo đúng quy định để hoàn tất thủ tục hưởng chế độ. Chúc anh mau chóng bình phục!",``  
    `"latency_ms": 2873.47`  
  `}`  
`]`

## ---

**3\. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI**

> * \[x\] Đã điền API Key thật trong .env và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).  
> * **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.  
> * **Số lượt gọi Tool qua MCP Server chính xác:** 5 lượt.  
> * **Kết quả đẩy Repo nộp bài:** \[x\] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

\> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3\!