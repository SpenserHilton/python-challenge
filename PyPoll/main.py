import csv
import os


# Pathing to file
election_data = os.path.join('election_data_1.csv')

#initialize lists
voters = []
candidate = []

#Populate lists
with open(election_data, newline="") as data:
	reader = csv.reader(data, delimiter = ",")
	next(reader) #skip header
	for row in reader:
		#grab voter id
		voters.append(row[0])

		#grab candidate
		candidate.append(row[2])

#total number of votess cast
totalvotes=len(voters)

#list of candidates receiving votes
unique_cand = set(candidate)
unique_cand_list = list(unique_cand)

#count votes for each candidate
cand1_votes = candidate.count(unique_cand_list[0])
cand2_votes = candidate.count(unique_cand_list[1])
cand3_votes = candidate.count(unique_cand_list[2])
cand4_votes = candidate.count(unique_cand_list[3])

#generate percentage of votes per candidate
perc_votes = []

cand1_perc = '{0:.2f}%'.format(candidate.count(unique_cand_list[0])/totalvotes*100)
cand2_perc = '{0:.2f}%'.format(candidate.count(unique_cand_list[1])/totalvotes*100)
cand3_perc = '{0:.2f}%'.format(candidate.count(unique_cand_list[2])/totalvotes*100)
cand4_perc = '{0:.2f}%'.format(candidate.count(unique_cand_list[3])/totalvotes*100)

perc_votes.append(cand1_perc)
perc_votes.append(cand2_perc)
perc_votes.append(cand3_perc)
perc_votes.append(cand4_perc)

votecount = []
votecount.append(cand1_votes)
votecount.append(cand2_votes)
votecount.append(cand3_votes)
votecount.append(cand4_votes)


votes_by_cand = zip(unique_cand, perc_votes, votecount)

print("Election Results", "\n", "-------------------")
print("Total Votes:", totalvotes, "\n", "------------------")
print(unique_cand_list[0]+ ": " +str(cand1_perc) + " (" +str(votecount[0]) +")" )
print(unique_cand_list[1]+ ": " +str(cand2_perc) + " (" +str(votecount[1]) +")" )
print(unique_cand_list[2]+ ": " +str(cand3_perc) + " (" +str(votecount[2]) +")" )
print(unique_cand_list[3]+ ": " +str(cand4_perc) + " (" +str(votecount[3]) +")" )


print("--------------------")	
print("Winner: ", max(set(candidate), key=candidate.count ))


#set fielpath for output
output_file = os.path.join("output.txt")
#open and write to output file
file = open("output.txt", 'w')
file.write("Election Results"+ "\n"+ "-------------------" +"\n")
file.write("Total Votes:"+ str(totalvotes)+ "\n" + "------------------" +"\n")
file.write(unique_cand_list[0]+ ": " +str(cand1_perc) + " (" +str(votecount[0]) +")" +"\n" )
file.write(unique_cand_list[1]+ ": " +str(cand2_perc) + " (" +str(votecount[1]) +")" +"\n" )
file.write(unique_cand_list[2]+ ": " +str(cand3_perc) + " (" +str(votecount[2]) +")" + "\n")
file.write(unique_cand_list[3]+ ": " +str(cand4_perc) + " (" +str(votecount[3]) +")" +"\n")


file.write("--------------------" + "\n")	
file.write("Winner: "+ max(set(candidate), key=candidate.count ))

file.close()