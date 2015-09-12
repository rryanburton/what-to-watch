from movie_lib import *

user1 = User(5)
user2 = User(12)


def test_user_creation():

    assert user1.id == 5
    assert user2.id == 12



# def test_user_creation():
#     user = User(a)
#     assert user.user_id == a
movie2 = Movie(9, 'Pretty Woman')
movie1 = Movie(3, 'Toy Story')
#
def test_movie_creation():
#
    assert movie1.title == 'Toy Story'
    assert movie1.id == 3
#
#
    assert movie2.title == 'Pretty Woman'
    assert movie2.id == 9
#
#
# rating1 = Rating(user2.user_id, movie2.movie_id, 5)
#
# def test_rating():
#     assert rating1.user_id == 5
#
#
# def test_find_ratings_for_movie():
#     toy_story_rating = all_movies[movie1.id].get_ratings()
