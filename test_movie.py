from movie_lib import *
# def test_get_data():
#     get_items()
#     get_users()
#     get_ratings()

frank = User(2)
john = User(7)
siskel = User(5)
ebert = User(12)
movie2 = Movie(9, 'Pretty Woman')
movie1 = Movie(3, 'Toy Story')
rating1 = Rating(siskel.id, movie1.id, 4)
rating2 = Rating(ebert.id, movie2.id, 3)
rating3 = Rating(siskel.id, movie2.id, 1)
rating4 = Rating(ebert.id, movie1.id, 5)
rating5 = Rating(john.id, movie2.id, 2)
rating6 = Rating(frank.id, movie2.id, 4)
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

def test_rating_creation():
    assert rating1.user == rating3.user == siskel.id
    assert rating2.user == rating4.user == ebert.id
    assert rating1.movie == rating4.movie == movie1.id
    assert rating2.movie == rating3.movie == movie2.id

def test_rating_rating():
    assert rating1.stars == 4
    assert rating2.stars == 3
    assert rating3.stars == 1
    assert rating4.stars == 5

def test_all_ratings_fora_movie_by_id():
    pass

def test_ave_rating_movie_by_id():
    pass

def test_moviename_by_id():
    pass

def test_all_ratings_fora_user_id():
    print(all_users[5].get_user_ratings(), "all user[5] ratings") #this prints if test fails
    assert all_users[5].get_user_ratings() == {9: 1, 3: 4}


def test_find_ratings_for_movie():
    toy_story_ratings = all_movies[movie1.id].get_ratings()
    all_pw_ratings = all_movies[movie2.id].get_ratings()
    all_user_ratings = all_users[5].get_user_ratings()
    # ave_pw_rating = sum(all_pw_ratings) / len(all_pw_ratings)
    # print(all_pw_ratings)
    # print(len(toy_story_ratings))
    # print(toy_story_ratings)
    # print(all_movies[movie2.id])
    # print(all_movies[movie2.title])
    # # print(all_movies[movie2.title].get_id())
    # print(rating.stars)

    print(all_movies[9], "all_movies[9]")
    # print(id("Pretty Woman"))
    # print(id(all_movies[9]))




    print(all_movies[movie2.id].get_ratings(), 'all_movies[movie2.id].get_ratings()')
    print(all_movies[movie2.id].get_ave_rating())
    print(len(all_movies[movie2.id].get_ratings()))
    #
    #
    # print(all_movies[movie1.id].get_title())
    # print(all_movies[9].get_title())
    # print(all_movies)
    # print(list(all_movies))
    # print(all_movies.keys())
    # print(all_movies.get_id('Pretty Woman'))

    # toy_story_ratings = get_ratings_for_movie(movie1.id)
    # return a list of Rating objects

    assert len(toy_story_ratings) == 2
    # assert len(toy_story_ratings) == len(pw_ratings)
