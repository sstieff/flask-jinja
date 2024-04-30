def movie_stars(movie_dict):
  for movie in movie_dict:
    movie['stars'] = add_stars(movie['rating'])
  return movie_dict

def add_stars(rating):
  my_return = ""
  for x in range(10):
    x += 1
    if x % 2 == 0 and rating * 2 >= x:
      my_return += "<span class=\"fa fa-star checked\"></span>" 
    elif x % 2 == 1 and rating * 2 == x:
      my_return += "<span class=\"fa fa-star-half checked\"></span> "
    else: ""
  return my_return

movie_dict = [
  {"title": "Dune", "genre": "Sci-Fi", "rating":2.5},
  {"title": "Alien", "genre": "Sci-Fi", "rating":3.5},
  {"title": "Batman", "genre": "Comics", "rating":4.5}
 ]