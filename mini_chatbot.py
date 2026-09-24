from ollama import chat 
print("WELCOME MINNU !!! HOPING TO HAVE A GREAT CONVERSATION....")
system_msg = "you are a analyst,answer like a analyst,in just one line "

while True:
    question= input("Ask a question")
    if question == "":
        print("MINNU:Please type something!!!")
    if question.lower().strip() == "exit":
        print("minnu: See you soon minnu...please come back soon!🤧🤧🤧")
        break
    try:
        response = chat(
            model = "llama3.2",
            messages = [
                {
                    "role": "user",
                    "content": question
                },
                {
                    "role" : "system",
                    "content" : system_msg
                }
            ]
        )
        print(f"minnu:{response['message']['content']}")
    except Exception as e:
        print("unknown issue. Is ollama running?")