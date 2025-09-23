import os
from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage
load_dotenv()

metis_api_key = os.getenv("METIS_API_KEY")
metis_base_url = "https://api.metisai.ir/openai/v1"

model = ChatOpenAI(
    model="gpt-4o",
    openai_api_key=metis_api_key,
    openai_api_base=metis_base_url,
    max_completion_tokens=10
)

prompt = [HumanMessage("what is the capital of france?")]
response = model.invoke(prompt)
print(response.content)
