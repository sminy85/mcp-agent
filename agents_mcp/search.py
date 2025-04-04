from context.message import create_message
from langchain.utilities import GoogleSerperAPIWrapper

search = GoogleSerperAPIWrapper()

def handle_search_message(message):
    query = message["context"].get("refined_task")
    language = message["context"].get("language", "ko")

    result = search.run(query)

    return create_message(
        sender="SearchAgent",
        recipient="SummarizerAgent",
        context={
            "search_result": result,
            "original_task": message["context"].get("original_task"),
            "language": language
        }
    )
