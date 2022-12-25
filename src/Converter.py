#!/usr/bin/env python3
import xlsxwriter
import csv


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

    def __init__(self, input_filename: str, output_filename: str):
        self.input_filename = input_filename
        self.output_filename = output_filename

    def convert(self, convert_type: str, options: dict = {}) -> bool:
        switch = {
            'csv2xlsx' : ConverterCSV2XLSX(self.input_filename, self.output_filename)
        }
        return switch.get(convert_type)._convert(options)
        

        