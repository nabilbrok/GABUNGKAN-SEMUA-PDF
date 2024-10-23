import tkinter as tk
from tkinter import filedialog, messagebox
import os
import PyPDF2 as pdf

def browse_files():
    # Open file dialog for multiple file selection and store the selected file paths
    filenames = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    if filenames:
        # Extract file names and convert them to a list
        file_names = [os.path.basename(file) for file in filenames]
        # Update the label with the file names
        label.config(text="\n".join(file_names))
        # Enable the merge button
        merge_button.config(state=tk.NORMAL)
        # Store selected file paths for merging
        global selected_files
        selected_files = filenames

def merge_pdfs(pdf_list, output):
    pdf_writer = pdf.PdfWriter()

    for pdf_file in pdf_list:
        pdf_reader = pdf.PdfReader(pdf_file)
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])

    with open(output, 'wb') as out_file:
        pdf_writer.write(out_file)

    # Notify the user that the PDFs have been merged
    messagebox.showinfo("Success", f"PDFs merged into {output}")

def merge_selected_files():
    if selected_files:  # Check if any files are selected
        output_filename = filedialog.asksaveasfilename(defaultextension=".pdf", 
                                                        filetypes=[("PDF files", "*.pdf")])
        if output_filename:
            merge_pdfs(selected_files, output_filename)

# Create the main application window
root = tk.Tk()
root.title("Multiple PDF Merger")
root.geometry("400x300")

# Global variable to hold selected files
selected_files = []

# Create a button to browse files
browse_button = tk.Button(root, text="Browse Files", command=browse_files)
browse_button.pack(pady=20)

# Create a label to display the selected file names
label = tk.Label(root, text="No files selected", justify=tk.LEFT)
label.pack(pady=20)

# Create a button to merge selected files (initially disabled)
merge_button = tk.Button(root, text="Merge PDFs", command=merge_selected_files, state=tk.DISABLED)
merge_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
