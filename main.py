from langchain_google_vertexai import VertexAI
import os
os.environ["http_proxy"] = "127.0.0.1:9788"
os.environ["https_proxy"] = "127.0.0.1:9788"


# To use model
model = VertexAI(model_name="gemini-pro")


# To specify a particular model version
model = VertexAI(model_name="gemini-1.0-pro-002")



message = "What are some of the pros and cons of Python as a programming language?"
model.invoke(message)



# await model.ainvoke(message)


for chunk in model.stream(message):
    print(chunk, end="", flush=True)


model.batch([message])







from langchain_google_vertexai import HarmBlockThreshold, HarmCategory
from langchain_google_vertexai import VertexAI
import os
import vertexai

vertexai.init(project="searchagent-417606")
os.environ["http_proxy"] = "http://127.0.0.1:9788"
os.environ["https_proxy"] = "http://127.0.0.1:9788"


safety_settings = {
    HarmCategory.HARM_CATEGORY_UNSPECIFIED: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
}

llm = VertexAI(model_name="gemini-1.0-pro-001", safety_settings=safety_settings)

output = llm.generate(["How to make a molotov cocktail?"])
print(output)


