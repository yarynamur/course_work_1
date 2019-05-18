from data_type import MoviesFull
import unittest
from unittest import TestCase


class TestDataType(TestCase):
    def test_data_type(self):
        datatype = MoviesFull('1995')
        self.assertEqual(datatype.year, '1995')
        self.assertEqual(datatype.movies.movies_dict, {'FOX': ['French Kiss', 'Kiss of Death', 50012507, 'Bushwhacked', 'Bye Bye Love'], 'MGM': [49800000, 'Lord of Illusions', 31596911, 115101622, 'The Set Up', 20350754], 'DIS': ['Heavyweights', 'Circle of Life: An Environmental Fable', 346079773], 'TWX': [187436818, 104324083, 189859560, 11534477, 'Carrotblanca', 'Forget Paris', 'Dolores Claiborne', 40622], 'UVV':
                                                       [116112375, 2122561, 23574130, 13071518, 'Twilight Man'], 'LGF': [718490], 'NFLX': ['The Indian in the Cupboard', 'Loving You', 303], 'DRH': ['Citizen X', 'The First 100 Years: A Celebration of American Movies', '5 American Handguns - 5 American Kids', 'Kings of the Ring: Four Legends of Heavyweight Boxing']})
        self.assertEqual(datatype.stock_pr, {'MGM': 6.51, 'DIS': 14.38, 'TWX': 3.3,
                                             'FOX': 7.9, 'UVV': 8.76, 'LGF': None, 'NFLX': None, 'DRH': None, 'WWE': None})
        self.assertEqual(datatype.found_year, {'MGM': 1990, 'DIS': 1962, 'TWX': 1992,
                                               'FOX': 1987, 'UVV': 1988, 'LGF': 1998, 'NFLX': 2002, 'DRH': 2005, 'WWE': 1999})


if __name__ == "__main__":
    unittest.main()
