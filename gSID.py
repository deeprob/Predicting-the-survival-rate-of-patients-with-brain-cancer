#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import json
from tqdm import tqdm

pbar = tqdm(total=197)

def getSeriesID(pid,Collection):
    baseurl = 'https://services.cancerimagingarchive.net/services/v3/TCIA'
    queryEndpoint = '/query/getSeries?'
    queryParams = f'Collection={Collection}&PatientID={pid}&'
    form = 'format=json'
    url = baseurl+queryEndpoint+queryParams+form
    response = requests.get(url)
    SeriesInstanceUID = set()
    for dictionary in response.json():
        SeriesInstanceUID.add(dictionary['SeriesInstanceUID'])
    pbar.update(1)
    return SeriesInstanceUID

