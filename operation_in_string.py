#Membership
#in
s="Hello World"
print("o" in s) #true


# not in
print("o" not in s) #false
print("z" not in s) #true



#Comprsion in string
print("python"=="python") #true
print("python "=="python") #false


#Removing spaces in string use strip()
s1="   python  "
print(s1.strip())

print(s1.strip()=="python") #true


#replace
s2="we are learning python"
print(s2) #we are learning python
print(s2.replace("python","java")) #we are learning java


print(s2.replace("e","E")) #wE arE lEarning python
print(s2.replace("e","E",1)) #wE are learning python



#count
s3="hello world"
s4="hello"
print(s3.count(s4)) #1
print(f"occurances of hello is: {s3.count(s4)}") #occurances of hello is: 1
print(f"occurances of o is:{s3.count("o")}") #occurances of o is:2

#cases in python upper/lower/title/captlise

s5=" hello we are learning Python3.11"
print(s5.upper()) #PYTHON

print(s5.lower()) #python

print(s5.title()) # Hello We Are Learning Python3.11

print(s5.capitalize())  #hello we are learning python3.11




