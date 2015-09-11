import csv




class User:
    def __init__(self, user_id, **kwargs):
        self.user_id = user_id
        # age
        # gender
        # occupation
        # zipcode

#     def __str__(self):
#         return 'User(id)'

##find all ratings for a User
# #look for all instances of the user id in u.data of the user id in u.user

with open('u.user') as args:
    cin = csv.reader(args, delimiter='|')
    users = [row for row in cin]
print(users)









class Movie:
    def __init__(self, movie_id, movie_title, **kwargs):
        self.movie_id = movie_id
        self.movie_title = movie_title
        # several other columns of info

#lookup movie_id when given movie_title
#find the name of the movie in u.item by looking up a particular movie_id


with open('u.item') as args:
    cin = csv.reader(args, delimiter='|')
    movie_info = [row for row in cin]
print(movie_info)




class Rating:
    def __init__(self, rating_user_id, rating_item_id, rating_rating, **kwargs):
        self.rating_user_id = rating_user_id
        self.rating_item_id = rating_item_id
        self.rating_rating = rating_rating
        # timestamp
#Find all ratings for a movie by id


##Find the average rating for a movie by id
#Find all ratings for a movie by id
# then find the average rating for the matching rows
#

##find all ratings for a User
# #look for all instances of the user id in u.data of the user id in u.user


# with open('u.data', 'rt') as args:
with open('testdata.csv', 'rt') as args:
    cin = csv.reader(args, delimiter='\t')
    movie_ratings = [row for row in cin]
print(movie_ratings)








# class ClassName(object):
#     """docstring for """
#     def __init__(self, arg):
#         super(, self).__init__()
#         self.arg = arg
#
