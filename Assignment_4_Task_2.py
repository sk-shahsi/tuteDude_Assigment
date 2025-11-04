user_input = input("Enter text to write to the file:")
with open("output.txt",'w') as file:
    file.write(user_input+"\n")
print("Data successfully written to output.txt.")

extra_dat = input("Enter additional text to append:")
with open("output.txt","a") as file:
    file.write(user_input + "\n")
print("data successfully append.")

print("\nFinal content of output.txt:")
with open("output.txt","r") as file:
    contant = file.read()
    print(contant)