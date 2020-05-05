import 

# Function goes here
def make_list(file_name):
    file_name = file_name+".txt" # add .txt to names to make it easier to call
    list_name = open(file_name).read().splitlines()
    return list_name


def text_helper(question, choose_random, items_per_line, possible_answers=None):



# main routine goes here

# Set up blank Adjective Lists
genre_list = []
all_negative = all_positive = all_neutral = []
action_list = fantasy_list = funny_list = historical_list = scary_list = []

# Populate adjective lists with content from text files

genre_list = make_list("genre")
all_negatives = make_list("all_negative")
all_positives = make_list("all_positive")
all_neutral = make_list("all_neutral")

action_list = make_list("action")
fantasy_list = make_list("fantasy")
funny_list = make_list("funny")
historical_list = make_list("historical")
scary_list = make_list("scary")

# Test that list has been generated
genre = "action"
adjective = text_helper("Choose an adjective", "yes", 4, action_list)
print(adjective)

