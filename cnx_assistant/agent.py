from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from google.adk.agents import SequentialAgent

from .custom_tools import add_prompt_to_state


intent_agent = Agent(
    model='gemini-2.5-flash',
    name='intent_agent',
    description='An assistant who is specialized at analyzing user intentions.',
    instruction="""
    Analyze the user's PROMPT and find the user's intention about Chaing Mai, CNX.
    Simplyfy the user's PROMPT to pass it to the google_search_agent.

    If the user's PROMPT doesn't make sense to analyze or simply, don't do and ask the user again.

    Your response shoud include:
    - User's question simplified
    - User's intention

    PROMPT:
    { PROMPT }
    """,
    output_key="USER_INTENT"
)


google_search_agent = Agent(
    model='gemini-2.5-flash',
    name='google_research_agent',
    description='An assistant who is specialized at searching information using google search.',
    instruction="""
    You are a helpful assistant to search the answers in the internet for the questions about Chiang Mai, Thailand. 
    Your objective is to provide the best results about Chaing Mai. 

    You have access to google_search tool to search the latest information about Chiang Mai.

    Using the USER_INTENT, search the best results depending on user's intention. 
    USER_INTENT includes:
    - User's qustion
    - User's intention

    Your response should include only the top results and reply with only necessary information.

    USER_INTENT:
    { USER_INTENT }
    """,
    tools=[google_search],
    output_key="SEARCH_DATA"
)


response_formatter_agent = Agent(
    model='gemini-2.5-flash',
    name='response_formatter_agent',
    description='An assistant who is specialized at searching information using google search.',
    instruction="""
    You are the friendly voice of Chiang Mai, Thailand. Your task is to take the
    SEARCH_DATA and present it to the user in a complete and helpful answer.

    - Present the specific information about Chiang Mai.
    - Be conversational and engaging.

    Your response should be in Engilsh.

    SEARCH_DATA:
    { SEARCH_DATA }
    """
)


cnx_workflow = SequentialAgent(
    name='cnx_workflow',
    description='The main workflow for handling user questions about Chiang Mai, Thailand.',
    sub_agents=[
        intent_agent,
        google_search_agent,
        response_formatter_agent
    ]
)


reask_agent = Agent(
    model='gemini-2.5-flash',
    name='reask_agent',
    description='An assistant to encourage users to ask about Chiang Mai, Thailand.',
    instruction="""
    Tell the user politely to ask only about Chiang Mai. 
    """
)


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='The main entry point for helping providing information related to Chiang Mai, Thailand.',
    instruction="""
    You have to do two steps for the user questions. 
    - Welcome the user warmly and let them know you will help finding information about Chiang Mai, Thailand.
    - When the user responds, use add_prompt_to_state tool to save their response.

    After using the tool, transfer control to the cnx_workflow.

    If the user's question isn't asking about Chiang Mai, transfer control to the reask_agent to ask the user again. 
    """,
    tools=[add_prompt_to_state],
    sub_agents=[cnx_workflow, reask_agent]
)
