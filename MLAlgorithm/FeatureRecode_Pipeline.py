# modify the feature sex recode as 0 and 1  

for df in [train,test]:
    df['Sex_binary']=df['Sex'].map({'male':1,'female':0})


# creating pipeline for step by step operations 

from sklearn.pipeline import pipeline, make_pipeline

# pipeline1 = pipeline('tupple_name',Constructor()) or [(multiple_tuple),(tuple)] )

pipeline1 = pipeline(steps=[('robust',RobustScaler()),('GBClassifier',GradientBoostingClassifier())])
pipeline2 = pipeline2([('robust',RobustScaler()),('standard',StandardScaler()),('GBClassifier',GradientBoostingClassifier())])

# output of first tuple is passed on to the second tuple in the pipeline 
# e.g. in pipeline 2 after robust scaler data or input will be passed through standard scaler and then through gradient boosing classigier

pipeline.named_steps # Returns a dictionary with key : name of the constructor and value : all the hyperparameters of the constructor

pipeline.steps # returns tupes with parameters 

# to access the hyperparameters 

pipeline1.named_steps['GBClassifier'].learning_rate
pipeline1.named_steps['GBClassifier'].random_state

''' What is make pipeline : 
the difference is that make_pipeline automatically names the constructor for us '''

process_pipeline1 = make_pipeline(RobustScaler(),GradientBoostingClassifier())

# Names for both will be robustscaler and gradientboosingclassifier All Lower case ! Right 
#  Pipelines can be used for cleaing transforming preprocessing and model fitting

pipeline_miss_num = make_pipeline(Imputer(strategy='median',axis=0)) # for numerical features 
pipeline_miss_cat = make_pipeline(Imputer(strategy='most_frequent',axis=0)) # for categorical ones 

# We could have created one single pipeline for the above 3 pipelines 



# mow using the pipelines 
# Example 

from sklearn.imputer import SimpleImputer
frmo sklearn.preprocessing import StandardScaler,OneHotEncoder


num_features = train.select_dtypes(include=['int64','float64']).columns # only features names are taking
cat_features = train.select_dtypes(exclude=['int64','float64']).columns # only features names are taking

numerical_changer = pipeline(steps = [
	('imputr',SimpleImputer(strategy='median')),
	('scalr',StandardScaler())
	])

categorical_changer = pipeline(steps=[
	('imputr',SimpleImputer(strategy='most_frequent',fill_value='missing')),
	('onehot',OneHotEncoder(handle_unknown='ignore'))
	])

from sklearn.compose import ColumnTransformer
preprocessor = ColumnTransformer(transformers = [
	('num',numerical_changer,num_features),
	('cat',categorical_changer,cat_features)
	])

# Now fitting the model 

from sklearn.ensemble import RandomForestClassifier
rf = pipeline(steps=[
	('prepro',preprocessor),
	('clasifier',RandomForestClassifier())
	])

# numerical veraibles will be preprocessed separately
# Categorical will be preprocessed separately

rf.fit(X_train,y_train)




