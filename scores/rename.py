import os

def rename_files_in_order(directory_path):
    # Get a list of all files in the directory
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    
    # Sort the files to ensure they are renamed in a consistent order
    files.sort()

    # Determine the number of digits needed based on the number of files
    num_digits = len(str(len(files)))

    for i, filename in enumerate(files, start=1):
        # Get the file extension
        file_extension = os.path.splitext(filename)[1]

        # Create the new filename with leading zeros
        new_filename = f"{str(i).zfill(num_digits)}{file_extension}"

        # Rename the file
        os.rename(os.path.join(directory_path, filename), os.path.join(directory_path, new_filename))

# Specify the path to the directory containing the files
directory_path = 'bleu_scores'
rename_files_in_order(directory_path)
