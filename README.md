# 🪓 PDF Splitter & Page Deleter

A simple Python script that can:

1. **Split large PDFs** into smaller PDFs (default: 30 pages per file).
2. **Delete selected pages** from a PDF.

For example:

* **Splitter**: A 60-page PDF can be split into two 30-page files.
* **Deleter**: User input `1-10, 15-17` will remove those pages from the PDF.

---

## 🚀 Features

### PDF Splitter

* Splits any PDF into chunks of **custom page length** (default: 30).
* Automatically names output files (`_part1`, `_part2`, etc.).
* Saves the new PDFs in the **same directory** as the original file.
* Supports long file names and complex paths (e.g., `C:\Users\...`).

### PDF Deleter

* Deletes **selected pages** from a PDF based on user input.
* Automatically names output files (`[file name]_updated.pdf`).
* Saves the new PDFs in the **same directory** as the original file.
* Supports long file names and complex paths (e.g., `C:\Users\...`).

---

## 🧠 How It Works

The script uses the **PyPDF2** library to:

1. Read the input PDF.
2. Count the total number of pages.
3. Split the PDF into smaller files (for the splitter) or remove selected pages (for the deleter).
4. Save the resulting PDFs in the same folder as the original file.

---

## 🛠️ Requirements

Make sure you have **Python 3.7+** installed and install the required library:

```bash
pip install PyPDF2
```

---

## 🧩 Usage

1. Clone or download this repository.
2. Place your PDF file in a convenient folder.
3. Run the relevant script. E.g.,

```bash
python PDFsplitter.py
```

4. When prompted:

   * **For splitting**: Enter the full path to your PDF.
   * **For deleting pages**: Enter the full path to your PDF and the pages to delete in a format like `1-10, 15, 18-20`.

---

### 🗂 Example Output

#### Splitter

If your PDF has 65 pages and you split by 30 pages:

```
myfile_part1.pdf  (pages 1–30)
myfile_part2.pdf  (pages 31–60)
myfile_part3.pdf  (pages 61–65)
```

#### Deleter

If you delete pages `1-10, 15, 18-20` from a PDF called `myfile.pdf`:

```
myfile_updated.pdf  (all pages except 1-10, 15, 18-20)
```

---

### ⚡ Notes

* PDF pages are **1-indexed** when entering ranges.
* Make sure your input format for deleting pages is **comma-separated** with optional ranges (`start-end`).
* The original PDF **is not modified**; a new PDF is created.
