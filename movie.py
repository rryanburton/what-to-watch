import csv


# class User:
#     def __init__(self, id, **kwargs):
#         self.id = id
#         if 'age' in kwargs['age']
#
#     def __str__(self):
#         return 'User(id)'
#
#
# class Movie:
#     def __init__(self, id, **kwargs):
#         if 'id' in kwargs:
#             self.id = kwargs['id']
#
# class Rating:
#     def __init__(self, id, **kwargs):
#         if 'id' in kwargs:
#             self.id = kwargs['id']
#
# class ClassName(object):
#     """docstring for """
#     def __init__(self, arg):
#         super(, self).__init__()
#         self.arg = arg
#

# import csv
# with open('testdata.csv', newline='\n') as csvfile:
#     # spamreader = csv.reader(csvfile, delimiter=' ', quotechar='"|"')
#     # for row in spamreader:
#     #     print(', '.join(row))


import csv
with open('testdata.csv', 'rt') as args:
    cin = csv.reader(args, delimiter='\t')
    movie_ratings = [row for row in cin]
print(movie_ratings)


import csv
with open('u.item') as args:
    cin = csv.reader(args, delimiter='|')
    movie = [row for row in cin]
print(movie)

# with open('u.item', 'rt') as fin:
#     cin = csv.DictReader(fin, delimiter='|', fieldnames=['movie_id', 'movie_title', 'release_date', 'vrelease_date'])
#     movie_info = [row for row in cin]
#     print(movie_info)
# with open('u.item', 'rt') as fin:
#     cin = csv.reader(fin, delimiter='|')
#      movie_info = [row for row in cin]
# print(movie_info)

# with open('testdata.csv', 'wb') as f:
#     reader = csv.reader(f, delimiter='\t')
#     for row in for row in reader:
#         print(row)
#Find all ratings for a movie by id
#
# then look at the list of u.data and find all the instances
# is in the list from u.item and find the instance of a movie's movie_id

##Find the average rating for a movie by id
# then find the average rating for the matching rows

##find the name of the movie in u.item by looking up a particular movie_id

##find all ratings for a User
# #look for all instances of the user id in u.data of the user id in u.user
