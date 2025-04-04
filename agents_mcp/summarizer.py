from context.message import create_message
from langchain_community.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

def handle_summarizer_message(message):
    # ✅ organizer가 전달한 organized_info 사용
    organized_text = message["context"].get("organized_info")
    language = message["context"].get("language", "ko")

    prompt = f"다음 정보를 한국어로 자연스럽게 요약해줘:\n\n{organized_text}"
    summary_result = llm.invoke(prompt)
    summary = summary_result.content

    return create_message(
        sender="SummarizerAgent",
        recipient="ReporterAgent",
        context={
            "summary": summary,
            "original_task": message["context"].get("original_task"),
            "language": language
        }
    )
