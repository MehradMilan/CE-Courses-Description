# CE Courses Description

## What is this repository for?
Some European universities require a description of the courses that the student has taken in order to validate the credits.

This repository contains the description of the courses that are part of the **Computer Engineering** degree at the `Sharif University of Technology`.

## How to use this repository?
The repository is organized in the following way:

+ Each course description is a separate markdown file located in the `Courses` directory.
+ The `converter.py` file is used to convert the markdown files to a `PDF` file.

### Running the converter
To convert the markdown files to a PDF, use the following command:

```bash
python3 converter.py -o [output.pdf] -i [input1] [input2] ...
```

Where:
- `[output.pdf]` is the name of the output PDF file (required).
- `[input1]`, `[input2]`, ... are the names of the input files or directories containing markdown files (required). You can provide multiple files and directories.

### Options:
- `-o` / `--output`: Specify the output PDF file (e.g., `Description.pdf`).
- `-i` / `--input`: Specify one or more input files or directories containing markdown files. This can be multiple files and directories.
- `-b` / `--page-break`: If you want to add page breaks after each markdown file, use this flag.

### Example usage:
1. **Convert a single markdown file to PDF:**
   ```
   python3 converter.py -o Description.pdf -i Courses/40441-Data_and_Network_Security.md
   ```

2. **Convert multiple markdown files and directories to a PDF with page breaks:**
   ```
   python3 converter.py -b -o Description.pdf -i Intro.md /Courses
   ```

## Requirements
To run the `converter.py` script, you need to install the following dependencies:

1. **`wkhtmltopdf`**: A tool required by `pdfkit` to generate PDFs from HTML.
   Install it using the following command:
   ```
   apt install wkhtmltopdf
   ```

2. **Python packages**: Install required Python packages using `pip`:
   ```
   pip install markdown pdfkit
   ```

## How to contribute?
To contribute to this repository, you can:
- Add a new course description:
  + Use the `Template.md` file as a template.
- Update or fix an existing course description.
