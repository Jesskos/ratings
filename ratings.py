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
        print restaurant_ratings_list
        return restaurant_ratings_list


def make_ratings(ratings_list):
 
    
    restaurant_ratings = {}

    for restaurant in ratings_list:
        restaurant_ratings[restaurant[0]] = restaurant[1]

    print restaurant_ratings
    print type(restaurant_ratings)

    return restaurant_ratings


def print_ratings_alphabetically(restaurant_dict):
    #with open(file_name) as file_name:
        
        alphabetical_restaurants = sorted(restaurant_dict.keys())
        for restaurant in alphabetical_restaurants:
            rating = restaurant_dict[restaurant]
            print "{} is rated at {}".format(restaurant, rating)



ratings = making_restaurant_ratings_list('scores.txt')
restaurant_dict = make_ratings(ratings)
print_ratings_alphabetically(restaurant_dict)

