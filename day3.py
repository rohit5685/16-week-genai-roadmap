# Tasks
# From a list of 6 server names, print the first, the last, the last three and all except the first.
# Write trim_history(messages, keep) that returns the system message plus the last keep other messages.
# Write trim_by_tokens(messages, limit) that removes the oldest non-system messages until the total is within limit.

servers=["l2jump.com","aws.com","mac.com","shd.com","rohit.com","zs.com"]



messgage=["sys","nishal","hi","bye"]
def trim_history(messages,keep):
    if((len(messages))<=keep):
        return messages
    
    recent=messages[-keep:]

    return [messages[0]]+recent



def create_message(role, content):
    return {"role": role, "content": content}

messages = [
    create_message("system", "You are an ops assistant."),   # 6 tokens
    create_message("user", "Why is my disk full?"),          # 5 tokens
    create_message("user", "How do I check it?"),            # 4 tokens
    create_message("user", "How can I delete old logs?"),    # 6 tokens
]
def token_count(ques):
    count=len(ques)//4
    return count
def totoal_token_count(messges):
    total_toke_count=0
    for i in messges:
        total_toke_count+=token_count(i["content"])
    return total_toke_count


def trim_by_tokens(messages,limit):
    trimmed_messages=messages.copy()
    while(totoal_token_count(trimmed_messages)>limit and len(trimmed_messages)>1):

        trimmed_messages.pop(1)
    return trimmed_messages
for limit in [50, 20, 12, 5]:
    result = trim_by_tokens(messages, limit)
    print(limit, totoal_token_count(result), [m["content"] for m in result])

print("original length:", len(messages))

    


    

# for limit in [5]:
#     result = trim_by_tokens(messages, limit)
#     print(limit, total_tokens(result), [m["content"] for m in result])