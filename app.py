import os
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Load the .env file from the parent directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../.env"))

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.9)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a creative, poetic, and friendly AI assistant."),
        ("human", "{user_input}"),
    ]
)

chain = prompt | llm | StrOutputParser()
print("\n🎉 Chatbot ONE (Creative) is ready! Type 'exit' to stop.\n")

while True:
    user_message = input("You: ")
    if user_message.lower() in ["exit", "quit"]:
        break
    if not user_message.strip():
        continue
    print("AI is thinking...")
    print(f"\nAI: {chain.invoke({'user_input': user_message})}\n")
