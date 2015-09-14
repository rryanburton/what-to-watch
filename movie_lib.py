import csv
import math
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
        self.ratings = {}  #key: movie_id, value: rating stars

    def add_user_rating(self, rating):
        self.ratings[rating.movie] = rating.stars

    def get_user_ratings(self):
        return self.ratings


        # def __str__(self):
        #     return 'User(user_id={})'.format(self.id)
        # def __repr__(self):
        #     return self.__str__()


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
        self.ratings[rating.user] = rating.stars

    def get_ratings(self):
        return self.ratings.values()

    def get_ave_rating(self):
        return round(sum(self.get_ratings())/len(self.get_ratings()), 2)

    def get_title(self):
        return self.title

    # def get_id(title):
    #     return movie_id


class Rating:
    def __init__(self, user, movie, stars):
        self.user = user
        self.movie = movie
        self.stars = stars
        # self.timestamp = timestamp
        all_movies[self.movie].add_rating(self)
        all_users[self.user].add_user_rating(self)


    def __str__(self):
        return 'Rating(user_id={}, movie_id={}, stars={})'.format(self.user_id, self.movie_id, self.stars)

    def __repr__(self):
        return self.__str__()




def get_ratings():
    with open('ml-100k/u.data') as args:
        reader = csv.DictReader(args, fieldnames=['user_id', 'movie_id', 'rating'], delimiter='\t')
        for row in reader:
            Rating(int(row['user_id']), int(row['movie_id']), int(row['rating']))

def get_items():
    with open('ml-100k/u.item', encoding='latin-1') as args:
        reader = csv.DictReader(args,  fieldnames=['movie_id', 'movie_title', ], delimiter='|')
        for row in reader:
            Movie(int(row['movie_id']), row['movie_title'])

def get_users():
    with open('ml-100k/u.user') as args:
        reader = csv.DictReader(args, fieldnames=['user_id'], delimiter='|')
        for row in reader:
            User(int(row['user_id']))


def top_movies():
    get_items()
    get_users()
    get_ratings()
    num_top = int(input("how many top movies do you want to see?\n"))
    min_num_top = int(input("what is the minimum number of ratings a movie must have to be considered in the top list? \n"))
    top_dict = {}
    for idx in all_movies:
        if len(all_movies[idx].get_ratings()) > min_num_top:
            top_dict[idx] = all_movies[idx].get_ave_rating()
    top_dict = sorted(top_dict.items(), reverse = True)
    print("""The top {} movies by average rating are:\n
        disclaimer: movies must have been ranked at
         least {} times.\n""".format(num_top,min_num_top))
    print(top_dict[:num_top])
# take the movies and find len(ratings)
# make a new list or remove the movies with quantity of ratings less than min_num_top



# show the num_top quantity of movies sorted with the highest ave rank 1st

top_movies()
# for each movie in top_movies look for a user_id and
# remove those movie_ids and make a new top_movies list



            # class ClassName(object):
            #     """docstring for """
            #     def __init__(self, arg):
            #         super(, self).__init__()
            #         self.arg = arg


#   Find all ratings for a movie by id
#   all_movies[movie1.id].get_ratings()
#   returns this:  dict_values([3, 1, etc])

#   Find average rating for movie by id
#   all_movies[movie2.id].get_ave_rating()
#   returns this: 2.0  (float ave)
