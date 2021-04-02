# append_text = "\nthis is append file"
# print(append_text)
#
# my_file = open('my file.txt','a')
# my_file.write(append_text)
# my_file.close()

file = open('my file.txt','r')
# content = file.readline()
# second_red_line = file.readline()
# print(content)
# print(second_red_line)
content = file.readlines()
print(content)