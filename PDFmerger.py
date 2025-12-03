from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_path="merged_output.pdf"):
    merger = PdfMerger()

    for pdf in pdf_list:
        try:
            merger.append(pdf)
            print(f"Added: {pdf}")
        except Exception as e:
            print(f"Error adding {pdf}: {e}")

    merger.write(output_path)
    merger.close()
    print(f"\n✅ Merged PDF saved as: {output_path}")

if __name__ == "__main__":
    print("Enter paths to PDFs you want to merge.")
    print("Enter an empty line to finish.\n")

    files = []
    while True:
        path = input("PDF path: ").strip().strip('"')
        if path == "":
            break
        files.append(path)

    if not files:
        print("No files entered. Exiting.")
    else:
        output_name = input("\nEnter output file name (default merged_output.pdf): ").strip()
        if output_name == "":
            output_name = "merged_output.pdf"
        if not output_name.endswith(".pdf"):
            output_name += ".pdf"

        merge_pdfs(files, output_name)
