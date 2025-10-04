from fpdf import FPDF

# Create a simple PDF with a table
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Sample PDF with Table", ln=True, align="C")

# Add some spacing
pdf.ln(10)

# Table headers
headers = ["ID", "Name", "Age", "Department"]
data = [
    [1, "Alice", 30, "HR"],
    [2, "Bob", 24, "Engineering"],
    [3, "Charlie", 29, "Sales"],
    [4, "David", 35, "Marketing"],
]

# Set column widths
col_widths = [20, 50, 20, 50]

# Print headers
for i, header in enumerate(headers):
    pdf.cell(col_widths[i], 10, header, 1, 0, 'C')
pdf.ln()

# Print data rows
for row in data:
    for i, item in enumerate(row):
        pdf.cell(col_widths[i], 10, str(item), 1, 0, 'C')
    pdf.ln()

# Save the PDF
pdf.output("sample_table.pdf")
