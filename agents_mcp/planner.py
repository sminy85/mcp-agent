from context.message import create_message

def handle_planner_message(message):
    task = message["context"]["task"]
    language = message["context"].get("language", "ko")

    refined_task = f"{task} 관련 정보를 검색해주세요."

    return create_message(
        sender="PlannerAgent",
        recipient="SearchAgent",
        context={
            "refined_task": refined_task,
            "original_task": task,
            "language": language
        }
    )
