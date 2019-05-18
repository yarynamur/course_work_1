import json
import http.client
import quandl


class MoviesBase:
    def __init__(self, year):
        self.year = year
        self.movies_dict = {}

    def set_movies_dict(self):
        with open('sorted_dict.json') as f:
            dict = json.load(f)
            cur_year = dict[self.year]
            for comp in cur_year:
                self.movies_dict[comp] = []
                for id in cur_year[comp]:
                    conn = http.client.HTTPSConnection("api.themoviedb.org")
                    payload = "{}"
                    adress = "/3/movie/" + id + "?language=en-US&api_key=f8ddb7d056e033df36a511c18ea94e17"
                    conn.request("GET", adress, payload)
                    res = conn.getresponse()
                    movie = json.loads(res.read())
                    try:
                        if movie['revenue'] != 0:
                            self.movies_dict[comp].append(movie['revenue'])
                        else:
                            self.movies_dict[comp].append(movie['title'])
                    except:
                        print('There is no revenue parameter in movie {}, id: {}'.format(
                            movie['title'], id))
