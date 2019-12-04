#!/usr/bin/env python
# coding: utf-8

# In[1]:
from tqdm import tqdm

pbar = tqdm(total=197)

def multiply(x):
    pbar.update(1)
    return 100*x

