from langchain.utilities import GoogleSerperAPIWrapper
from context.message import create_message 

search = GoogleSerperAPIWrapper()

def search_info(query: str) -> str:
    return search.run(query)
