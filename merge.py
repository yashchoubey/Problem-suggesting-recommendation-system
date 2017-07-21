import csv

hacker_id=None
challenge_id=None
attempts=0
solved=0
flag=True
max_solved=0
input_file = csv.DictReader(open("submissions.csv"))

csvfile = open('outputFileName.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(['hacker_id', 'challenge_id', 'attempts', 'solved'])

for row in input_file :
	if flag:#only for first time
		hacker_id=row['hacker_id']
		challenge_id=row['challenge_id']
		attempts=1
		solved=row['solved']
		flag=False
		
	if attempts>max_solved:
	  max_solved=attempts
	  
	#print hacker_id+ challenge_id+ str(attempts)+ str(solved)
	if hacker_id==row['hacker_id'] and 	challenge_id==row['challenge_id']:
		if row['solved']==1:
			solved=1
		attempts+=1
	else:
		#print "@@@@@"+hacker_id+ challenge_id+ str(attempts)+ str(solved)
		#write global values to file
		writer.writerow([hacker_id, challenge_id, attempts, solved])
		#set new terms as global variables
		hacker_id=row['hacker_id']
		challenge_id=row['challenge_id']
		attempts=1
		solved=row['solved']

#print max_solved
csvfile.close()

input_file = csv.DictReader(open("outputFileName.csv"))
matrix_score=0
csvfile = open('correlation.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(['hacker_id', 'challenge_id', 'matrix_score'])
for row in input_file :
  matrix_score=0
  if int(row['solved'])==1:
    matrix_score=100
  else:
    matrix_score=row['attempts']
  
  writer.writerow([row['hacker_id'], row['challenge_id'], matrix_score])
csvfile.close()
