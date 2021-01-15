'''With this method you will be able to add info to the file'''
'''and close it automatically'''

with open ("textfile.txt", "a+") as data:
    data.write('\nFourth line added by Python')
