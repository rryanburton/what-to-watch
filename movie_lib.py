import csv

all_movies = {}
all_user = {}


class User:
    def __init__(self, user_id):
        self.id = user_id
        # age
        # gender
        # occupation
        # zipcode


class Movie:
    def __init__(self, movie_id, title):
        self.id = movie_id
        self.title = title
        all_movies[self.id] = self
        self.ratings = {}  #key: user_id, value: Rating object

        # several other columns of info
    def __str__(self):
        return 'Movie(movie_id={}, title={})'.format(self.id, repr(self.title))

    def get_ratings(self):
        return self.ratings.values()

    def add_rating(self, rating):
        self.ratings[rating.user_id] = rating


    def Movie(movie_title):
        movie_id = Movie.movie_title


class Rating:
    def __init__(self, user, movie, stars):
        self.user = user
        self.movie = movie
        self.stars = stars
        # self.timestamp = timestamp
        all_movies[self.movie_id].add_rating(self)

    def __str__(self):
        return 'Rating(user_id={}, movie_id={}, stars={})'.format(self.id)

        # timestamp
#Find all ratings for a movie by id


##Find the average rating for a movie by id
#Find all ratings for a movie by id
# then find the average rating for the matching rows
#

##find all ratings for a User
# #look for all instances of the user id in u.data of the user id in u.user

#
# with open('u.data', 'rt') as args:
# with open('testdata.csv', 'rt') as args:
#     cin = csv.reader(args, delimiter='\t')
#     movie_ratings = [row for row in cin]
# print(movie_ratings)
#
# with open('testdata.csv') as f:
#     reader = csv.reader(f, delimiter='\t')
#     # header = next(reader)
#     for row in reader:
#         print(row)
#
# with open('testdata.csv') as f:
#     reader = csv.DictReader(f, delimiter='\t')
#     for row in reader:
#         print(row)

# with open('testdata.csv') as f:
#     reader = csv.DictReader(f, delimiter='\t', fieldnames=['user_id', 'movie_id', 'stars', 'timestamp'])
#     for row in reader:
#         print(row)



# with open('u.item') as args:
#     cin = csv.reader(args, delimiter='|')
#     movie_info = [row for row in cin]
# print(movie_info)
#
#
# with open('u.user') as args:
#     cin = csv.reader(args, delimiter='|')
#     users = [row for row in cin]
# print(users)


# class ClassName(object):
#     """docstring for """
#     def __init__(self, arg):
#         super(, self).__init__()
#         self.arg = arg
#
#lookup movie_id when given movie_title
#find the name of the movie in u.item by looking up a particular movie_id

##find all ratings for a User
# #look for all instances of the user id in u.data of the user id in u.user
