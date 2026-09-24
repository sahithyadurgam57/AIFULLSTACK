from ollama import chart
messages=[
    {"role" : "system", "content" : "Identify sentiment as positive,negative,neutral,neutral. Reply with one word only."},
    {"role": "user", "content": "Great movie"},
    {"role" : "system","content" :"positive"},
    
    
   {"role": "user", "content": "I hate this movie"},
    {"role" : "system","content" :"negative"},
    
    {"role": "user", "content": "This movie is okay"},
    {"role" : "system","content" :"neutral"},
    
    {"role": "user", "content": "This movie is not good but not bad either"},
    {"role" : "system","content" :"neutral"},
    
    {"role" : "user", "content": "Loved the acting but the ending was dull."}
    
]
response=chat(
    model1="llama3.2",
    messages=messages,
)
print(response.message.content)