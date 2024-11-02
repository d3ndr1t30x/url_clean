def remove_non_urls(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Strip leading/trailing whitespace and check if the line starts with 'http://' or 'https://'
            line = line.strip()
            if line.startswith('http://') or line.startswith('https://'):
                outfile.write(line + '\n')

if __name__ == '__main__':
    input_file = input("Enter the path to the input .txt file: ")
    output_file = input("Enter the path for the output .txt file: ")
    remove_non_urls(input_file, output_file)
    print(f"Non-URL lines have been removed. Cleaned file saved as {output_file}")
