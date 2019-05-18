import json
import http.client
from last_id import *


class MoviesBase:
    def __init__(self):
        self.movies_dict = {}
        self.last_movie = last_movie

    def set_movies_dict(self, year):
        file = 'id_' + str(year) + '.txt'
        with open(file) as f:
            all_id = f.readlines()
            for id in all_id:
                id = id.strip()
                conn = http.client.HTTPSConnection("api.themoviedb.org")
                payload = "{}"
                adress = "/3/movie/" + id + "?language=en-US&api_key=f8ddb7d056e033df36a511c18ea94e17"
                conn.request("GET", adress, payload)
                res = conn.getresponse()
                movie = json.loads(res.read())
                try:
                    self.movies_dict[movie['title']] = {}
                    for el in ['vote_average', 'vote_count', 'popularity', 'budget', 'revenue', 'release_date']:
                        self.movies_dict[movie['title']][el] = movie[el]
                    self.movies_dict[movie['title']
                                     ]['production_companies'] = {}
                    for comp in movie['production_companies']:
                        if comp['origin_country'] == 'US':
                            self.movies_dict[movie['title']
                                             ]['production_companies'][comp['name']] = None
                except KeyError:
                    continue
        self.check_latest()

    def get_companies(self):
        companies = []
        for el in self.movies_dict:
            for comp in self.movies_dict[el]['production_companies']:
                companies.append(comp)
        return companies

    def set_companies(self, lst):
        i = 0
        for el in self.movies_dict:
            self.movies_dict[el] = lst[i]
            i += 1

    def check_latest(self):
        pass


if __name__ == '__main__':
    year = 2000
    atd = MoviesBase()
    atd.set_movies_dict(year)
    data = atd.movies_dict
    print(data)
