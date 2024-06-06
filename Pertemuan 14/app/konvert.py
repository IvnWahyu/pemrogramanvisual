from fpdf import FPDF

# File names to be combined
file_names = ["dataview.py", "plotdata.py", "stats.py"]

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size = 12)

# Read each file and add its content to the PDF
for file_name in file_names:
    with open(file_name, 'r') as file:
        for line in file:
            pdf.cell(200, 10, txt = line, ln = True, align = 'L')

# Save the PDF with name .pdf
pdf.output("combined_files.pdf")

print("PDF created successfully.")
