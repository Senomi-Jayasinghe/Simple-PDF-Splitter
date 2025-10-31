from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf, pages_per_split=30):
    reader = PdfReader(input_pdf)
    total_pages = len(reader.pages)
    num_parts = (total_pages + pages_per_split - 1) // pages_per_split  # round up

    print(f"Total pages: {total_pages}")
    print(f"Splitting into {num_parts} part(s) of {pages_per_split} pages each...")

    for i in range(num_parts):
        writer = PdfWriter()
        start_page = i * pages_per_split
        end_page = min(start_page + pages_per_split, total_pages)

        for j in range(start_page, end_page):
            writer.add_page(reader.pages[j])

        output_filename = f"{input_pdf.replace('.pdf', '')}_part{i+1}.pdf"
        with open(output_filename, "wb") as output_file:
            writer.write(output_file)

        print(f"✅ Created: {output_filename} ({end_page - start_page} pages)")

if __name__ == "__main__":
    input_pdf = input("Enter the path to your PDF file: ").strip()
    split_pdf(input_pdf, pages_per_split=30)
