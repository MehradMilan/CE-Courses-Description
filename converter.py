import pdfkit
import os
import markdown
import argparse

def convert_md_to_pdf(output_pdf, paths, p_break=False):
    md_content = ""
    for idx, path in enumerate(paths):
        if os.path.isdir(path):
            for root, _, files in os.walk(path):
                for file in files:
                    if file.endswith(".md"):
                        with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                            md_content += f.read() + "\n\n"
                            if p_break and idx < len(paths) - 1:
                                md_content += "<div style=\"page-break-after: always\"></div>"

        elif os.path.isfile(path) and path.endswith(".md"):
            with open(path, 'r', encoding='utf-8') as f:
                md_content += f.read() + "\n\n"
                if p_break and idx < len(paths) - 1:
                    md_content += "<div style=\"page-break-after: always\"></div>"

    if not md_content:
        print("No Markdown content found in the provided paths.")
        return

    html_content = markdown.markdown(md_content)

    pdfkit.from_string(html_content, output_pdf)
    print(f"PDF created successfully: {output_pdf}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert markdown files to PDF")
    parser.add_argument("-o", "--output", dest="output_pdf", required=True,
                        help="Specify the output PDF file")
    parser.add_argument("-i", "--input", dest="input_paths", required=True, nargs='+',
                        help="Specify input files and directories (required)")
    parser.add_argument("-b", "--page-break", action="store_true", default=False,
                        help="Add page breaks after each Markdown file")

    args = parser.parse_args()

    convert_md_to_pdf(args.output_pdf, args.input_paths, p_break=args.page_break)