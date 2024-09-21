file = open('tekst.txt','r+')
#print(file.read())

for line in file:  #reading line by line
    print(line, end='')

file.write("\nDodaje kolejną linie z pythona")

file.close()


with open('tekst.txt','rb') as file1:
    content = file1.readlines()
    print(content)


