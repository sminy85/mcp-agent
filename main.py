import os
from langchain.agents import initialize_agent, Tool
from langchain_community.chat_models import ChatOpenAI
from langchain.utilities import GoogleSerperAPIWrapper
from dotenv import load_dotenv

load_dotenv()  # .env에서 API Key 읽기

search = GoogleSerperAPIWrapper()

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")  # 또는 gpt-4

tools = [
    Tool(
        name="Search",
        func=search.run,
        description="Search the internet for recent AI news"
    )
]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

output = agent.run("최근 AI 에이전트 시장 동향을 분석해서 요약해줘. 반드시 한국어로만 대답해")

# 결과를 파일로 저장
with open("output/ai_report.md", "w", encoding="utf-8") as f:
    f.write(output)

# 또는 .txt로 저장
with open("output/ai_report.txt", "w", encoding="utf-8") as f:
    f.write(output)


os.makedirs("output", exist_ok=True)  # 이 줄 추가
with open("output/ai_report.md", "w", encoding="utf-8") as f:
    f.write(output)
