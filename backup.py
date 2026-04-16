# This is code of ai agent who can performe resoning task only 


import streamlit as st
from langchain_classic.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_classic.chains.llm_math.base import LLMMathChain
from langchain_classic.tools import tool
from langchain_classic.chains.llm import LLMChain
from langchain_classic.agents import create_react_agent,AgentExecutor
from langchain_classic.callbacks import StreamlitCallbackHandler



## Set upi the Stramlit app
st.set_page_config(page_title="SolveX AI: Intelligent Math & Reasoning Agent",page_icon="🧮")
st.title("SolveX AI: Intelligent Math & Reasoning Agent")

groq_api_key=st.sidebar.text_input(label="Enter Groq Api key",type="password")

if not groq_api_key:
    st.warning("Enter Groq api key")
    st.stop()

wikipedia_api_wrapper=WikipediaAPIWrapper()
@tool
def wikipedia_tool(query:str)->str:
    "A tool for searching the Internet to find the vatious information on the topics mentioned"
    return wikipedia_api_wrapper.run(query=query)

llm=ChatGroq(groq_api_key=groq_api_key,model="llama-3.3-70b-versatile")



prompt="""
        You are an AI agent specialized in solving mathematical and reasoning problems.

        You have access to the following tools:
        {tools}

        Tool names:
        {tool_names}

        Follow this format:

        Question: {question}
        Thought: think step by step
        Action: one of [{tool_names}]
        Action Input: input to the tool
        Observation: result of the tool
        ... (repeat if needed)
        Thought: I now know the final answer
        Final Answer: provide a clear, step-by-step explanation

        {agent_scratchpad}
"""

prompt_template=PromptTemplate(
    template=prompt,
    input_variables=["question"]
)

math_prompt = PromptTemplate.from_template(
"""You are a calculator.

Return ONLY the mathematical expression in EXACT format:

```text
2 + 2
'''
"""
)

llm_math_chain=LLMMathChain.from_llm(
    llm=llm,
    prompt=math_prompt
    )


@tool
def llm_math_chain_tool(query:str)->str:
    "A tools for answering math related questions. Only input mathematical expression need to bed provided"
    query = query.replace("numexpr.evaluate", "")
    return llm_math_chain.run({"question":query})

chain=LLMChain(llm=llm,prompt=prompt_template)
@tool
def chain_tool(query:str)->str:
    "A tool for answering logic-based and reasoning questions."
    return chain.run({"question":query})

tools=[chain_tool,llm_math_chain_tool,wikipedia_tool]

agent=create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt_template
)

final_agent=AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=False,
    )

if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"Assistent","context":"Hey i am ai agent for solving your maths questions"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["context"])


question=st.text_area("Enter youe question:","I have 5 bananas and 7 grapes. I eat 2 bananas and give away 3 grapes. Then I buy a dozen apples and 2 packs of blueberries. Each pack of blueberries contains 25 berries. How many total pieces of fruit do I have at the end?")

if st.button("Find my answer"):
    if question:
        with st.spinner("Genrating response"):
            st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
            st.session_state.messages.append({"role":"user","context":question})
            st.chat_message("user").write(question)
            response=final_agent.invoke(
                {"question":question},
                {"callbacks":[st_cb]}
            )
            st.session_state.messages.append({"role":"assistent","context":response})

            st.write(response)
    
    else:
        st.warning("Please enter question")