# Сrusher

This tool processes a large tab-delimited CSV file (`documents.csv`) and splits it into smaller chunks. Optionally, it can filter rows that contain HTTP/HTTPS links.

---

## 📄 Script: `crusher.py`

### Features:
- Splits the input file into chunks of 100 rows each.
- Optional filtering: keep only rows that contain `http://` or `https://`.
- Writes each chunk to a separate file in the `../new/` directory.
- Preserves the original CSV header in all output files.

---

## 🛠 How It Works

1. **Prompt**  
   Asks the user whether to filter rows by links:
   ```
   Do you want to search for value only with links in the document? (y/n)
   ```

2. **Input**  
   Expects a file named `documents.csv` located in the parent folder (`../`).

3. **Processing**  
   - If filtering is enabled (`y`), keeps only rows with `http://` or `https://`.
   - If disabled (`n`), keeps all rows.
   - Reads the file using a tab (`	`) delimiter.

4. **Output**  
   - Creates a folder `../new/` if it doesn't exist.
   - Saves each chunk in the format:
     ```
     new_doc_0.csv
     new_doc_1.csv
     ...
     ```
   - Each file contains up to 100 rows.

---

## 📁 Folder Structure

```
your_project/
│
├─ tools/
│   └─ csv_splitter.py
│
├─ documents.csv        # input file (tab-separated)
├─ new/                 # auto-created output folder
│   ├─ new_doc_0.csv
│   ├─ new_doc_1.csv
│   └─ ...
```

---

## ▶️ How to Run

Make sure you're in the folder containing `tools/` and `documents.csv`.

Run the script:

```bash
python tools/crusher.py
```

---

## 📝 Notes

- The script uses a 500MB buffer for fast reading of large files.
- Maximum rows per output file: 100
- File delimiter: tab (`\t`)
- Output encoding: UTF-8
- Link detection is done using the regex: `http[s]?://`

