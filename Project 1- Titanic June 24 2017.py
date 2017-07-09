# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 15:22:24 2017

@author: hn7569
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#setting style of charts
sns.set(style="whitegrid")

#Read Data
df=pd.read_csv('titanic_data.csv')


#Find out how long the dataset is and what the fields are.
len(df)
df.head(10)

#Added a record count field in order to count items
df["Count"]=1

#Check data types and for null values. Age has 714 values and the rest are null.
df.info()
  
#Function to check the values of each field for the qualitative variables.

def content():
    field=input("What field do you want to check?")
    content=df[[field,'Count']]
    content=content.groupby(field).sum()
    return content

#Use function to check content for each field for data exploration
content()

#For the missing ages, we will replace the null values 
#with the average ages for that sex and class.
#So we will need to find those values.

ages=df[['Pclass','Sex','Age']]
ages=ages.groupby(['Sex','Pclass']).mean()
ages

#Create a dataset of all of the values that do not have an age of Null
df1=df[df['Age']>0]

#Create a dataset of all the ages that are null
df2=df[df['Age'].isnull()]

#Apply average ages found in 'ages' table to the null values Ages

def agefix(df2):
    """ This function takes the null values in the age field and applies the averages age for that sex and pclass for that record entry.
        Args:
            This is the dataset that has only null values in age.
        Returns:
            Returns the average age for that sex and Pclass as found in ages.
    """
    if df2['Sex']=='male' and df2['Pclass']==3: return 26.5
    elif df2['Sex']=='male' and df2['Pclass']==2: return 30.7
    elif df2['Sex']=='male' and df2['Pclass']==1: return 41.28
    elif df2['Sex']=='female' and df2['Pclass']==1: return 34.61
    elif df2['Sex']=='female' and df2['Pclass']==2: return 28.72
    elif df2['Sex']=='female' and df2['Pclass']==3: return 21.75
    else: return df['Age']

df2['Age']=df2.apply(agefix,axis=1)

#Union the fixed ages with rest of the ages.
frames=[df1,df2]
df=pd.concat(frames)
df.info()

#Dropped unneeded fields
df=df.drop(['Name','Ticket','Cabin','PassengerId'],axis=1)

#Created field for survived description
df['Survived_Desc']="Survived"
df['Survived_Desc'][df['Survived']!=1]='Died'

#Created field for class description
df['Class_Desc']="First Class"
df['Class_Desc'][df['Pclass']==3]="Third Class"
df['Class_Desc'][df['Pclass']==2]="Second Class"
df=df.drop('Pclass',axis=1)

#Created field for age range descriptions
df['Age Group']=">=65"
df['Age Group'][df['Age']<65]="56 to 65"
df['Age Group'][df['Age']<55]="46 to 55"
df['Age Group'][df['Age']<45]="36 to 45"
df['Age Group'][df['Age']<35]="26 to 35"
df['Age Group'][df['Age']<25]="16 to 25"
df['Age Group'][df['Age']<=15]="15 and Younger"


#Functions. 

def survival_rate():
    """ This function helps the analyist find the survial rate. The inputs are the number of passengers that survivedd and died with that attribute.
        Args:
            None
        Returns:
            Returns survival rate in float format. Example, if player said 60 surived and 40 died. The function would return 60.0.
    """
    y=int(input("How many survived?"))
    x=int(input("How many died?"))
    return (y/(x+y))*100

def visualize(df):
    """ This function helps the analyist find the visualize the frequency chart. The input is the Titanic dataset. The user only enters the field that they wish to visualize.
        Args:
            df: It is the titanic dataset.
        Returns:
            Returns a horizonal bar chart of that attribute visualized.
    """
    print(df.columns)
    item=input("What attribute do you want to visualize of the ones above?")
    viz0=df[['Survived_Desc',item,'Count']]
    viz0=viz0.groupby(['Survived_Desc',item],as_index=False).sum()
    viz0=viz0.pivot(index=item,columns='Survived_Desc',values='Count')
    viz0
    viz0.plot(kind='barh',title='Survival Frequency')
    plt.xlabel('Number of Passengers')
    plt.ylabel(item)
       
#program... repeat as necessary
visualize(df)
survival_rate()

#Chart for main count on died and survival
viz1=df[['Survived_Desc','Count']]
viz1=viz1.groupby('Survived_Desc').sum()
viz1
viz1.plot(kind='barh',title='Number of passengers that Died and Survived')
plt.xlabel('Number of Passengers')
plt.ylabel('Survival Description')

#Histogram chart
age_bins = np.arange(0, 100, 4)
sns.distplot(df.loc[(df['Survived']==0) & (~df['Age'].isnull()),'Age'], bins=age_bins)
sns.distplot(df.loc[(df['Survived']==1) & (~df['Age'].isnull()),'Age'], bins=age_bins)
plt.title('Age Distribution within Survival Classes')
plt.ylabel('Frequency')
plt.legend(['Did Not Survive', 'Survived'])
