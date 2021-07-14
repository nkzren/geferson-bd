import random
import time
import string
import requests


def get_movies():
    url = "https://imdb8.p.rapidapi.com/title/get-popular-movies-by-genre"
    querystring = {"genre":"/chart/popular/genre/adventure"}
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


def str_time_prop(start, end, time_format, prop=random.random()):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formatted in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start, end):
    return str_time_prop(start, end, '%Y/%m/%d', random.random())
    
def randomstring(length):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

def random_item(arr):
    return random.choices(arr)[0]

def random_id(arr):
    return random.randint(1, len(arr))

def random_number(minimum, maximum):
    return random.randint(minimum, maximum)