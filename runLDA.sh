#!/usr/bin/env bash
# input: list of files you want to run

# For each file, run LDA to generate the output
for arg in "$@"
do 
	~/Development/spark-1.3.0/bin/run-example mllib.LDAExample --stopwordFile stopword.txt --k 10 "$arg"
done
