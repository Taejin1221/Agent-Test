FUNCTIONS = [
    {
        "type": "function",
        "function": {
            "name": "add_expense",
            "description": "새로운 지출 내역을 저장소에 추가하는 함수입니다.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "format": "date-time",
                        "description": "지출 내역의 날짜"
                    },
                    "place": {
                        "type": "string",
                        "description": "지출이 발생한 위치"
                    },
                    "item": {
                        "type": "string",
                        "description": "구매한 서비스나 아이템"
                    },
                    "amount": {
                        "type": "integer",
                        "description": "사용한 금액"
                    },
                    "category": {
                        "type": "string",
                        "enum": ["DRINK", "MEAL", "GIFT", "ENTERTAINMENT", "TRANSPORT"],
                        "description": "지출의 카테고리"
                    },
                    "desc": {
                        "type": "string",
                        "description": "An optional description of the expense.",
                        "nullable": True
                    }
                },
                "required": ["date", "place", "item", "amount", "category"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_expenses",
            "description": "저장소에서 모든 지출 내역을 얻는 함수",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "add_income",
            "description": "새로운 수입 내역을 저장소에 추가하는 함수",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "format": "date-time",
                        "description": "수입이 발생한 일자"
                    },
                    "source": {
                        "type": "string",
                        "description": "수입을 제공한 기관이나 사람"
                    },
                    "amount": {
                        "type": "integer",
                        "description": "수입 가격"
                    },
                    "category": {
                        "type": "string",
                        "enum": ["SALARY", "ALLOWANCE"],
                        "description": "수입 내역의 카테고리"
                    },
                    "desc": {
                        "type": "string",
                        "description": "An optional description of the income.",
                        "nullable": True
                    }
                },
                "required": ["date", "source", "amount", "category"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_incomes",
            "description": "저장소에서 모든 수입 내역을 얻어오는 함수",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    }
]
