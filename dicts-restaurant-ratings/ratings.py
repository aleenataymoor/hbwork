"""Restaurant rating lister."""
open_file=open("scores.txt","r")
ratings_dict={}




def print_restaurant_ratings():

    for line in open_file:
        word=line.rstrip().split(":")
        ratings_dict[word[0]]=int(word[1])
    alphabetized_ratings=sorted(ratings_dict)

    for restaurant in alphabetized_ratings:
        rating=ratings_dict[restaurant]
        print(f'{restaurant} is rated at {rating}')


        
def input_func():

    restaurant_name=input("What's the restaurant that you want to rate?>>>")
    restaurant_score=input("What's the rating?>>>")
    ratings_dict[restaurant_name]=restaurant_score
    print_restaurant_ratings()
input_func()


