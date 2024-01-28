from langchain_community.llms.openai import OpenAI
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents import create_csv_agent
import pandas as pd
import os

os.environ["OPENAI_API_KEY"] = "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"

agent = create_csv_agent(OpenAI(temperature=0), 'stock_data.csv', verbose=True)
agent.run("Identify the date with the highest trading volume.")