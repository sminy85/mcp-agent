from context.message import create_message
from langchain_community.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

def handle_organizer_message(message):
    search_result = message["context"].get("search_result", "")
    language = message["context"].get("language", "ko")

    prompt = f"""
                다음 정보를 항목별 JSON 형태로 정리해줘.
                카테고리: '시장 규모', '기술 트렌드', '주요 기업 동향'
                예시:
                {{
                "시장 규모": ["2024년 52억 달러", "2030년까지 연 40% 성장"],
                "기술 트렌드": ["생성형 AI를 넘어 실시간 작업 수행", "AI 에이전트 자율성"],
                "주요 기업 동향": ["Amazon 'Nova Act'", "WISEnut 기업용 확장"]
                }}
                응답은 반드시 JSON 형식으로, 한국어로 작성해줘:

                {search_result}
                """
    organized = llm.invoke(prompt).content

    return create_message(
        sender="OrganizerAgent",
        recipient="SummarizerAgent",
        context={
            "organized_info": organized,
            "original_task": message["context"].get("original_task"),
            "language": language
        }
    )
