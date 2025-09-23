## کلاس ChatOpenAI (مدرن و صحیح)
کد: from langchain_openai.chat_models import ChatOpenAI

هدف: این کلاس مخصوص مدل‌های گفتگو (Chat Models) ساخته شده است، مانند gpt-3.5-turbo, gpt-4, و مدلی که شما استفاده می‌کنید یعنی gpt-4o.

نحوه کار: این مدل‌ها برای مکالمه و پیروی از دستورالعمل‌ها بهینه شده‌اند. ورودی آن‌ها صرفاً یک متن ساده نیست، بلکه لیستی از «پیام‌ها» است که هر کدام یک «نقش» (Role) دارند (مانند system, user, assistant). البته LangChain کار را ساده کرده و وقتی شما یک رشته ساده به invoke می‌دهید، آن را به صورت خودکار به یک پیام با نقش user تبدیل می‌کند.

چرا به درستی کار می‌کند؟ چون این کلاس دقیقاً برای مدل gpt-4o طراحی شده است. درخواست را با فرمت صحیح (لیست پیام‌ها) به سرور می‌فرستد و سرور پاسخ می‌دهد. خروجی آن نیز یک آبجکت پیام (Message Object) است، نه فقط یک رشته ساده. این آبجکت شامل محتوای متنی (.content) و اطلاعات دیگر است. به همین دلیل شما می‌توانید response.content را چاپ کنید.import os
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
