from context.message import create_message

def handle_reporter_message(message):
    summary = message["context"].get("summary", "요약 내용 없음")
    task = message["context"].get("original_task", "")

    report = f"""
📄 [AI 자동 보고서]

🧩 주제: {task}

📝 요약:
{summary}

⏱️ 생성일시: {message['context'].get('timestamp')}
📍 생성자: MCP 기반 ReporterAgent
"""

    return create_message(
        sender="ReporterAgent",
        recipient="User",
        context={
            "report": report
        }
    )
