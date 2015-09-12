from movie_lib import *

siskel = User(5)
ebert = User(12)
movie2 = Movie(9, 'Pretty Woman')
movie1 = Movie(3, 'Toy Story')
rating1 = Rating(siskel.id, movie1.id, 4)
rating2 = Rating(ebert.id, movie2.id, 3)
rating3 = Rating(siskel.id, movie2.id, 1)
rating4 = Rating(ebert.id, movie1.id, 5)
print(all_movies)
print(all_movies[3])
print(id(movie1))
print(id(all_movies[3]))
print(id(siskel))

def test_user_creation():

    assert siskel.id == 5
    assert ebert.id == 12


#
def test_movie_creation():
    assert movie1.title == 'Toy Story'
    assert movie1.id == 3
    assert movie2.title == 'Pretty Woman'
    assert movie2.id == 9



# rating1 = Rating(user2.user_id, movie2.movie_id, 5)
#
def test_rating_creation():
    assert rating1.user_id == rating3.user_id == siskel.id
    assert rating2.user_id == rating4.user_id == ebert.id
    assert rating1.movie_id == rating4.movie_id == movie1.id
    assert rating2.movie_id == rating3.movie_id == movie2.id

def test_rating_rating():
    assert rating1.stars == 4
    assert rating2.stars == 3
    assert rating3.stars == 1
    assert rating4.stars == 5

def test_find_ratings_for_movie():
    toy_story_ratings = all_movies[movie1.id].get_ratings()
    pw_ratings = all_movies[movie2.id].get_ratings()
    print(len(toy_story_ratings))
    print(toy_story_ratings)
    # toy_story_ratings = get_ratings_for_movie(movie1.id)
    # return a list of Rating objects

    assert len(toy_story_ratings) == 2
    assert len(toy_story_ratings) == len(pw_ratings)
