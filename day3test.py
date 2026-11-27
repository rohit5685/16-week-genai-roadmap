messages = [
    {"role": "system", "content": "SYS!"},
    {"role": "user", "content": "Hi!!"},
    {"role": "assistant", "content": "Hello!"},
    {"role": "user", "content": "Explain Docker"},
    {"role": "assistant", "content": "Docker uses containers"}
]

def token_count(question):
    count = len(question)//4
    return count

def est_token_count(messg):
    tkn_count=0
    for ques in messg:
        qs=ques["content"]
        tkn_count+=token_count(qs)
    return tkn_count

print(est_token_count(messages))
