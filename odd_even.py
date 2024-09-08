def extract_even_odd_lines(input_file, even_output_file, odd_output_file):
    with open(input_file, 'r') as infile, \
         open(even_output_file, 'w') as even_outfile, \
         open(odd_output_file, 'w') as odd_outfile:
        
        for i, line in enumerate(infile, start=1):
            if i % 2 == 0:
                even_outfile.write(line)
            else:
                odd_outfile.write(line)

# Example usage
input_file = 'data'
even_output_file = 'even_lines.txt'
odd_output_file = 'odd_lines.txt'

extract_even_odd_lines(input_file, even_output_file, odd_output_file)
