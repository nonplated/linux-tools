
# 👨🏻‍🎓 Why?
To have a standalone compiled+ready+simple+trusted tool without any requirements to run. It can be done with [pyinstaller](https://pyinstaller.org/en/stable/), so you will never see error for missed modules or even python interpreter is not needed.

# 👶 For who?
For linux user, who wants to convert files from bash.

# 📚 Available tools
Name | Function
--- | ---
csv2xlsx | Convert CSV to XLSX format
csv2json | Convert CSV to JSON format

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
```bash
usage: csv2xlsx.py [-h] filename_csv [filename_csv ...]
```
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


