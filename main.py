import json
import data
from typing import List
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import pandas as pd
import pprint
import re

global personList
personList = []


def main():
    # data.downloadNLTK()
    global designation, name, workedAt, email, location, skills, degree, graduationYear, collegeName
    df = pd.read_json(r"C:\Users\merty\OneDrive\Masaüstü\Hackathon\2\hackaton_data\train.json", encoding='utf-8',
                      lines=True)

    fullNameTemp = df['content'].str.split("\n", n=1, expand=True)  # take names
    df['Name'] = fullNameTemp[0]

    pd.json_normalize(df)

    labelsTemp = df['annotation'].to_dict()  # take dataframe as dictionary
    labelsTempList = []
    for i in range(200):
        labelsTempList.append(labelsTemp[i])  # turn it into a list like this bcs typecasting didn't work

    df['labels'] = labelsTempList
    df.explode('labels')
    pd.json_normalize(df)  # wish this worked but nope

    # extract values from labelsTempList via iterating through and creating a ReadData object to hold them
    k = 0
    j = 0
    labelsDict = {"Skills":None, "Graduation Year":None, "College Name":None, "Location":None, "Designation":None, "Degree":None, "Companies worked at":None, "Name":None, "Email Address":None}
    newdf = pd.DataFrame(labelsDict, index=[0])
    newdf.dropna(how="all", inplace=True)
    for j in range(len(labelsTempList)):
        for k in range(len(labelsTempList[j])):  # can't assign values bcs of not defined error.
            # labelsTempListIterator = list(labelsTempList[j][0].values())
            # print(j)
            #print(labelsTempList[j][0].get("label"))
            if labelsTempList[j][k] is not None and "Skills" in labelsTempList[j][k].get("label"):
                skills = dict(labelsTempList[j][k].get('points')[0]).get('text')
                labelsDict["Skills"] = skills
            elif labelsTempList[j][k] is not None and "Graduation Year" in labelsTempList[j][k].get("label"):
                graduationYear = dict(labelsTempList[j][k].get('points')[0]).get('text')
                labelsDict["Graduation Year"] = graduationYear
            elif labelsTempList[j][k] is not None and "College Name" in labelsTempList[j][k].get("label"):
                collegeName = dict(labelsTempList[j][k].get('points')[0]).get('text')
                labelsDict["College Name"] = collegeName
            elif labelsTempList[j][k] is not None and "Location" in labelsTempList[j][k].get("label"):
                location = dict(labelsTempList[j][k].get('points')[0]).get('text')
                labelsDict["Location"] = location
            elif labelsTempList[j][k] is not None and "Designation" in labelsTempList[j][k].get("label"):
                designation = dict(labelsTempList[j][k].get('points')[0]).get('text')
                labelsDict["Designation"] = designation
            elif labelsTempList[j][k] is not None and "Degree" in labelsTempList[j][k].get("label"):
                degree = dict(labelsTempList[j][k].get('points')[0]).get('text')
                labelsDict["Degree"] = degree
            elif labelsTempList[j][k] is not None and "Companies worked at" in labelsTempList[j][k].get("label"):
                workedAt = dict(labelsTempList[j][k].get('points')[0]).get('text')
                labelsDict["Companies worked at"] = workedAt
            elif labelsTempList[j][k] is not None and "Name" in labelsTempList[j][k].get("label"):
                name = dict(labelsTempList[j][k].get('points')[0]).get('text')
                labelsDict["Name"] = name
            elif labelsTempList[j][k] is not None and "Email Address" in labelsTempList[j][k].get("label"):
                email = dict(labelsTempList[j][k].get('points')[0]).get('text')
                labelsDict["Email Address"] = email
            tempdf = pd.DataFrame(labelsDict, index=[0])
            newdf.append(tempdf)
            #personList.append(data.ReadData.__init__(collegeName , designation, name, workedAt, email, location, skills, degree, graduationYear))
            #not defined error


        #print(skills)
        #print(graduationYear)
        print(newdf)
    # print(labelsTempList[0])
    #print(dict(labelsTempList[0][0].get('points')).get('text'))
    #print(dict(labelsTempList[j][0].get('points')[0]).get('text'))
    # print(labelsTempList[0][1])
    # print(labelsTempList[0][0])
    # print(type(labelsTempList))
    # print(df)
    # print(df['annotation'][0])
    # print(type(df['annotation'][0][0]))
    # print(df['annotation'])
    # print(labelsTemp)
    # print(df['Name'])                                          comment hell
    # print(annotations)
    # print(labels[0])
    # print(annotations[0])
    # porter = PorterStemmer()
    # print(labelsTempList[0][0].values())
    # labelsTempListIteratorList = [list(labelsTempList.values())]
    # labelsTempListIterator = list(labelsTempList[0][0].values())
    # print(labelsTempListIterator[1][0])
    # print(labelsTempListIterator)


if __name__ == '__main__':
    main()

# then turn ReadData objects into a DataFrame
# bring those 2 dataframes together
# train with proper dataframe
# build model
# see how it compares to another model