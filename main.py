import os
import sys
import csv

def get_folders(folder, maximum_size):
    '''gets the folders that exceed a selected size 
       and prints it in the console and in a txt file'''
    
    #creates the txt file for the data
    with open(f'{os.path.dirname(__file__)}\\data.txt', 'w') as txt_file:
        data = txt_file.read()
        #look for all the folders and files in the selected folder
        for root, dirs, files in os.walk(folder):
            folder_size = 0
            #gets the size of the folder
            for file in files:
                try:
                    folder_size += os.path.getsize(f'{root}\\{file}')
                except:
                    print(f'An error ocurred measuring this file:\n {root}\\{file}')
            #converts the folder size from bytes to megabytes
            folder_size_MB = '{:.2f} MB'.format(folder_size / 1048576)
            #prints the folders that exceed the selected size
            if folder_size > maximum_size:
                print(root, folder_size_MB)
                #prints the data in a csv file
                data.writerow([f'Folder path: \'{root}\' || Size: {folder_size_MB} MB'])

#TODO: sort folders according to their size

def main(argv):
    maximum_size = int(input('Maximum size in MB: ')) * 1048576
    folder = input('Folder: ')
    get_folders(folder, maximum_size)
    
if __name__ == "__main__":
    main(sys.argv)
