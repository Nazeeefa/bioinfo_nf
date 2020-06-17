#!/usr/bin/env python3
import sys
import argparse
import gzip

"""Author: Nazeefa Fatima
Date: 20/06/2019

Description:
	The script performs demultiplexing i.e. sorting reads into separate files according to barcode of the sample FASTQ file 
	with the help of the barcode-to-sample translation.

Procedure:
		. Starts off with reading (for example) barcodes.txt file to create a dictionary.
			. Stores sample and barcode names as keys and values, respectively.
		. Search for barcode matches in compressed FASTQ file
		. If a match is found, take read (including sequence header and score) and save it to a new file
			. A compressed fastq file for each sample barcode will be created, 
				with the filename taken from the corresponding sample name mentioned in barcodes.txt
				Example: sample_A_demux.fastq.gz)

Usage:
		./demux_nf.py -i file.fastq.gz -b barcodes.txt
"""

usage ='''
Reads compressed FASTQ files, performs demultiplexing, and creates output files based on amount of samples.
''' 

def config_parser(parser):

		parser.add_argument("-v", "--version",
							action="version",
							version='%(prog)s 1.0')

		parser.add_argument("-i", "--fastq",
							action="store",
							dest="fastq",
							help="FASTQ file to be demultiplexed.",
							required=True)

		parser.add_argument("-b", "--barcodes",
							action="store",
							dest="barcodes",
							required=True,
							help="Text file with a list of barcodes that need to be extracted from each FASTQ file.")

def identify_barcodes(barcodes_txt):
	barcodes_dict = {}

	with open(barcodes_txt) as f:
		for line in f:
			if line.strip():
				sample,barcode = line.split()
				barcodes_dict[sample] = barcode
		# print(barcodes)
	return(barcodes_dict)

def barcode_to_sample(fastq, barcodes_file):

	barcodes = identify_barcodes(barcodes_file)
	count_line = 0
	match = False
	sample_fout = ""
	fout = ""

	with gzip.open(fastq) as fin:
		for line in fin:
			line = line.decode("utf-8")
			count_line += 1
			line.rstrip('\n')

			if count_line % 4 == 1:
				line = line.replace("wildype", "wildtype") #noticed a typo in input file
				barcode_f = line.strip().rsplit(" ", 1)[1] #barcode_f refers to a barcode in FASTQ file
				for sample,barcode in barcodes.items():
					if barcode == barcode_f:
						match = True
						sample_fout = sample
						break
						# print(sample_fout)
					else: 
						match = False
				if match == True:
					if fout != "":
						fout.close()
					# print(sample_fout)
					# note: gzip.open has high computational load
					# note: "at" != efficient to use & re-running the script will append to file.
					fout = gzip.open(sample_fout + "_demux.fastq.gz", "at")
					fout.write(line)
			else:
				if match == True and fout != "":
					fout.write(line)

def main():

	# Generate argument parser
	parser = argparse.ArgumentParser(description=usage)

	# Configure argparser
	config_parser(parser)

	# Parse arguments
	args = parser.parse_args()

	barcode_to_sample(args.fastq, args.barcodes)

if __name__ == "__main__":
    main()
