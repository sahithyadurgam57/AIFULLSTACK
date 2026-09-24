from ollama import chat
roles=[
    "You are a strict math teacher. Answer briskly and within 1 line",
    "You are movie director. Answer in a filmy way.one line answer.",
    "You are a lawyer. Answer professionally.one line answer."
]
for role in roles:
    response=chat(
        model="llam3.2",
        messages=[
            {
                "role" : "system",
                "content" : role
            },
            {
                "role" : "user",
                "content" : "How many colours in the rainbow?"
                
            }
        ]
    )
    print(f"---{role} ---")
    print(response.message.content)
    print()