
# 👨🏻‍🎓 Why?
To have a compiled+ready+simple+fast+universal+trusted tool without any additional requirements.

# 👶 For who?
For linux users.

# 📚 Available tools
Name | Function
--- | ---
csv2xlsx | Convert CSV to XLSX format

# 💄 Structure 
Dir | Description
--- | ---
`./src/` | Source code
`./dist/` | Compiled binaries

# 👷🏽 Install
```bash
mkdir linux-tools
clone https://github.com/nonplated/linux-tools .
```
or just copy all `./dist/*` or selected subdir

# 🔧 Usage
From directory where exists `any_file.csv`
```bash
./linux-tools/dist/csv2xlsx/csv2xlsx any_file.csv
```
Run without any arguments to see more options in console: 
```bash
./linux-tools/dist/csv2xlsx/csv2xlsx
```

# ✂️ Compile new or modified tool
Use virtual environment (not used here for readability)

From `./linux-tools` install `pyinstaller` (if not exists) and then compile .py source file to binary linux format.
```bash
python3 install -U pyinstaller
pyinstaller --hidden-import xlsxwriter ./src/csv2xlsx.py
```
Compiled script will appear in `./linux-tools/dist/csv2xlsx` dir.


