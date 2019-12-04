#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import zipfile
import io
import pydicom
from pydicom import dcmread
from pydicom.filebase import DicomBytesIO
import requests
from tqdm import tqdm

pbar = tqdm(total=197)
def getImageUrl(sid):
    baseurl = 'https://services.cancerimagingarchive.net/services/v3/TCIA'
    queryEndpoint = '/query/getImage?'
    queryParams = f'SeriesInstanceUID={sid}&'
    form = 'format=zip'
    url = baseurl+queryEndpoint+queryParams+form
    return url
    

def download_extract_zip(url):
    """
    Download a ZIP file and extract its contents in raw bytes format 
    in memory
    yields (filename, file-like object) pairs
    """
    response = requests.get(url)
    with zipfile.ZipFile(io.BytesIO(response.content)) as thezip:
        for zipinfo in thezip.infolist():
            data = thezip.read(zipinfo.filename)
            yield zipinfo.filename, data
            
def getImages(SID):
    imagedataset = []
    for s,sid in enumerate(SID):
        if s>3: break
        myurl = getImageUrl(sid)
        files = []
        for i,j in download_extract_zip(myurl):
            files.append(j)
        for i,f in enumerate(files):
            if i>3:
                break
            try:
                imagedataset.append(f)
#                imagedataset.append(dcmread(DicomBytesIO(f)))
            except:
                continue
    pbar.update(1)
    return imagedataset

