import re

print("enter your  postfix expression  below")
text_to_search = input("enter: ")

#pattern = re.compile(r'[a-zA-Z0-9]+_[a-zA-Z0-9]+_[a-zA-Z0-9\+\-\*\/]+_[a-zA-Z0-9\+\-\*\/]+_[a-zA-Z0-9\+\-\*\/]+_[a-zA-Z0-9\+\-\*\/]+_[a-zA-Z0-9\+\-\*\/]+_[a-zA-Z0-9\+\-\*\/]+_[a-zA-Z0-9\+\-\*\/]+_[a-zA-Z0-9\+\-\*\/]+_')

#matches = pattern.finditer(text_to_search)

#for match in matches:
#print(match)


result = re.findall(r'[0-9]+', text_to_search)
print("these are are the numeric constant in postfix expression")
print (result)

print("        " )
print(" ***********************" )

delimiter = re.findall(r'_' , text_to_search)
print("these are are the delimiter in postfix expression")
print (delimiter)

print("        " )
print(" ***********************" )


variables = re.findall(r'[a-zA-Z]+' , text_to_search)
print("these are all the variable  in postfix expression")
print (variables)

print("        " )
print(" ***********************" )

operators = re.findall(r'[\+\-\*\/]+' , text_to_search)
print("these are all the operators in postfix expression")
print (operators)

print("        " )
print(" ***********************" )

decimal = re.findall(r'[\.]+' , text_to_search)
print("these are all the decimals")
print (decimal)

