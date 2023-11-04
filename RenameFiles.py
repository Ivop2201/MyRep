import os
import sys

def replace_slashes(file_path):
    return file_path.replace('\\','/')

file_path = replace_slashes('H:\Claudio\Pagos e Impuestos\ABL/2022')

os.chdir(file_path)
file_list = os.listdir()

while True:
    for item in file_list:
        file_name = item

        if file_name[:3] == "Rec":
            #print(file_name)
            new_name= "ABL Comprobante 2022_" + file_name [11:13] + ".pdf"
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
