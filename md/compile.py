import os

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

