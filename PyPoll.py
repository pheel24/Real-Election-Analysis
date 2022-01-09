#dependencies
import csv
import os
# variable to load file
file_to_load = os.path.join("resources", "election_results.csv")
# variable to save file
file_to_save=os.path.join("analysis","election_analysis.txt")

#accumulator
total_votes=0

#candidates
candidate_options=[]

#vote key-value store
candidate_votes={}

#victory trackers
winning_candidate=""
winning_count=0
winning_percentage=0

#open results and read file
with open(file_to_load) as election_data:
    
    #read file object
    file_reader=csv.reader(election_data)
    
    #print header
    headers=next(file_reader)
    
    #print rows for some stupid reason (melt disk?)
    for row in file_reader:
    
    #add total vote count
        total_votes +=1
    
    #print candidates for each row
        candidate_name=row[2]
        #candidate doesnt match any existing..
        if candidate_name not in candidate_options:
        #add name to list
            candidate_options.append(candidate_name)

            #track vote counts
            candidate_votes[candidate_name]=0
        #add votes to total
        candidate_votes[candidate_name]+=1
#percentages calculation
for candidate_name in candidate_votes:
    #retrieve vote count
    votes=candidate_votes[candidate_name]
    #calc %
    vote_percentage=float(votes) / float(total_votes)*100
    #print name & %
    print(f"{candidate_name}: recieved {round(vote_percentage,1)}% of the vote")
    
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    #determine winning count\candidate
    if (votes>winning_count) and (vote_percentage > winning_percentage):
        # if true, set winning count = votes etc.
        winning_count = votes
        winning_percentage = vote_percentage
        #set winning candidate equal to candidate name
        winning_candidate = candidate_name
winning_candidate_summary= (
    f"-----------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-----------------------\n")

print(winning_candidate_summary)