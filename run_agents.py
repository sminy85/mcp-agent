from agents_mcp.planner import handle_planner_message
from agents_mcp.search import handle_search_message
from agents_mcp.summarizer import handle_summarizer_message
from agents_mcp.reporter import handle_reporter_message
from context.message import create_message

# Step 1: 사용자 입력 기반 메시지 생성
initial_message = create_message(
    sender="User",
    recipient="PlannerAgent",
    context={
        "task": "최근 AI 에이전트 시장 동향에 대해 조사하고 요약해줘",
        "language": "ko"
    }
)

# Step 2: PlannerAgent → SearchAgent
msg1 = handle_planner_message(initial_message)

# Step 3: SearchAgent → SummarizerAgent
msg2 = handle_search_message(msg1)

# Step 4: SummarizerAgent → ReporterAgent
msg3 = handle_summarizer_message(msg2)

# Step 5: ReporterAgent → 최종 메시지
msg4 = handle_reporter_message(msg3)

# 결과 출력
print("\n📄 최종 생성된 보고서:\n")
print(msg4["context"].get("report", "보고서 없음"))
