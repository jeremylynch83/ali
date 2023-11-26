import os
import subprocess

# First create separate md files from the main master md file

def create_md_files_from_headings(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return

    with open(file_path, 'r') as file:
        content = file.read()

    # Split the content by lines and initialize variables
    lines = content.splitlines()
    current_heading = None
    current_text = []

    for line in lines:
        if line.startswith('#'):
            # Write the previous section to a file if there is one
            if current_heading is not None:
                write_to_file(current_heading, current_text)

            # Start a new section
            current_heading = line[1:].strip().replace(' ', '_') + '.md'
            current_text = [line]
        else:
            current_text.append(line)

    # Write the last section to a file
    if current_heading is not None:
        write_to_file(current_heading, current_text)

def write_to_file(filename, text_lines):
    with open(filename, 'w') as file:
        file.write('\n\n'.join(text_lines))
    print(f"Created file: {filename}")

# Replace 'master.txt' with the path to the actual file
create_md_files_from_headings('master.txt')

# Now compile all the md files to html

# Path to the Pandoc template
template_path = "templates/standard.html"

# Directory containing the markdown files
md_directory = os.getcwd()

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

