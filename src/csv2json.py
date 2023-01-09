#!/usr/bin/env python3
from Converter import Converter
import argparse

if __name__ == '__main__':

    # Usage
    parser = argparse.ArgumentParser(description='csv2json -- convert CSV files to JSON format // 2023 // MD')
    parser.add_argument('filename_csv', nargs='+', help="search pattern (csv extension required)")
    args = parser.parse_args()

    # Define files
    files_to_convert = args.filename_csv

    # Convert all specified files
    try:
        for input_filename in files_to_convert:
            c = Converter(input_filename)
            output_filename = c.get_output_filename('json')
            if (c.get_input_extension()=='.csv'): 
                print(f'Converting %s to %s ... ' % (input_filename, output_filename), end='')
                c.convert_to('json', output_filename)
                print(f'OK')
            else:
                print(f'".csv" extension is required, found: "%s". File ignored: %s' % (c.get_input_extension(), input_filename) )
    except Exception as err: 
        print(f'')    
        print('An exception occurred: ' + str(err))
