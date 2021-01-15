''' this script call the file that is in the same directory'''
''' and you will be able to view what is in the file'''
readdata = open("textfile.txt", "r")

#This will print the each line in the file
print(readdata.read())


#This will close the file at the end, you will see a better method.
#of Closing the file.
readdata.close()

