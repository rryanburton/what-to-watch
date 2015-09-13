import csv

all_movies = {}
all_users = {}


class User:
    def __init__(self, user_id):
        self.id = user_id
        # age
        # gender
        # occupation
        # zipcode
        all_users[self.id] = self

        def __str__(self):
            return 'User(user_id={})'.format(self.id)
        def __repr__(self):
            return self.__str__()


class Movie:
    def __init__(self, movie_id, title):
        self.id = movie_id
        self.title = title
        all_movies[self.id] = self
        self.ratings = {}  #key: user_id, value: Rating object

        # several other columns of info

    def __str__(self):
        return 'Movie(movie_id={}, title={})'.format(self.id, repr(self.title))

    def __repr__(self):
        return self.__str__()

    def add_rating(self, rating):
        self.ratings[rating.user_id] = rating

    def get_ratings(self):
        return self.ratings.values()


    def get_title(self):
        return self.title

    def get_id(title):
        return movie_id


class Rating:
    def __init__(self, user_id, movie_id, stars):
        self.user_id = user_id
        self.movie_id = movie_id
        self.stars = stars
        # self.timestamp = timestamp
        all_movies[self.movie_id].add_rating(self)

    def __str__(self):
        return 'Rating(user_id={}, movie_id={}, stars={})'.format(self.user_id, self.movie_id, self.stars)

    def __repr__(self):
        return self.__str__()


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

#   Find the name of a movie by id


#   Find all ratings for a movie by id
#   all_movies[movie1.id].get_ratings()
#   returns this:  dict_values([Rating(user_id=12, movie_id=9, stars=3), Rating(user_id=5, movie_id=9, stars=1)])
def top_movies():
    num_top = input("how many top movies do you want to see?\n")
    min_num_top = input("what is the minimum number of ratings a movie must have to be considered in the top list? \n")

# take the movies and find len(ratings)
# make a new list or remove the movies with quantity of ratings less than min_num_top


# show the num_top quantity of movies sorted with the highest ave rank 1st
    print("""The top {} movies by average rating are:\n
        disclaimer: movies must have been ranked at
         least {} times.\n""".format(num_top,min_num_top))
