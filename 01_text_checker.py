# Checks that user enters something for required text (such as title)


# Functions go here
def not_blank(question):

    error = "Sorry, responses to this question can't be blank"

    valid = False
    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error)
            print()


# Main Routine goes here
title = not_blank("Title: ")
print("You will be reviewing {}".format(title))


def can_be_blank(question1):

    blank = "Anonymous"

    valid = False
    while not valid:
        response = input(question1)

        if response !="":
            return response
        else:
            return blank


author = can_be_blank("Author: ")
print("The book is written by {}".format(author))
