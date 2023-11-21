import os
import subprocess

# Path to the Pandoc template
template_path = "templates/standard.html"

# Directory containing the markdown files
md_directory = "md"

# Get all markdown files in the specified directory
markdown_files = [f for f in os.listdir(md_directory) if f.endswith('.md')]

# Convert each markdown file to HTML
for md_file in markdown_files:
    # Full path to the markdown file
    full_md_path = os.path.join(md_directory, md_file)

    # Name for the HTML file (saved in the current directory)
    html_file = md_file.replace('.md', '.html')

    subprocess.run(["pandoc", full_md_path, "-o", html_file, "--template", template_path], check=True)

# Output message
print("Markdown files have been successfully converted to HTML.")

