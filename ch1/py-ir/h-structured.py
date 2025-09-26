import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel
# --- برای چاپ زیبای خروجی ابتدا pip install rich را نصب نمایید ---
# --- اکر نصب ندارید دستور زیر را کامنت کنید ---
from rich import print
load_dotenv()

# --- دریافت کلید و آدرس API ---
metis_api_key = os.getenv("METIS_API_KEY")
metis_base_url = "https://api.metisai.ir/openai/v1"

# --- تعریف ساختار خروجی با Pydantic ---
class AnswerWithJustification(BaseModel):
    """An answer to the user's question along with justification for the answer."""
    answer: str
    """The answer to the user's question"""
    justification: str
    """Justification for the answer"""

# --- ساخت مدل زبان با پارامتر صحیح ---
llm = ChatOpenAI(
    model="gpt-4o",
    openai_api_key=metis_api_key,
    openai_api_base=metis_base_url,
    temperature=0.0,
   # max_tokens=50  # <-- اینجا اصلاح شد
)

# --- ساخت مدل ساختاریافته ---
structured_llm = llm.with_structured_output(AnswerWithJustification)

# --- فراخوانی مدل و چاپ نتیجه ---
response = structured_llm.invoke(
    "What weighs more, a pound of bricks or a pound of feathers")


# --- اگر می خواهید پاسخ با رعایت انیتر و خط های جداگانه باشد دستورات زیر را از حالت کامنت بردارید ---
# # ۱. استخراج متن از فیلدهای صحیح
# answer_text = response.answer
# justification_text = response.justification

# # ۲. تمیزکاری و جایگزینی '\\n' با خط جدید واقعی
# # (ممکن است مدل هنوز '\\n' متنی تولید کند)
# clean_justification = justification_text.replace('\\n', '\n')

# # ۳. چاپ خروجی به صورت مرتب
# print("--- Structured Output ---")
# print(f"✅ Answer: {answer_text}")
# print("\n📖 Justification:")
# print(clean_justification)
print ("\n")
print(response)
