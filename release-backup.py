


try:
    file = open('newfile.txt','x')
    file.write('hello there!\n')
    file.close()
except FileExistsError:
    with open('newfile.txt', 'a+') as file:
        file.write("I am adding another line!!!")
        file.close()
