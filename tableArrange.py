#!/usr/bin/python
# coding: UTF-8

# Python version: 2.7.10 (system)

import csv

inputFile = open('input.csv', 'r')
reader = csv.reader(inputFile)

outputFile = open('output.csv', 'w')
writer = csv.writer(outputFile, lineterminator='\n')

header = next(reader)
headerLabel = next(reader)

headerCount =  header.count("header")
dataCount = header.count("data1")

output_row = []

# make header label
for j in range(header.count("header")):
	print headerLabel[j] +",",
	output_row.append(headerLabel[j])

print "data1"
output_row.append("data1")
writer.writerow(output_row)
output_row = []

# make data table
for row in reader:
	
	for i in range(dataCount):#header.count("data1"):
		
		# write header
		for j in range(header.count("header")):
			output_row.append(row[j])

		# add data labels to list
		output_row.append(headerLabel[i + headerCount])

		# add data to list
		output_row.append(row[i + headerCount])

		# write data label and data
		writer.writerow(output_row)
		output_row = []
	

inputFile.close()
outputFile.close()