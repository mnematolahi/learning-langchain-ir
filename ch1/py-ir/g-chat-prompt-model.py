
import os
from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()
from rich import print

metis_api_key = os.getenv("METIS_API_KEY")
metis_base_url = "https://api.metisai.ir/openai/v1"

model = ChatOpenAI(
    model="gpt-4o",
    openai_api_key=metis_api_key,
    openai_api_base=metis_base_url,
    temperature=0.3,
    max_completion_tokens= 50
)

# چت پرامپت تمپلیت مانند نوشتن یک سناریوی نمایش‌نامه است. شما یک لیست از دیالوگ‌ها دارید
# شما مشخص می کنید هر نقش (سیستم، هیومن، ای آی ) چه دیالوگی دشاته باشد

template = ChatPromptTemplate.from_messages (
    [
        ("system","you are a helpful assistant, answer with provided info"),
        ("human","context:{context}"),
        ("human","question:{question}")
    ]
)

response = template.invoke(
    {
        "context": "The most recent advancements in NLP are being driven by Large Language Models (LLMs). These models outperform their smaller counterparts and have become invaluable for developers who are creating applications with NLP capabilities. Developers can tap into these models through Hugging Face's `transformers` library, or by utilizing OpenAI and Cohere's offerings through the `openai` and `cohere` libraries, respectively.",
        "question": "Which model providers offer LLMs?",
    }
)

print(model.invoke(response).content)

