
# Why?
To have a compiled+ready+simple+fast+universal tool without any additional requirements.

# For who?
For linux users.

# Install
```bash
mkdir linux-tools
clone https://github.com/nonplated/linux-tools .
```

# Usage
From directory where exists `any_file.csv`
```bash
./linux-tools/dist/csv2xls/csv2xls any_file.csv
```
Run without any arguments to see more options in console: 
```bash
./linux-tools/dist/csv2xls/csv2xls
```

# Compile new or modified tool
All sources are in `./src`, compiled scripts in `./dist`

Use virtual environment (not used here for clarify)

From `./linux-tools`
```bash
python3 install -U pyinstaller
pyinstaller --hidden-import xlsxwriter ./src/csv2xls.py
```
Compiled app will appear in `./linux-tools/dist/csv2xls` dir.


