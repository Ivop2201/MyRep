#This code allows you to quickly rename files with similar names in a specific folder

import os
import sys

#Use this line to enther the path to the folder
file_path = replace_slashes('C:/User/Folder...')


os.chdir(file_path)
file_list = os.listdir()

while True:
    for item in file_list:
        file_name = item
        if file_name[:4] == "Name": #Here you can specify the characters and in which part of the file name they are
            new_name = "New name 2022_" + file_name [11:13] + ".pdf"  
            while True:
                answer = input(f'\nFile {file_name} will be renamed to: {new_name}.\n(Press enter to rename the file) or (Enter 0 to skip this file) or (Enter q to exit program)')
                if answer == '':
                    print('File name updated\n')
                    os.rename(file_name,new_name)
                    break
                elif answer == '0':
                    print('File skiped\n')
                    break
                elif answer == 'q':
                    sys.exit()              
    break
