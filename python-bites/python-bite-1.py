#Phthon basic frequently used commands 

#read from csv to pandas data frame 
df=pd.read_csv('path/subpath/filename.csv')

#write to csv output to csv
df.to_csv('filename.csv')

#rename a column in dataframe 
data.rename(columns={'v1': 'label', 'v2': 'message'}, inplace=True)
df.rename(str.lower, axis='columns')
df.rename({1: 2, 2: 4}, axis='index')
data = data.rename({'v1': 'label', 'v2': 'message'})

# do something of entire column of dataframe 
data['column1'].apply(len) # identify length of each element in the column1 of data
# create function of your own which takes argument as each element of column and return the modified version

#==================

# encode categorical variable 

data['label'].replace(['ham','HAM'],'Hamburger',inplace=True)# replace ham or HAM to Hamburger for a column
data.replace(['ham','HAM'],'Hamburger',inplace=True) # replace ham or HAM to Hamburger for entire dataframe
data.repalce(10,100) # wherever its 10 will be replaced by 100

data['gender'].replace({'male':1,'female':0}) # best method to encode 
#=================== 

# tokenize a string sentence : returns each word in that sentence as separate string array

sentence = """At eight o'clock on Thursday morning ... Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)
tokens 
['At', 'eight', "o'clock", 'on', 'Thursday', 'morning',
'Arthur', 'did', "n't", 'feel', 'very', 'good', '.']