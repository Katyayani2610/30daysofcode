#find the first non repeated character
input_str="tattoos"
for char in input_str:
    print(char)
    #input_str.cout  is used when to tell that no of string me charachter  kitne baar aaye hain
    if input_str.count(char)==1:
       
        print("char is:",char )
        break