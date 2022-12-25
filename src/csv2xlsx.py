#!/usr/bin/env python3
# from abcmeta import ABC, abstractmethod # https://pypi.org/project/abcmeta/
from Converter import Converter
import argparse
# import glob
# import sys
import os

if __name__ == '__main__':

    # Usage
    parser = argparse.ArgumentParser(description='csv2xlsx -- convert CSV files to XLSX format // 2022 // MD')
    parser.add_argument('filename_csv', nargs='+', help="search pattern (csv extension required)")
    args = parser.parse_args()

    # Define files
    files_to_convert = args.filename_csv

    # Convert all specified files
    try:
        for input_filename in files_to_convert:
            input_basename, input_extension = os.path.splitext(input_filename)
            # output_filename = input_filename[:-len(input_extension)] + '.xlsx'
            output_filename = input_basename + '.xlsx'
            if (input_extension!='.csv'): 
                print(f'".csv" extension is required, found: "%s". File ignored: %s' % (input_extension, input_filename) )
            else:
                print(f'Converting %s to %s ... ' % (input_filename, output_filename), end='')
                (Converter(input_filename)).convert_to('xlsx', output_filename)
                print(f'OK')
    except Exception as err: 
        print(f'')    
        print('An exception occurred: ' + str(err))

