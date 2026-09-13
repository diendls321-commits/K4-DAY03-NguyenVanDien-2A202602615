"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    # Tool 1: Tra cứu quỹ phép của nhân viên
    {
        "name": "check_leave_balance",
        "description": "Tra cứu số ngày phép còn lại (phép năm, phép ốm...) của nhân viên VinFast bằng mã nhân viên.",
        "parameters": {
            "type": "object",
            "properties": {
                "employee_id": {
                    "type": "string",
                    "description": "Mã nhân viên cần tra cứu (ví dụ: 'VF12345')"
                }
            },
            "required": ["employee_id"]
        }
    },
    
    # --------------------------------------------------------------------------
    # Tool 2: Tạo đơn xin nghỉ phép
    # --------------------------------------------------------------------------
    {
        "name": "create_leave_request",
        "description": "Tạo đơn xin nghỉ phép cho nhân viên trên hệ thống nhân sự VinFast.",
        "parameters": {
            "type": "object",
            "properties": {
                "employee_id": {
                    "type": "string",
                    "description": "Mã nhân viên VinFast của người cần tạo đơn (ví dụ: 'VF12345')"
                },
                "leave_type": {
                    "type": "string",
                    "description": "Loại hình nghỉ phép (ví dụ: 'Phép năm', 'Nghỉ ốm', 'Nghỉ thai sản', 'Nghỉ không lương')"
                },
                "start_date": {
                    "type": "string",
                    "description": "Ngày bắt đầu nghỉ phép, định dạng DD/MM/YYYY (ví dụ: '25/10/2026')"
                },
                "end_date": {
                    "type": "string",
                    "description": "Ngày kết thúc nghỉ phép, định dạng DD/MM/YYYY (ví dụ: '27/10/2026')"
                },
                "reason": {
                    "type": "string",
                    "description": "Lý do xin nghỉ phép cụ thể của nhân viên"
                }
            },
            "required": ["employee_id", "leave_type", "start_date", "end_date", "reason"]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

MOCK_DATABASE = {
    "VF12345": {
        "full_name": "Nguyễn Văn A",
        "department": "Khối Sản xuất - Xưởng Pin",
        "position": "Kỹ sư tự động hóa",
        "email": "a.nv@vinfast.vn",
        "status": "Đang làm việc",
        "leave_balance": {
            "annual_leave": 12,
            "sick_leave": 5,
            "unpaid_leave": 30
        }
    },
    "VF54321": {
        "full_name": "Trần Thị B",
        "department": "Phòng Kinh doanh",
        "position": "Chuyên viên bán hàng",
        "email": "b.tt@vinfast.vn",
        "status": "Đang làm việc",
        "leave_balance": {
            "annual_leave": 2,
            "sick_leave": 10,
            "unpaid_leave": 30
        }
    }
}


def execute_check_leave_balance(employee_id: str) -> str:
    """Thực thi tra cứu quỹ ngày phép theo mã nhân viên"""
    employee = MOCK_DATABASE.get(employee_id.strip().upper())
    if employee:
        return json.dumps({
            "status": "SUCCESS",
            "employee_id": employee_id,
            "data": employee
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy dữ liệu nhân viên có mã '{employee_id}'"
        }, ensure_ascii=False)


def execute_create_leave_request(employee_id: str, leave_type: str, start_date: str, end_date: str, reason: str) -> str:
    """Thực thi tạo đơn xin nghỉ phép trên hệ thống"""
    # Bước xác thực cơ bản xem nhân viên có tồn tại không
    employee = MOCK_DATABASE.get(employee_id.strip().upper())
    if not employee:
        return json.dumps({
            "status": "ERROR",
            "message": f"Lỗi: Không thể tạo đơn do không tìm thấy nhân viên mã '{employee_id}'."
        }, ensure_ascii=False)
        
    return json.dumps({
        "status": "SUCCESS",
        "request_id": f"REQ-LEAVE-{employee_id}-99",
        "employee_id": employee_id,
        "leave_type": leave_type,
        "start_date": start_date,
        "end_date": end_date,
        "reason": reason,
        "message": f"Tạo đơn '{leave_type}' thành công cho nhân viên {employee_id} từ ngày {start_date} đến {end_date}."
    }, ensure_ascii=False)


# Router gọi tool thực tế
TOOL_ROUTER = {
    "check_leave_balance": execute_check_leave_balance,
    "create_leave_request": execute_create_leave_request
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)