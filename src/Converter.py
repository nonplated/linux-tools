#!/usr/bin/env python3
import xlsxwriter
import csv
import os
import json

class ConverterCSV2XLSX:

    def __init__(self, input_filename: str, output_filename: str):
        self.input_filename = input_filename
        self.output_filename = output_filename

    def _convert(self, options: dict = {}) -> bool:
        try:
            workbook = xlsxwriter.Workbook(self.output_filename)
            worksheet = workbook.add_worksheet()
            with open(self.input_filename, 'rt', encoding='utf8') as f:
                reader = csv.reader(f)
                for r, row in enumerate(reader):
                    for c, col in enumerate(row):
                        worksheet.write(r, c, col)
            workbook.close()
        except Exception as err:
            print(str(err))
            return False
        return True        


class ConverterCSV2JSON:

    def __init__(self, input_filename: str, output_filename: str):
        self.input_filename = input_filename
        self.output_filename = output_filename

    def _convert(self, options: dict = {}) -> bool:
        try:
            # Open the CSV file and read the contents into a list
            with open(self.input_filename, 'r') as f:
                reader = csv.DictReader(f)
                rows = list(reader)

            # Write the JSON file
            with open(self.output_filename, 'w') as f:
                json.dump(rows, f)             
            # output_json = []
            # with open(self.input_filename, 'rt', encoding='utf8') as f:
            #     reader = csv.reader(f)    
            #     row_nr = 0     
            #     header = []
            #     for r, row in enumerate(reader):
            #         if (row_nr==0):
            #             # for c, col in enumerate(row):
            #             #     header.append(col)
            #             header = row.copy()
            #         else:
            #             # for c, col in enumerate(row):
            #             output_json.append( dict(zip(header,row)) )
            #         line_nr = line_nr + 1
            #     print(output_json)

        except Exception as err:
            print(str(err))
            return False
        return True        


class Converter:

    def __init__(self, input_filename: str):
        self.input_filename = input_filename

    def get_output_filename(self, convert_type: str) -> str:
        input_basename, input_extension = os.path.splitext(self.input_filename)
        output_filename = input_basename + '.' + convert_type
        return output_filename

    def get_input_extension(self) -> str:
        _, input_extension = os.path.splitext(self.input_filename)
        return input_extension

    def convert_to(self, convert_type: str, output_filename: str = '', options: dict = {}) -> bool:
        self.output_filename = output_filename
        switch = {
            'xlsx' : ConverterCSV2XLSX(self.input_filename, self.output_filename),
            'json' : ConverterCSV2JSON(self.input_filename, self.output_filename),
        }
        return switch.get(convert_type)._convert(options)
        