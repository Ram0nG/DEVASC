'''With this method you will be able to open and close the file'''
''' automatically'''

with open("textfile.txt", "r") as data:

    print(data.read())
