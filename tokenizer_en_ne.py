# from sacremoses import MosesTokenizer
# from indicnlp.tokenize import indic_tokenize

# # Initialize the tokenizers
# english_tokenizer = MosesTokenizer()

# # Function to read sentences from a file
# def read_sentences_from_file(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         sentences = file.readlines()
#     return sentences

# # Function to write tokenized sentences to a file
# def write_tokenized_sentences_to_file(sentences, file_path):
#     with open(file_path, 'w', encoding='utf-8') as file:
#         for sentence in sentences:
#             file.write(sentence + '\n')

# # Tokenize English sentences
# def tokenize_english_sentences(sentences):
#     return [english_tokenizer.tokenize(sentence.strip(), return_str=True) for sentence in sentences]

# # Tokenize Nepali sentences
# def tokenize_nepali_sentences(sentences):
#     return [" ".join(indic_tokenize.trivial_tokenize(sentence.strip())) for sentence in sentences]

# # File paths
# #train
# # english_input_file = 'train.clean.pp.dedup.norm.en'
# # english_output_file = 'tokenized_eng_sent.txt'
# # nepali_input_file = 'train.clean.pp.dedup.norm.ne'
# # nepali_output_file = 'tokenized_nep_sent.txt'

# #valid
# english_input_file = 'admin/test.clean.pp.dedup.norm.en'
# english_output_file = 'admin/tokenized_eng_test.txt'
# nepali_input_file = 'admin/test.clean.pp.dedup.norm.ne'
# nepali_output_file = 'admin/tokenized_nep_test.txt'

# #test
# # english_input_file = 'train.clean.pp.dedup.norm.en'
# # english_output_file = 'tokenized_eng_test.txt'
# # nepali_input_file = 'train.clean.pp.dedup.norm.ne'
# # nepali_output_file = 'tokenized_nep_test.txt'

# # Read and tokenize English sentences
# english_sentences = read_sentences_from_file(english_input_file)
# tokenized_english = tokenize_english_sentences(english_sentences)
# write_tokenized_sentences_to_file(tokenized_english, english_output_file)

# # Read and tokenize Nepali sentences
# nepali_sentences = read_sentences_from_file(nepali_input_file)
# tokenized_nepali = tokenize_nepali_sentences(nepali_sentences)
# write_tokenized_sentences_to_file(tokenized_nepali, nepali_output_file)

# # Print tokenized sentences
# # print("Tokenized English Sentences:")
# # for sentence in tokenized_english:
# #     print(sentence)

# # print("\nTokenized Nepali Sentences:")
# # for sentence in tokenized_nepali:
# #     print(sentence)

import sys
from sacremoses import MosesTokenizer
from indicnlp.tokenize import indic_tokenize

# Initialize the tokenizers
english_tokenizer = MosesTokenizer()

# Function to read sentences from a file
def read_sentences_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        sentences = file.readlines()
    return sentences

# Function to write tokenized sentences to a file
def write_tokenized_sentences_to_file(sentences, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for sentence in sentences:
            file.write(sentence + '\n')

# Tokenize English sentences
def tokenize_english_sentences(sentences):
    return [english_tokenizer.tokenize(sentence.strip(), return_str=True) for sentence in sentences]

# Tokenize Nepali sentences
def tokenize_nepali_sentences(sentences):
    return [" ".join(indic_tokenize.trivial_tokenize(sentence.strip())) for sentence in sentences]

# Main function to handle arguments and perform tokenization
def main():
    if len(sys.argv) != 5:
        print("Usage: python3 script_name.py <english_input_file> <english_output_file> <nepali_input_file> <nepali_output_file>")
        sys.exit(1)
    
    english_input_file = sys.argv[1]
    nepali_input_file = sys.argv[2]
    english_output_file = sys.argv[3]
    nepali_output_file = sys.argv[4]

    # Read and tokenize English sentences
    english_sentences = read_sentences_from_file(english_input_file)
    tokenized_english = tokenize_english_sentences(english_sentences)
    write_tokenized_sentences_to_file(tokenized_english, english_output_file)

    # Read and tokenize Nepali sentences
    nepali_sentences = read_sentences_from_file(nepali_input_file)
    tokenized_nepali = tokenize_nepali_sentences(nepali_sentences)
    write_tokenized_sentences_to_file(tokenized_nepali, nepali_output_file)

    # Print tokenized sentences (optional)
    # print("Tokenized English Sentences:")
    # for sentence in tokenized_english:
    #     print(sentence)

    # print("\nTokenized Nepali Sentences:")
    # for sentence in tokenized_nepali:
    #     print(sentence)

if __name__ == "__main__":
    main()
