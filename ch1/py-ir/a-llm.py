# در این مثال از کلاس ChatOpenAI استفاده می شود. این کلاس مدرن است و نتیجه فروجی آن یک رشته ساده نیست بلکه یک آبجکت است. این مدل با gpt-4o در متیس قابل استفاده است


from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI

load_dotenv()

metis_api_key = os.getenv("METIS_API_KEY")
metis_base_url = "https://api.metisai.ir/openai/v1"

model = ChatOpenAI(
    model="gpt-4o",
    openai_api_key=metis_api_key,
    openai_api_base=metis_base_url,
  # به علت محدودیت توکن عدد 5 قرار گرفته ولی شما می توانید اگر محدودیت هزینه ندارید خط زیر را حذف نمایید.
    max_completion_tokens=5
)

print(" sending info to llm ...")

response = model.invoke("The sky is")
print(response.content)
