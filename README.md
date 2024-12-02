# Agent-Test
간단한 가계부 서비스를 자연어로 실행하는 Agent입니다.

# 실행
1. 필요 모듈 설치
    ```shell
    pip install -r requirement.txt
    ```

2. 환경 변수 설정
    ```shell
    export OPENAI_API_KEY="<api_key>"
    ```

3. DB로 사용할 파일 설정
    ```json
    {
        "incomes": [],
        "expenses": [],
        "balances": 0
    }
    ```

4. 실행
    ```shell
    python3 test/chat_service_test.py
    ```
