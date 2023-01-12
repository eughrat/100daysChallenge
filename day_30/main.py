# with open('a_file.txt') as file:
#     file.read()

# try:
#     file = open("a_file.txt")
#     a = {"key": "value"}
#     print(a["cos"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
# except KeyError as error_message:
#     print(f"the key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     raise TypeError("What the fck")


weight = float(input("enter weight: "))
height = float(input("enter height: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)