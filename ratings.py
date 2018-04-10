"""Restaurant rating lister."""


# put your code here

# open file
# get rid of white space
# split ':'
# add Restaurant[0] = key and Restaurant[1] = value - add values to dictionary
# sort dictionary by keys
# print dictionary in alphabetical order 

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


def print_ratings_alphabetically(restaurant_dict):
    # rating = True  
    # while rating == True:
    new_restaurant = raw_input("Give me a new restaurant to add: ").title()
    new_rating = int(raw_input("Give me a new rating to add for that restaurant: "))
        # if new_rating < 0 and new_rating > 6:
        #     print "Please try again with a rating of 1-5"
        # else:
        #     rating = False
    restaurant_dict[new_restaurant] = new_rating
    alphabetical_restaurants = sorted(restaurant_dict.items())
    for restaurant, rating in alphabetical_restaurants:
        print "{} is rated at {}".format(restaurant, rating)



ratings = making_restaurant_ratings_list('scores.txt')
restaurant_dict = make_ratings(ratings)
print_ratings_alphabetically(restaurant_dict)

