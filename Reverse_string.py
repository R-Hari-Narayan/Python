string_in= input("Enter string:")
string_out= ""
for i in range(-1, -len(string_in)-1, -1):
    string_out+= string_in[i]
print(string_out)
