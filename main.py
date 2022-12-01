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

file='https://raw.githubusercontent.com/valentinafv96/SecExam/main/data/openalexco_udea_pp_reduced.json'

#JSON SCHEME
#[{"student_id": str,
# "Evaluation 1":{"value": int,
#                 "%": int,
#                 "Description": str
#                 }, 
# ...
# }
#]

@app.get("/")
def read_item(id: str = ""):
    '''
    You can write the API documentation here:
    
    For example: 
    
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
