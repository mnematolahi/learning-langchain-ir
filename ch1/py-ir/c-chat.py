import os
from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage
load_dotenv()

metis_api_key = os.getenv("METIS_API_KEY")
metis_base_url = "https://api.metisai.ir/openai/v1"

model = ChatOpenAI(
    model="gpt-4o",
    openai_api_key=metis_api_key,
    openai_api_base=metis_base_url,
    temperature=0.3,
    max_completion_tokens= 10
)

System_msg = SystemMessage(
    "You are a helpful assistant that responds to questions with three exclamation marks. "
)

human_msg = HumanMessage("What is the capital of France?")
response = model.invoke([System_msg, human_msg])
print(response.content)
