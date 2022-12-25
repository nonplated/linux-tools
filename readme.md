
# Why?
To have a compiled+ready+simple+fast+universal tool without any additional requirements.

# For who?
For linux users.

# Install
```bash
mkdir linux-tools
clone https://github.com/nonplated/linux-tools .
```
or just copy `./dist/*`

# Usage
From directory where exists `any_file.csv`
```bash
./linux-tools/dist/csv2xlsx/csv2xlsx any_file.csv
```
Run without any arguments to see more options in console: 
```bash
./linux-tools/dist/csv2xlsx/csv2xlsx
```

# Compile new or modified tool
All sources are in `./src`, compiled scripts in `./dist`

Use virtual environment (not used here for clarify)

From `./linux-tools`
```bash
python3 install -U pyinstaller
pyinstaller --hidden-import xlsxwriter ./src/csv2xlsx.py
```
Compiled app will appear in `./linux-tools/dist/csv2xlsx` dir.


# Available tools
Name | Function
--- | ---
csv2xlsx | Converter from CSV to XLSX format
