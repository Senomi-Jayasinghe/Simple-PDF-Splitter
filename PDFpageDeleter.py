import os
from PyPDF2 import PdfReader, PdfWriter

def parse_page_ranges(page_input):
    pages_to_delete = set()
    parts = [p.strip() for p in page_input.split(',')]

    for part in parts:
        if '-' in part:
            start, end = part.split('-')
            start, end = int(start), int(end)
            pages_to_delete.update(range(start, end + 1))
        else:
            pages_to_delete.add(int(part))
    return pages_to_delete


# ---- MAIN PROGRAM ----

pdf_path = input("Enter the path to your PDF file: ").strip('"')
page_input = input("Enter pages to delete (e.g., 1-5, 7, 10-12): ")

# Parse pages
pages_to_delete = parse_page_ranges(page_input)

# PDF reader & writer
reader = PdfReader(pdf_path)
writer = PdfWriter()

# PDF pages in PyPDF2 are 0-indexed — adjust
pages_to_delete = {p - 1 for p in pages_to_delete}  

for page_num in range(len(reader.pages)):
    if page_num not in pages_to_delete:
        writer.add_page(reader.pages[page_num])

# Output file path
folder = os.path.dirname(pdf_path)
filename = os.path.basename(pdf_path)
name, ext = os.path.splitext(filename)

output_path = os.path.join(folder, f"{name}_cleaned{ext}")

with open(output_path, "wb") as f:
    writer.write(f)

print(f"Successfully saved cleaned PDF as:\n{output_path}")
