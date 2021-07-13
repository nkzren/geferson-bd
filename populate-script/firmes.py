import requests

url = "https://imdb8.p.rapidapi.com/title/get-popular-movies-by-genre"

querystring = {"genre":"/chart/popular/genre/adventure"}

headers = {
    'x-rapidapi-key': "b8eb11b991msh17b100125999668p13a6dbjsncd193db9f42d",
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }

tconsts = requests.request("GET", url, headers=headers, params=querystring)

lista = tconsts.text.strip('][').split(', ')
print(lista)

