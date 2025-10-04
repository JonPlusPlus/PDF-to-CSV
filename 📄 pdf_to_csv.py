import pdfplumber
import pandas as pd
import os

def pdf_to_csv(pdf_path, csv_path):
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return

    all_tables = []

    with pdfplumber.open(pdf_path) as pdf:
        print(f"Opened PDF: {pdf_path}")
        for i, page in enumerate(pdf.pages):
            print(f"Processing page {i + 1}/{len(pdf.pages)}")
            tables = page.extract_tables()
            for table in tables:
                if table:
                    df = pd.DataFrame(table)
                    all_tables.append(df)

    if not all_tables:
        print("No tables found in the PDF.")
        return

    # Combine all tables vertically (stacked)
    combined_df = pd.concat(all_tables, ignore_index=True)

    # Save to CSV
    combined_df.to_csv(csv_path, index=False, header=False)
    print(f"CSV saved to: {csv_path}")

# Example usage
if __name__ == "__main__":
    pdf_path = "sample.pdf"      # Replace with your PDF file
    csv_path = "output.csv"      # Output CSV file
    pdf_to_csv(pdf_path, csv_path)
