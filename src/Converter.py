#!/usr/bin/env python3
import xlsxwriter
import csv
import os

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
            'xlsx' : ConverterCSV2XLSX(self.input_filename, self.output_filename)
        }
        return switch.get(convert_type)._convert(options)
        