import pandas as pd
#q1
data = {'Name':['Sia', 'Sumit'],'Age':[18,24],'mail id':['sia@gmail.com','sumit@gmail.com'],'phone no':['6958398','875450938']}
df = pd.DataFrame(data)
df.loc[2]=['Pia',26,'pia@gmail.com','fjdhfjd']
print(df)

#Q2. Import the data from "https://raw.githubusercontent.com/Shreyas3108/Weather/master/weather.csv" and print:
df=pd.read_csv('weather.csv')
#print(df)
#a.) First 5 rows of Dataframe
print(df.head(5))
#b.) First 10 rows of the Dataframe
print(df.head(10))
#c.) Find basic statistics on the particular dataset.
print(df['MinTemp'].describe())
print(df['MaxTemp'].describe())
#d.) Find the last 5 rows of the dataframe
print(df.tail(5))
#e.) Extract the 2nd column and find basic statistics on it.
finaldata=[df.iloc[:,2].sum(),
df.iloc[:,2].mean(),
df.iloc[:,2].median(),
df.iloc[:,2].nunique(),
df.iloc[:,2].max(),
df.iloc[:,2].min()]
print(finaldata)