student = {"Aashish" : 89,"Ranjan" : 76,"Raj":92,
           "Ravi":81, "Monu":67}

name=input("Enter the student's name:")
if name in student:
    print(f"{name}'s marks :{student[name]}")

else:
    print(f"student {name} not found in the record.")