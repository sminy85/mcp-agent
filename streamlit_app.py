import os
import streamlit as st
from langchain.agents import initialize_agent, Tool
from langchain_community.chat_models import ChatOpenAI
from langchain.utilities import GoogleSerperAPIWrapper
from dotenv import load_dotenv

# 1. API Key 불러오기 (.env에서)
load_dotenv()

# 2. LLM & 검색 툴 설정
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
search = GoogleSerperAPIWrapper()

tools = [
    Tool(
        name="Search",
        func=search.run,
        description="Search the internet for recent AI news"
    )
]

# 3. LangChain 에이전트 초기화
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

# 4. Streamlit UI 구성
st.title("📄 AI 에이전트 보고서 생성기")
prompt = st.text_area("요청 입력", "최근 AI 에이전트 시장 동향 정리해줘. 반드시 한국어로 대답")

if st.button("생성"):
    with st.spinner("생성 중입니다..."):
        result = agent.run(prompt)
        st.success("완료!")
        st.write(result)
