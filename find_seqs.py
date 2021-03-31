import re, sys, os
import numpy as np

query_file = sys.argv[1]
input_sequence_file = sys.argv[2]
output_file_name = sys.argv[3]

print('Arguments are:'+' '.join(sys.argv[1:]))



secs_query = open(query_file, 'r').readlines()
secs_query = [re.sub('\n|', '', i) for i in secs_query]

infile = open(input_sequence_file, 'r')
outfile = open(output_file_name, 'w')
counter = 0
recorded = 0
writing_lines = False

while True:
    counter += 1
    line = infile.readline()
    
    if (not line) or (recorded > (len(secs_query))):
        break
    
    if '>' in line:
        taxon_name = re.sub('>|\n', '', line)
        is_in_metadata = [i == taxon_name for i in secs_query]
        if any(is_in_metadata):
            match = np.where(is_in_metadata)
            outfile.write('>'+taxon_name+'\n')
            writing_lines = True
            recorded += 1
            print('found '+taxon_name+'. Searched '+str(counter)+' lines.'+' Recorded '+str(recorded))
        else:
            writing_lines = False
            
    elif writing_lines:
        outfile.write(line)


infile.close()
outfile.close()

