try:
    with open("sample.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
 print("File not found")

 print("Error: The file 'sample.txt' does not exist'")

except Exception as a:
    print(f"An unexpected error occurred:{a}")