import os
import streamlit as st
import json
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime
from context.message import create_message
from agents_mcp.planner import handle_planner_message
from agents_mcp.search import handle_search_message
from agents_mcp.organizer import handle_organizer_message
from agents_mcp.summarizer import handle_summarizer_message
from agents_mcp.reporter import handle_reporter_message

load_dotenv()

st.set_page_config(page_title="MCP 에이전트 보고서 생성기", layout="wide")
st.title("📄 MCP 기반 AI 에이전트 보고서 생성기")

user_prompt = st.text_input("분석할 주제를 입력하세요", "최근 AI 에이전트 시장 동향 요약")

if st.button("보고서 생성"):
    with st.spinner("에이전트들이 정보를 수집하고 정리 중입니다..."):

        # 메시지 흐름 시작
        msg0 = create_message(
            sender="User",
            recipient="PlannerAgent",
            context={"task": user_prompt, "language": "ko"}
        )

        msg1 = handle_planner_message(msg0)
        msg2 = handle_search_message(msg1)
        msg3 = handle_organizer_message(msg2)
        msg4 = handle_summarizer_message(msg3)
        msg5 = handle_reporter_message(msg4)

        # 보고서 텍스트만 추출
        report_text = msg5["context"].get("report", "보고서 없음")

        # 📌 에이전트별 중간 결과 표시
        with st.expander("🔧 Planner 출력"):
            st.code(msg1["context"].get("refined_task", "-"), language="markdown")

        with st.expander("🌐 Search 결과"):
            st.code(msg2["context"].get("search_result", "-"), language="markdown")

        with st.expander("🗂 Organizer 정리"):
            try:
                # JSON 형태 파싱 시도
                organized_info = msg3["context"].get("organized_info", "{}")
                parsed = json.loads(organized_info)

                # 테이블 형태로 변환 (카테고리 → 항목 리스트)
                rows = []
                for category, items in parsed.items():
                    for item in items:
                        rows.append({"항목": category, "내용": item})

                df = pd.DataFrame(rows)
                st.dataframe(df)

            except Exception as e:
                # JSON 파싱 실패한 경우 그냥 텍스트 출력
                st.code(organized_info, language="markdown")

        with st.expander("📝 Summarizer 요약"):
            st.code(msg4["context"].get("summary", "-"), language="markdown")

        # 결과 보고서 출력
        st.subheader("📃 최종 보고서")
        st.text_area("요약 보고서", report_text, height=400)

        # 자동 저장 - 파일명: output/보고서_날짜시간.txt
        os.makedirs("output", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"output/보고서_{timestamp}.txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(report_text)

        st.success(f"📁 보고서가 저장되었습니다: {filename}")
