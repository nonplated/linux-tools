#!/usr/bin/env python3
# from abcmeta import ABC, abstractmethod # https://pypi.org/project/abcmeta/
import glob
import sys
import os
from Converter import Converter


if __name__ == '__main__':

    # Get arguments / Usage
    if len(sys.argv)==2: 
        # files_to_convert = glob.glob(os.path.join('.', '*.csv'))
        files_to_convert = glob.glob(os.path.join('.', sys.argv[1]))
        if (len(files_to_convert)==0): 
            sys.exit(f'No files matching the pattern were found: %s' % os.path.join('.', sys.argv[1]))
    elif (len(sys.argv)>=2):
        files_to_convert = sys.argv[1:]
    else:
        print('csv2xlsx -- convert CSV files to XLSX format // 2022 // MD')
        print('Usage: ')
        print('        ./csv2xlsx filename1.csv [filename2.csv] ...')
        print('        ./csv2xlsx *.csv     -- convert all files from current dir according to the pattern *.csv')
        sys.exit()


    # Convert all specified files
    try:
        for input_filename in files_to_convert:
            _, input_extension = os.path.splitext(input_filename)
            output_filename = input_filename[:-len(input_extension)] + '.xlsx'
            if (input_extension!='.csv'): 
                print(f'".csv" extension is required, found: "%s". File ignored: %s' % (input_extension, input_filename) )
            else:
                print(f'Converting %s to %s ... ' % (input_filename, output_filename), end='')
                (Converter(input_filename, output_filename)).convert('csv2xlsx')
                print(f'OK')
    except Exception as err: 
        print(f'')    
        print('An exception occurred: ' + str(err))

