import os
import json
import matplotlib.pyplot as plt

# Define the folder containing the JSON files
folder_path = 'bleu_scores'

# Initialize lists to store file names and BLEU scores
file_data = []

# Iterate over all files in the folder
for file_name in os.listdir(folder_path):
    # Store both file name and BLEU score in a tuple
    file_path = os.path.join(folder_path, file_name)
    
    # Open and read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
        for metric in data:
            if metric['name'] == 'BLEU':
                file_data.append((file_name, metric['score']))
                break

# Sort the file data by file name
file_data.sort(key=lambda x: x[0])

# Unzip the sorted data into file names and BLEU scores
file_names, bleu_scores = zip(*file_data)

# Plot the BLEU scores
print(file_names, bleu_scores)
plt.figure(figsize=(10, 6))
plt.plot(file_names, bleu_scores, marker='o', linestyle='-', color='b')
plt.xticks(rotation=90)
plt.xlabel('File Names')
plt.ylabel('BLEU Score')
plt.title('BLEU Scores from JSON Files')
plt.tight_layout()
plt.show()
