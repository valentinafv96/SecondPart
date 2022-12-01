'''
$ sudo pip3 install fastapi
$ pip3 install uvicorn[standard]
$ uvicorn main:app --reload
'''
from typing import Optional

from fastapi import FastAPI

import requests

import json

app = FastAPI()

file='https://raw.githubusercontent.com/valentinafv96/SecondPart/main/data/openalexco_udea_pp_reduced.json'

#JSON SCHEME
#[{"id": str,
# "doi": str,
# "title": str,
# "display_name": str,
# "publication_year": value,
# "publication_date": str
# ...}
#]

@app.get("/")
def read_item(id: str = ""):
    '''
    Filtration of data is through the `id`, so the usage is as follows: 
    
    USAGE: http://127.0.0.1:8000/?id=https://openalex.org/W4289443651
    '''
    #Real time JSON file
    r=requests.get(file)
    db=r.json()
    new_db=[ d for d in db if str(d.get('id'))==id  ]
    f=open('data/filtered.json','w')
    json.dump(new_db,f)
    f.close()
    #with open(file) as json_file:
    #   db=json.load(json_file)

    if not id:
        return db
    else:
        return new_db
