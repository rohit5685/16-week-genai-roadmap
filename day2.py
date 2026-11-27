def classify(num):
    if(num<0 or num>1):
        return "INVALID"
    elif(num>=0.8):
        return "AUTO"
    elif(num>=0.5):
        return "REVIEW"
    else:
        return "REJECT"
for s in [0.8,0.5,0.4,0,1,4,0.3,0.8]:
    print(classify(s))