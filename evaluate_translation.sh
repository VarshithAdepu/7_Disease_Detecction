# #!/bin/bash

# if [ $# -ne 1 ]; then
#     echo "usage: $0 GENERATE_PY_OUTPUT OUTPUT_FILE"
#     exit 1
# fi

# GEN=$1

# SYS=$GEN.sys
# REF=$GEN.ref

# if [ $(tail -n 1 $GEN | grep BLEU | wc -l) -ne 1 ]; then
#     echo "not done generating"
#     exit
# fi

# grep ^H $GEN | awk -F '\t' '{print $NF}' | perl -ple 's{(\S)-(\S)}{$1 ##AT##-##AT## $2}g' > $SYS
# grep ^T $GEN | cut -f2- | perl -ple 's{(\S)-(\S)}{$1 ##AT##-##AT## $2}g' > $REF
# fairseq-score --sys $SYS --ref $REF

# # Compute chrF++ score using sacrebleu
# sacrebleu $REF -i $SYS -m chrf --chrf-word-order 2

# # Compute chrF++ score using sacrebleu with FLORES-200 dataset
# sacrebleu $REF -i $SYS -m chrf --chrf-word-order 2

# # Compute scores using sacrebleu and store them in OUTPUT_FILE
# sacrebleu $REF -i $SYS -m bleu chrf ter --chrf-word-order 2 > $OUTPUT_FILE


# echo "Scores have been saved to $OUTPUT_FILE"

#!/bin/bash

if [ $# -ne 2 ]; then
    echo "usage: $0 GENERATE_PY_OUTPUT OUTPUT_FILE"
    exit 1
fi

GEN=$1
OUTPUT_FILE=$2

SYS=$GEN.sys
REF=$GEN.ref

if [ $(tail -n 1 $GEN | grep BLEU | wc -l) -ne 1 ]; then
    echo "not done generating"
    exit
fi

grep ^D $GEN | awk -F '\t' '{print $NF}' | perl -ple 's{(\S)-(\S)}{$1 ##AT##-##AT## $2}g' > $SYS
grep ^T $GEN | cut -f2- | perl -ple 's{(\S)-(\S)}{$1 ##AT##-##AT## $2}g' > $REF

# Compute scores using sacrebleu and store them in OUTPUT_FILE
sacrebleu $REF -i $SYS -m bleu chrf ter --chrf-word-order 2 > $OUTPUT_FILE

echo "Scores have been saved to $OUTPUT_FILE"
