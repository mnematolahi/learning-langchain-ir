
import os
from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate
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

# پرامپت تمپلیت فقط متن می گیرد و بنابراین به اون رشته های متنی دادیم. پرامپت تمپلیت مانند نوشتن یک نامه چند خطی است که چند تا متن فقط داخلش میزاریم
template = PromptTemplate.from_template("""Answer the question based on the context below. If the question cannot be answered using the information provided, answer with "I don't know".
    context={context}
    question={question}
    
    
answer:""")
# ایجاد دیکشنری برای تعیین دقیق مقدار متغییرهای بالا
prompt = template.invoke({
    "context": "The most recent advancements in NLP are being driven by Large Language Models (LLMs). These models outperform their smaller counterparts and have become invaluable for developers who are creating applications with NLP capabilities. Developers can tap into these models through Hugging Face's `transformers` library, or by utilizing OpenAI and Cohere's offerings through the `openai` and `cohere` libraries, respectively.",
    "question":"which model providers offer llms?"   
})

response = model.invoke(prompt)
print(response.content)
