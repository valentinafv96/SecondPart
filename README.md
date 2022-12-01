# User instructions

Install the following packages:

```
$ sudo pip3 install fastapi
$ pip3 install uvicorn[standard]
```

## Backend

1. Download the ZIP repository.
2. Extract the file.
3. In the location of the file, type in terminal:

```
$ uvicorn main:app --reload
```

4. Copy and paste the resultant url in your browser, e.g:

 * [http://127.0.0.1:8000/](http://127.0.0.1:8000/)



5. Now filter by `id` one of the given articles into the url as follows:

 * [http://127.0.0.1:8000/?id=https://openalex.org/W4280569373](http://127.0.0.1:8000/?id=https://openalex.org/W4280569373)

## Frontend

6. Finally, to visualize de result obtained, open a new terminal, go to the location of the extracted file and type:

```
$ python3 -m http.server 8001
```

The result will be the name, publication date and the location of the article filtered.
