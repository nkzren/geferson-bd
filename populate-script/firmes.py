import requests


def get_movies():
    url = "https://imdb8.p.rapidapi.com/title/get-most-popular-movies"
    
    querystring = {"homeCountry":"US","purchaseCountry":"US","currentCountry":"US"}

    headers = {
        'x-rapidapi-key': "b8eb11b991msh17b100125999668p13a6dbjsncd193db9f42d",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

    tconsts = requests.request("GET", url, headers=headers, params=querystring)
    lista_tconsts = tconsts.text.replace('"', '').strip('][').split(',')


    url = "https://imdb8.p.rapidapi.com/title/get-details"

    movies = list()
    for t in lista_tconsts:
        t = t.split('/')[-2]
        
        querystring = {"tconst": t}
        response = requests.request("GET", url, headers=headers, params=querystring)

        title = response.json()['title']
        print(title)
        movies.append(title)

    return movies

get_movies()