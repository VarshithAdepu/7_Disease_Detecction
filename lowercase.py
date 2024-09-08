# Define input and output file paths
input_file_path = 'train.clean.pp.dedup.norm.en'
output_file_path = 'output.txt'

# Open the input file and read its content
with open(input_file_path, 'r') as file:
    content = file.read()

# Convert the content to lowercase
lowercase_content = content.lower()

# Write the lowercase content to the output file
with open(output_file_path, 'w') as file:
    file.write(lowercase_content)

print(f"Text from {input_file_path} has been converted to lowercase and saved to {output_file_path}.")
