# در اینجا از ال ال ام استفاده می وشد و نه قابلیت چت. خروجی آن یک رشته ساده است

import os
from dotenv import load_dotenv
from langchain_openai.llms import OpenAI

load_dotenv()

metis_api_key = os.getenv("METIS_API_KEY")
metis_base_url = "https://api.metisai.ir/openai/v1"


model = OpenAI(
    model="gpt-3.5-turbo-instruct",
    openai_api_key=metis_api_key,
    openai_api_base=metis_base_url,
    max_tokens=10
    
)
response = model.invoke("the sky is")
print(response)
