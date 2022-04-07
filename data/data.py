import csv

input_file=r"./spam_email.txt"
ouput_file=r"./spam_email.csv"

in_txt = csv.reader(open(input_file,'r'), delimiter = ' ')
out_csv = csv.writer(open(ouput_file,'w'))

out_csv.writerows(in_txt)

del out_csv