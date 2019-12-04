#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import requests
import json
from tqdm import tqdm

pbar = tqdm(total=96)

def getBodyPart(Collection):
    '''Provides the body part affected in a collection dataset'''
    baseurl = 'https://services.cancerimagingarchive.net/services/v3/TCIA'
    queryEndpoint = '/query/getBodyPartValues?'
    queryParams = f'Collection={Collection}&'
    form = 'format=json'
    url = baseurl+queryEndpoint+queryParams+form
    response = requests.get(url)
    if response.status_code==200:
        BodyPartExamined = []
        for dictionary in response.json():
            try:
                BodyPartExamined.append(dictionary['BodyPartExamined']) 
            except:
                continue
        pbar.update(1)
        return BodyPartExamined
    else:
        raise ValueError('Bad/No response')  

