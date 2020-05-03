import math
#Function goes here


def get_rating():

    error = "Please enter a number between 1 and 5"
    rating_reason = []

    valid = False
    while not valid:

        try:

            response = float(input("Rating: "))

            if response > 5:
                print("OK - the rating will be recorded as '5' - the highest possible rating")
                response = 5
                reason = input("Please give a reason for rating this book so highly: ")
            elif response < 1:
                print("OK - the rating will be recorded as '1' star because Good Reads does not "
                      "allow users to rate books with less than one star. ")
                response = 1
                reason = input("Please enter a reason for the low rating: ")

            elif response % 1 != 0:
                valid_round = False
                while not valid_round:
                    round_it = input("You have entered a decimal, would you like us to round up or down? ").lower()

                    if round_it == "up":
                        default_reason = " The book was worth than {} stars".format(int(response))
                        response = math.ceil(response)
                        break

                    elif round_it == "down":
                        default_reason = "It is not worth {} stars".format(math.ceil(response))
                        response = int(response)
                        break


                    else:
                        print("Please enter <up> or <down>")

                    print("Please enter reason for rounding the rating {}: ".format(round_it))
                    if reason == "":
                        print("You left the reason blank, so we have put in a reason for you.")
                        reason = default_reason

                reason = input("Please enter a reason for rounding the rating {}: ".format(round_it))
                if reason == "":
                    print("You left the reason blank, so we have put in a reason for you. ")
                    reason = default_reason

            else:
                response = int(response)
                reason = input("Please explain why you gave the book a rating of {}: ".format(response))

            rating_reason.append(response)
            rating_reason.append(reason)
            return rating_reason


        except ValueError:
            print(error)



# main routine goes here
rate_reason = get_rating()
print()
book_rating = rate_reason[0]
book_reason = rate_reason[1]

print("Rating: {}".format(book_rating))
print("Reason: {}".format(book_reason))
