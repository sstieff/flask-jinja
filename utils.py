from flask import request

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

def register_data(form_data):
  feedback = []
  for key, value in form_data.items():
    # checkboxes have [] for special handling
    if key.endswith('[]'):
      # Use getlist to get all values for the checkbox
      checkbox = request.form.getlist(key)
      key = key.replace('_', ' ').replace('[]', '')
      feedback.append(f"{key}: {', '.join(map(str, checkbox))}")
    else:
      # Handle other form elements
      key = key.replace('_', ' ')
      feedback.append(f"{key}: {value}")
  return feedback