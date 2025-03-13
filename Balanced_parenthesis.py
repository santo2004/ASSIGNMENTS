Str = input()
l = len(Str)

stack = []

for i in range(l):
    if Str[i] in "{[(":
        stack.append(Str[i])
    elif Str[i] in "}])" and stack: 
        if ((Str[i] == "}" and stack[-1] == "{") or 
           (Str[i] == "]" and stack[-1] == "[") or 
           (Str[i] == ")" and stack[-1] == "(")):
            stack.pop()
        else:
            print("Not Balanced")
            exit()  

print("Balanced" if not stack else "Not Balanced")