import pandas as pd
import graphlab
# pass in column names for each CSV and read them using pandas. 
# Column names available in the readme file

#Reading users file:
u_cols=['challenge_id','contest_id','domain','subdomain','difficulty','solved_submission_count','total_submissions_count']
challenges = pd.read_csv('challenges.csv',  names=u_cols,)

#Reading ratings file:
r_cols=['hacker_id','contest_id','challenge_id','language','solved','created_at']
ratings = pd.read_csv('submissions.csv', sep='\t', names=r_cols,
 encoding='latin-1')


r_cols = ['hacker_id','challenge_id','matrix_score']
train_data = graphlab.SFrame.read_csv('train.csv',header=True,column_type_hints=[str,str,int])
test_data = graphlab.SFrame.read_csv('test.csv',header=True,column_type_hints=[str,str,int])
#print train.shape, test.shape



#########A Simple Popularity Model############
popularity_model = graphlab.popularity_recommender.create(train_data, user_id='hacker_id', item_id='challenge_id', target='matrix_score')
popularity_recomm = popularity_model.recommend(users=None,k=10)
popularity_recomm.print_rows(num_rows=25)


#predict, recommend, evaluate, and save
###########A Collaborative Filtering Model##############
#Train Model
item_sim_model = graphlab.item_similarity_recommender.create(train_data, user_id='hacker_id', item_id='challenge_id', target='matrix_score', similarity_type='pearson')

item_sim_model.show()
print "##########################################"
#Make Recommendations:
item_sim_recomm = item_sim_model.recommend(users=None,k=10)
item_sim_recomm.print_rows(num_rows=25)

###################checking performance################
model_performance = graphlab.compare(test_data, [popularity_model, item_sim_model])

