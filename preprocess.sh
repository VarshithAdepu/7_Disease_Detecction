#!/bin/bash

# Check if train folder is passed as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <FOLDER>"
    exit 1
fi

# Set variables for folder and file paths
FOLDER=$1
TRAIN_EN="$FOLDER/$FOLDER.en"
TRAIN_NE="$FOLDER/$FOLDER.ne"
CLEAN_EN="$FOLDER/$FOLDER.clean.en"
CLEAN_NE="$FOLDER/$FOLDER.clean.ne"
CLEAN_PP_EN="$FOLDER/$FOLDER.clean.pp.en"
CLEAN_PP_NE="$FOLDER/$FOLDER.clean.pp.ne"
DEDUP_EN="$FOLDER/$FOLDER.clean.pp.dedup.en"
DEDUP_NE="$FOLDER/$FOLDER.clean.pp.dedup.ne"
NORM_EN="$FOLDER/$FOLDER.clean.pp.dedup.norm.en"
NORM_NE="$FOLDER/$FOLDER.clean.pp.dedup.norm.ne"
TOKENIZED_EN="$FOLDER/tokenized_eng_sent.txt"
TOKENIZED_NE="$FOLDER/tokenized_nep_sent.txt"
CODES_EN="codes.en"
CODES_NE="codes.ne"
BPE_EN="$FOLDER/$FOLDER.bpe.en"
BPE_NE="$FOLDER/$FOLDER.bpe.ne"

# Step 1: Cleaning and Filtering
echo "Cleaning and filtering data..."
./clean-corpus-n.perl -max-word-length 50 $FOLDER/$FOLDER en ne $FOLDER/$FOLDER.clean 0 150

# echo "Building preprocessing tools..."
# git clone https://github.com/kpu/preprocess.git
# cd preprocess
# mkdir build
# cd build
# cmake ..
# make -j4
# cd ../../

echo "Applying simple cleaning..."
preprocess/build/bin/simple_cleaning -p $CLEAN_EN $CLEAN_NE $CLEAN_PP_EN $CLEAN_PP_NE

echo "Removing duplicates..."
preprocess/build/bin/dedupe -p $CLEAN_PP_EN $CLEAN_PP_NE $DEDUP_EN $DEDUP_NE

# Step 2: Normalization
echo "Normalizing data..."
# pip install sacremoses
sacremoses normalize < $DEDUP_EN > $NORM_EN
sacremoses normalize < $DEDUP_NE > $NORM_NE

# Step 3: Tokenization
echo "Tokenizing data..."
python3 tokenizer_en_ne.py $NORM_EN $NORM_NE $TOKENIZED_EN $TOKENIZED_NE

# Step 4: Byte Pair Encoding (BPE)
# Check if 'train' argument is provided
if [[ $FOLDER == "train" ]]; then
    echo "Learning and applying BPE..."
    subword-nmt learn-bpe -s 8000 < $TOKENIZED_EN > $CODES_EN
    subword-nmt apply-bpe -c $CODES_EN < $TOKENIZED_EN > $BPE_EN
    
    subword-nmt learn-bpe -s 8000 < $TOKENIZED_NE > $CODES_NE
    subword-nmt apply-bpe -c $CODES_NE < $TOKENIZED_NE > $BPE_NE
else
    echo "Applying BPE using pre-existing codes..."
    subword-nmt apply-bpe -c $CODES_EN < $TOKENIZED_EN > $BPE_EN
    subword-nmt apply-bpe -c $CODES_NE < $TOKENIZED_NE > $BPE_NE
fi  # <-- Add this fi to close the if block
echo "All steps completed successfully!"
