#!/usr/bin/env python3
import xlsxwriter
import glob
import csv
import sys
import os

# Get arguments / Usage
if len(sys.argv)==2: 
    # files_to_convert = glob.glob(os.path.join('.', '*.csv'))
    files_to_convert = glob.glob(os.path.join('.', sys.argv[1]))
    if (len(files_to_convert)==0): 
        sys.exit(f'No files matching the pattern were found: %s' % os.path.join('.', sys.argv[1]))
elif (len(sys.argv)>=2):
    files_to_convert = sys.argv[1:]
else:
    print('csv2xls -- convert CSV files to XLSX format // 2022 // Maciej Dymowski')
    print('Usage: ')
    print('        ./csv2xls filename1.csv [filename2.csv] ...')
    print('        ./csv2xls *.csv     -- convert all files from current dir according to the pattern *.csv')
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
            workbook = xlsxwriter.Workbook(output_filename)
            worksheet = workbook.add_worksheet()
            with open(input_filename, 'rt', encoding='utf8') as f:
                reader = csv.reader(f)
                for r, row in enumerate(reader):
                    for c, col in enumerate(row):
                        worksheet.write(r, c, col)
            workbook.close()
            print(f'OK')
except Exception as err: 
    print(f'')    
    print('An exception occurred: ' + str(err))

