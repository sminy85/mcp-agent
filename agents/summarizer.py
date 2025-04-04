# from langchain_community.chat_models import ChatOpenAI

# llm = ChatOpenAI(temperature=0)

# def summarize_text(raw_info: str) -> str:
#     return llm.invoke(f"다음 내용을 한국어로 요약해줘:\n\n{raw_info}")

from context.message import create_message
from langchain_community.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

def handle_summarizer_message(message):
    raw_text = message["context"].get("search_result")
    language = message["context"].get("language", "ko")

    prompt = f"다음 정보를 한국어로 자연스럽게 요약해줘:\n\n{raw_text}"
    summary = llm.invoke(prompt)

    return create_message(
        sender="SummarizerAgent",
        recipient="ReporterAgent",
        context={
            "summary": summary,
            "original_task": message["context"].get("original_task"),
            "language": language
        }
    )