from langchain_experimental.agents import create_csv_agent
from langchain_community.llms import OpenAI
import streamlit as st
import os
import tempfile

os.environ["OPENAI_API_KEY"] = "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"

def main():
    # Configure Streamlit page
    st.set_page_config(page_title="Ask your CSV")
    st.header("Ask your CSV")

    file = st.file_uploader("upload file", type="csv")

    if file is not None:
        with tempfile.NamedTemporaryFile(mode='w+', suffix=".csv", delete=False, encoding='utf-8') as f:

            # Converting bytes to a string before writing to the file
            data_str = file.getvalue().decode('utf-8')
            f.write(data_str)
            f.flush()

            # An instance of the OpenAI language model with temperature set to 0
            llm = OpenAI(temperature=0)

            user_input = st.text_input("Enter the question here:")

            # A CSV agent using the OpenAI language model and the temporary file
            agent = create_csv_agent(llm, f.name, verbose=True)

            if user_input:
                # Run the agent on the user's question and get the response
                response = agent.run(user_input)
                st.write(response)
            
            if file is not None:
                with tempfile.NamedTemporaryFile(mode='w+', suffix=".csv", delete=False, encoding='utf-8') as f:
                    # Convert bytes to a string before writing to the file
                    data_str = file.getvalue().decode('utf-8')
                    f.write(data_str)
                    f.flush()

if __name__ == "__main__":
    main()