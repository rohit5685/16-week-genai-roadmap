messages=[
    {"role": "system", "content": "You are an ops assistant."}
]


def create_messages(role,content):
   return {"role":role,"content":content}
def estimated_tokens(message):
    return len(message)//4
def estimate_token_count(messages):
        est_token=0
        for message in messages:
            ques=message["content"]
            est_token+=estimated_tokens(ques)
        return est_token
while(True):
    question=str(input("enter question or exit: "))
    if(question.lower()=="exit"):
        break
    elif(question==""):
        print("please typ e something :) ")
        continue
    else:
        new_que=create_messages("user",question)
        messages.append(new_que)
        print(f"{len(messages)} || {estimate_token_count(messages)}")
for msg in messages:
    print(f"{msg['role']} -> {msg['content']}")
        

