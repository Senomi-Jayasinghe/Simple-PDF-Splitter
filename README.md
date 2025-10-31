## 🪓 PDF Splitter

A simple Python script that splits a large PDF into smaller PDFs — each containing **30 pages** (or a number you choose).
For example, a 60-page PDF will be split into two 30-page files.

---

### 🚀 Features

* Splits any PDF into chunks of **custom page length** (default: 30).
* Automatically names the output files (`_part1`, `_part2`, etc.).
* Saves the new PDFs in the **same directory** as the original file.
* Supports long file names and complex paths (like `C:\Users\...`).

---

### 🧠 How It Works

The script uses the **PyPDF2** library to:

1. Read the input PDF.
2. Count the total pages.
3. Create smaller PDF files with 30 pages each (or your chosen number).

---

### 🛠️ Requirements

Make sure you have **Python 3.7+** installed and install the required library:

```bash
pip install PyPDF2
```

---

### 🧩 Usage

1. Clone or download this repository.
2. Place your PDF file in a convenient folder.
3. Run the script:

   ```bash
   python PDFsplitter.py
   ```
4. When prompted, type or paste the full path to your PDF (without quotes):

   ```
   C:\Users\admin\Downloads\Lecture 10 - The Layered Architecture of The Computers.pdf
   ```
5. The script will generate:

   ```
   Lecture 10 - The Layered Architecture of The Computers_part1.pdf
   Lecture 10 - The Layered Architecture of The Computers_part2.pdf
   ```

   in the same folder.

---

### 🗂 Example Output

If your PDF has 65 pages, you’ll get:

```
myfile_part1.pdf  (pages 1–30)
myfile_part2.pdf  (pages 31–60)
myfile_part3.pdf  (pages 61–65)
```
