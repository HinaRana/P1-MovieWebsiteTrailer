#This file contains the list of my favourite movies along with their
#details such as Movie name, Storyline, Movie poster image and
#Movie trailer url.

import media
import fresh_tomatoes


#following are the instances of the class movie

toy_story = media.Movie("Toy Sory",
                        "A story of a boy and his toys which come to life",
                        "https://vignette4.wikia.nocookie.net/disney/images/5/5b/Toy_Story_3_-_Poster.jpg/revision/latest?cb=20160408160703",
                        "https://youtu.be/JcpWXaA2qeg")




avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://s3.foxmovies.com/foxmovies/production/films/18/images/posters/251-asset-page.jpg",
                     "https://youtu.be/5PSNL1qE6VY")



me_before_you = media.Movie("Me Before You",
                            "A story of a girl and a boy who fall in love",
                            "http://moviereviews.s3.amazonaws.com/2016/02/09/07/26/37/478/oN5lELHH5Xheiy0YdhnY3JB4hx2.jpg",
                            "https://youtu.be/Eh993__rOxA")



midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back in time to meet authors",
                                "https://ih0.redbubble.net/image.12813797.9187/flat,1000x1000,075,f.u2.jpg",
                                "https://youtu.be/FAfR8omt-CY")


deadpool = media.Movie("Deadpool",
                       "A man reinvents himself as a wisecracking, spandex-clad antihero known as Deadpool, and seeks revenge on those responsible.",
                       "http://static.rogerebert.com/uploads/movie/movie_poster/deadpool-2016/large_large_k1QUCjNAkfRpWfm1dVJGUmVHzGv.jpg",
                       "https://youtu.be/Xithigfg7dA")



the_vow = media.Movie("The Vow",
                      "Story of a happily married couple whose life suddenly shutter when a car accident leaves the wife in comma.",
                      "http://www.impawards.com/2012/posters/vow_ver2_xlg.jpg",
                      "https://youtu.be/7JoXHO3ceUY")


#Array containing list of all the movies.
movies = [toy_story , avatar, me_before_you, midnight_in_paris, deadpool, the_vow]
fresh_tomatoes.open_movies_page(movies)


