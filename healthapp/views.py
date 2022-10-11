import pandas as pd
import requests
import json

#Extracting the data
dataAPI = requests.get('https://play.dhis2.org/2.38.1.1/dhis-web-dataentry/index.action')
dataframe = dataAPI.text
parse_json = json.loads(dataframe)
 
#return dataframe

#Transforming the data
def transform(dataframe):
       sum = dataframe[Consumption] + dataframe[End balance]
       return sum

#Loading the data
def load(targetfile,dataframe):
    postdata = requests.post('https://play.dhis2.org/2.38.1.1/dhis-web-dataentry/index.action')
    return postdata




        