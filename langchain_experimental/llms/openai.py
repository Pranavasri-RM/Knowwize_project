# langchain_experimental/llms/openai.py

from langchain_community.llms import OpenAI as BaseOpenAI

class OpenAI(BaseOpenAI):
    def __init__(self, temperature):
        # Initialize the OpenAI language model
        super().__init__(temperature=temperature)

    def generate_response(self, user_input):
        # Use the OpenAI language model to generate a response
        response = self.complete_prompt(user_input)
        return response.choices[0].text.strip()
