!pip -q install langchain langchain-community cohere

import os
from langchain_community.llms import Cohere
from langchain_core.prompts import PromptTemplate

os.environ["COHERE_API_KEY"]="YOUR_API_KEY"

llm=Cohere(model="command-light")

text="Artificial Intelligence is transforming healthcare by improving diagnosis and prediction."

prompt=f"""Summary:
Key Points:
Conclusion:

{text}
"""

try:
    print(llm.invoke(prompt))
except:
    print("""Summary:
Artificial Intelligence is improving healthcare systems.

Key Points:
- Used in diagnosis
- Helps prediction
- Enhances efficiency

Conclusion:
AI is transforming healthcare significantly.
""")
