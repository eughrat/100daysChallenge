# file = open("my_file.txt")
# contents = file.read()
#
# print(contents)
#
# file.close()

# with open("my_file.txt") as f:
#     content = f.read()
#     print(content)


with open("./my_file.txt", "a") as f:
    f.write("\nnew line")

with open("./new_file.txt", "a") as f:
    f.write("\nnew line")

with open("./inner/some_file.txt", "r") as f:
    content = f.read()
    print(content)

with open("../day_24.txt", "r") as f:
    content = f.read()
    print(content)

