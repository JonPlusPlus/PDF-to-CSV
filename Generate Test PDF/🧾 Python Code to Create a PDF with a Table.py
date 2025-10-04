from fpdf import FPDF
from fpdf.enums import XPos, YPos

# Create PDF document
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Title
pdf.cell(200, 10, txt="Sample PDF with Table", new_x=XPos.LEFT, new_y=YPos.NEXT, align="C")

# Add some vertical spacing
pdf.cell(0, 10, "", new_x=XPos.LEFT, new_y=YPos.NEXT)

# Table headers and data
headers = ["ID", "Name", "Age", "Department"]
data = [
    [1, "Alice", 30, "HR"],
    [2, "Bob", 24, "Engineering"],
    [3, "Charlie", 29, "Sales"],
    [4, "David", 35, "Marketing"],
]

# Column widths
col_widths = [20, 50, 20, 50]

# Print headers
for i, header in enumerate(headers):
    pdf.cell(col_widths[i], 10, header, border=1, align='C', new_x=XPos.RIGHT, new_y=YPos.TOP)

# Move to next line after headers
pdf.cell(0, 10, "", new_x=XPos.LEFT, new_y=YPos.NEXT)

# Print each row of data
for row in data:
    for i, item in enumerate(row):
        pdf.cell(col_widths[i], 10, str(item), border=1, align='C', new_x=XPos.RIGHT, new_y=YPos.TOP)
    # Move to next line after each row
    pdf.cell(0, 10, "", new_x=XPos.LEFT, new_y=YPos.NEXT)

# Save PDF
pdf.output("sample_table.pdf")
