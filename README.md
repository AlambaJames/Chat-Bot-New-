# Chat-Bot-New-

### 📝 Code Summary & Explanation

This script creates an interactive, command-line AI chatbot using the **LangChain** framework and **Google's Gemini 2.5 Flash** model. It runs in a continuous loop, taking user text from the terminal, sending it to Google's cloud servers, and printing out the AI's response.

* * *

### 🔍 Line-by-Line Breakdown

python

    import os
    

Use code with caution.

*   **What it does**: Imports Python's built-in operating system module.
*   **Why it's there**: It allows the script to navigate your laptop's folders so it can locate the `.env` file sitting outside in the parent directory.

python

    from dotenv import load_dotenv
    

Use code with caution.

*   **What it does**: Imports the `load_dotenv` function from the `python-dotenv` package.
*   **Why it's there**: It reads your `.env` file and securely loads your secret `GOOGLE_API_KEY` into your computer's temporary background memory.

python

    from langchain_core.output_parsers import StrOutputParser
    

Use code with caution.

*   **What it does**: Imports a utility that cleans up raw AI responses.
*   **Why it's there**: By default, the AI sends back a massive data object filled with metadata. This parser strips away everything else and extracts *only* the raw text message.

python

    from langchain_core.prompts import ChatPromptTemplate
    

Use code with caution.

*   **What it does**: Imports LangChain's system for structuring AI instructions.
*   **Why it's there**: It sets up the rules, roles, and guidelines for how the chatbot must behave before the conversation even begins.

python

    from langchain_google_genai import ChatGoogleGenerativeAI
    

Use code with caution.

*   **What it does**: Imports the official Google Gemini connector for LangChain.
*   **Why it's there**: It acts as the bridge that connects your local Python script directly to Google's cloud-hosted brain over the internet.

python

    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../.env"))
    

Use code with caution.

*   **What it does**: Looks exactly one folder level higher (`../`) to find your `.env` file and reads it.
*   **Why it's there**: This prevents the script from crashing due to a "missing API key" error, ensuring both of your separate subfolders can share the exact same key file.

python

    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
    

Use code with caution.

*   **What it does**: Configures and initializes your AI engine.
*   **Why it's there**: It specifies that you are using the lightning-fast, free `gemini-2.5-flash` model. The `temperature=0.7` setting controls the balance between random creativity and logical strictness.

python

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful, friendly, and concise AI coding assistant."),
            ("human", "{user_input}"),
        ]
    )
    

Use code with caution.

*   **What it does**: Establishes the template context for the AI.
*   **Why it's there**: The `"system"` line hardcodes the AI's persona so it knows its job. The `"human"` line creates a dynamic placeholder (`{user_input}`) where your actual typed text will be inserted.

python

    chain = prompt | llm | StrOutputParser()
    

Use code with caution.

*   **What it does**: Combines your components into a single workflow using LangChain's pipeline (`|`) operator.
*   **Why it's there**: It links everything together in a set order: **User Input** ➡️ goes into the **Prompt Template** ➡️ gets processed by the **Gemini LLM** ➡️ gets cleaned up by the **String Output Parser**.

python

    print("\n🎉 Chatbot is ready! Type 'exit' or 'quit' to stop.\n")
    

Use code with caution.

*   **What it does**: Prints a simple welcome message in your VS Code terminal.
*   **Why it's there**: Visual feedback to let you know the environment setup worked perfectly and the script is fully loaded.

python

    while True:
    

Use code with caution.

*   **What it does**: Starts an infinite, continuous loop.
*   **Why it's there**: This is what actually turns the script into a "chatbot." Without this loop, the script would run your message once and immediately shut down.

python

        user_message = input("You: ")
    

Use code with caution.

*   **What it does**: Pauses the program execution and waits for you to type something into the terminal.
*   **Why it's there**: Captures your real-time text input and stores it inside the variable `user_message`.

python

        if user_message.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
    

Use code with caution.

*   **What it does**: Monitors your text for the kill phrases "exit" or "quit".
*   **Why it's there**: It safely exits the infinite loop (`break`) and shuts down the script when you are finished chatting.

python

        if not user_message.strip():
            continue
    

Use code with caution.

*   **What it does**: Checks if you accidentally hit Enter without typing anything.
*   **Why it's there**: Bypasses empty inputs (`continue` skips to the next turn) so you don't waste your daily free API calls on blank messages.

python

        try:
            print("AI is thinking...")
            response = chain.invoke({"user_input": user_message})
            print(f"\nAI: {response}\n")
    

Use code with caution.

*   **What it does**: Executes the AI pipeline and displays the output.
*   **Why it's there**: `chain.invoke` sends your message into the pipeline, securely waits for Gemini to process it in the cloud, receives the response text, and prints it out nicely in the terminal.

python

        except Exception as e:
            print(f"\n❌ Error: {e}")
    

Use code with caution.

*   **What it does**: A safety net for unexpected crashes.
*   **Why it's there**: If your internet drops out or your API key stops working, this prevents Python from throwing an ugly system crash. Instead, it gently prints out the exact error message so you can fix it.
