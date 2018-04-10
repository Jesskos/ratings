"""Restaurant rating lister."""


# put your code here

# open file
# get rid of white space
# split ':'
# add Restaurant[0] = key and Restaurant[1] = value - add values to dictionary
# sort dictionary by keys
# print dictionary in alphabetical order 

import random 

def making_restaurant_ratings_list(file_name):
    restaurant_ratings_list = []    
    with open(file_name) as ratings_file:
        for line in ratings_file:
            line = line.rstrip()
            words_in_line = line.split(':')
            restaurant_ratings_list.append(words_in_line)
        return restaurant_ratings_list


def make_ratings(ratings_list):
 
    
    restaurant_ratings = {}

    for restaurant, rating in ratings_list:
        restaurant_ratings[restaurant] = rating


    return restaurant_ratings


def print_ratings_alphabetically(restaurants_with_ratings):

    alphabetical_restaurants = sorted(restaurants_with_ratings.items())

    for restaurant, rating in alphabetical_restaurants:
        print "{} is rated at {}".format(restaurant, rating)

def run_function():

    keep_running_function = True 

    while keep_running_function == True:

        choose_action = raw_input("\n Please choose one of the following numbers: \n Enter 1 to see all the rating) \n Enter 2 to add a new restaurant (and rate it) \n Choose 3 to modify a random restaurant \n Enter 4 to modify an existing restaurant \n Enter 5 to quit \n ")
       
        if choose_action == "1":
            print_ratings_alphabetically(restaurants_with_ratings)
        
        
        elif choose_action == "2":
            print ask_user_for_restaurant_and_rating(restaurants_with_ratings)
        
        elif choose_action == "3":
            print modify_random_restaurant(restaurants_with_ratings)


        elif choose_action == "4":
            print modify_existing_restaurant(restaurants_with_ratings)

        elif choose_action == "5":
            keep_running_function = False
        

        else:
            "Invalid Entry. Try again!"


def ask_user_for_restaurant_and_rating(restaurants_with_ratings):
    rating = True  
    while rating == True:
        new_restaurant = raw_input("Give me a new restaurant to add: ").title()
        new_rating = int(raw_input("Give me a new rating to add for that restaurant: "))
        if new_rating > 5:
            print "Please try again with a rating of 1-5"
        else:
            rating = False
            restaurants_with_ratings[new_restaurant] = new_rating


def modify_random_restaurant(restaurants_with_ratings):
    restaurants = restaurants_with_ratings.keys()
    random_restaurant = random.choice(restaurants)
    rating = True  
    while rating == True:
        users_rating = int(raw_input("Please enter your rating of {}".format(random_restaurant)))
        if users_rating > 5 or users_rating < 0:
            print "Please try again with a rating of 1-5"
        else:
            print "Your rating has been added!"
            rating = False
            restaurants_with_ratings[random_restaurant] = users_rating


def modify_existing_restaurant(restaurants_with_ratings):
    for restaurant, rating in restaurants_with_ratings.items():
        print "Restaurant: {}, rating: {}".format(restaurant, rating)
    rating = True  
    while rating == True:
        users_restaurant = raw_input("Please enter a restaurant from the list above\n").title()
        users_rating = int(raw_input("Please enter your rating of {}\n".format(users_restaurant)))
        if (users_rating > 5 or users_rating < 0):
            print "Please try again with a rating of 1-5"
        elif users_restaurant not in restaurants_with_ratings.keys():
            print "Uh oh. This restuarant does not exist, or you may have spelling error. Choose a restaurant from the list"
        else:
            rating = False
            restaurants_with_ratings[users_restaurant] = users_rating
            print "Your restaurant has been added."
            return None




ratings = making_restaurant_ratings_list('scores.txt')
restaurants_with_ratings = make_ratings(ratings)
run_function()
