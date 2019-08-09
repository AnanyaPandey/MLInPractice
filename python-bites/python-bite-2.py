import pandas as pd
( df > 0 ).all() # is every value in dataframe > 0 
( df.column1 > 0 ).all() # applied to only one column of df

(df>0).any() # is there even single data element > 0  # yes df == np.nan works as well missing values.
df.empty # to check if dataframe is empty | works with subset of df as well. 

for temp in [df1,df2,df3]:
if temp['col'].empty :
temp['col'] = 100

# df1 == df2 may not work because np.nan == np.nan is FALSE
df1.equals(df2) # Works !! 

df.sum() # df.sum(axis=0,skipna=True) axis=1 is column 
df.mean() 
df.std()

# count	Number of non-NA observations
# sum	Sum of values
# mean	Mean of values
# mad	Mean absolute deviation
# median	Arithmetic median of values
# min	Minimum
# max	Maximum
# mode	Mode
# abs	Absolute Value
# prod	Product of values
# std	Bessel-corrected sample standard deviation
# var	Unbiased variance
# sem	Standard error of the mean
# skew	Sample skewness (3rd moment)
# kurt	Sample kurtosis (4th moment)
# quantile	Sample quantile (value at %)
# cumsum	Cumulative sum
# cumprod	Cumulative product
# cummax	Cumulative maximum
# cummin	Cumulative minimum


Series.nunique() # number of unique non NA values in series
series.unique() # returns the unique values of the series 

df.idxmin() # idxmin(axis=1) / axis=0
df.idxmax()

df.value_counts()
series.value_counts()

# aggregare of dataframe 
datafram.agg(['sum','mean'])
#             A         B         C
#sum   3.033606 -1.803879  1.575510
#mean  0.505601 -0.300647  0.262585

datafram.agg(['sum', lambda x: x.mean()])
def myfun(x):
return(np.log(x))
datafram.agg(['sum',myfun])

# aggregate with help of dictionary
datafram.agg({'A':['mean','sum'], 'B':'sum'})

# Transforming entire Dtaframe
df.transform(np.abs)  # abs is absolute value |a|
df.transform({'A': np.abs, 'B': lambda x: x + 1}) # A and B are columns of dataframe

# element wise operation
# map apply and applymap
df['column'].map(len) 
df['column'].map(myfun)
df.applymap(myfun)
df.apply(myfun,axis=0) # applies row wise

# drop a column or row
df.drop(['col1','col2'],axis=1,inplace=True)
df.drop(columns=['col1','col2'])
df.drop([1,2,3],axis=0)


# sorting of dataframe 
df.sort_index()
df.sor_index(ascending=True)
df['column'].sort_index
data.sort_values(['ApplicantIncome','CoapplicantIncome'], ascending=False)

#changind the datatype pf columns

df.astype('float32').dtypes

# Data Filtering  | Filtering multiple columns 
#This will apply above 3 filters and return only 3 of these columns.
data.loc[(data["Gender"]=="Female") & (data["Education"]=="Not Graduate") & (data["Loan_Status"]=="Y"), ["Gender","Education","Loan_Status"]]

def num_missing(x)
return sum(x.isnull())

# Crosstabs 

pd.crosstab(data['CreditHistory'], data['LoanStatus'],margins=True)