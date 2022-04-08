import csv

input_file=r"./letters_CG.txt"
ouput_file=r"./letters_CG.csv"

in_txt = csv.reader(open(input_file,'r'), delimiter = ' ')
out_csv = csv.writer(open(ouput_file,'w'))

out_csv.writerows(in_txt)

del out_csv