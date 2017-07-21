import csv
user_list=[]

input_file = csv.DictReader(open("correlation.csv"))

csvfile = open('outputFileName.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(['hacker_id'])

for row in input_file :
	if row['hacker_id'] in user_list:
		pass
	else:
		user_list.append(row['hacker_id'])

	writer.writerow([row['hacker_id']])
#print max_solved
csvfile.close()