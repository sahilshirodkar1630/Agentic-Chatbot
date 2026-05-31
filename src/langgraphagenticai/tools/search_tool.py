from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tavily_tool():
    """
    Return the list of tools to be used in the chatbot
    """
    tavily_tool = [TavilySearchResults(max_result=2)]
    return tavily_tool

def create_tool_node(tools):
    """
    create and return a tool node for the graph
    """
    return ToolNode(tools=tools)
