'''


gameReturn Module

This module allows the user to return games and submit feedback based on the
game. This module checks if the user is renting the game by going into the
rental file and then updates the rental file and adds the feedback to the
feedback file after.

Key Features:
- Checks to see if the game is real and being rented by the user
- Updates the feedback file with feeback given from the users
- Updates the rental file with the return date instead of null

Functions:
- game_return(customerID,GameID,rating,comments): Accepts the customerID,
GameID, rating and comments and then checks to see if the game can be
returned or not and updates the feedback file and the rental file.
- verify_games(GameID): Verifies if the game is real or not by going
through the game info file
- game_not_available(GameID,customerID): Accepts the GameID and customerID
and checks the rental file to see if the game is rented or not and returns
True or False.
- add_feedback(GameID,rating,comments): Accepts GameID, rating and comments
and adds those values to the game feedback file
- update_rental_file(customerID,GameID): Accepts customerID and GameID
and then updates the rental file with todays date instead of NULL.
'''
import sys
import feedbackManager as FM
import Database as DATA
import datetime


def game_return(customerID,GameID,rating,comments):
    '''
    Manages the process of returning a game by a customer while updating the
    rental file appropiately.

    Verifies the game and checks if the customer had previously rented it. 
    If conditions are met, allows the customer to return the game, adds
    feedback, and updates the rental file. Otherwise, displays a message
    indicating the inability to return the game.

    Parameters:
    - customerID (str): ID of the customer returning the game.
    - GameID (str): ID of the game being returned.
    - rating (int): Rating given by the customer for the returned game.
    - comments (str): Comments or feedback provided by the customer for
    the returned game.

    Returns:
    - No return value.
    '''
    print("="*22)
    print("~"*3+"Returning a game"+"~"*3)
    print("="*22)   
    if verify_games(GameID) and game_not_available(GameID,customerID):
        add_feedback(GameID,rating,comments)
        update_rental_file(customerID,GameID)
        print("Game has been returned successfully")
    else:
        print("Sorry you cannot return the game")
    
def verify_games(GameID):
    """
    Verifies if the provided game ID exists in the game information.

    Parameters:
    - GameID (str): ID of the game to be verified.

    Returns:
    - games (bool): True if the game ID exists, False otherwise.
    """
    Game_Info_List = DATA.Read_File("Game_info.txt")
    games = False
    for i in range(1,len(Game_Info_List)):
        if Game_Info_List[i][0] == GameID:
                   games = True
    return games
    
def game_not_available(GameID,customerID):
    """
    Checks if the game is rented and available for the customer to be returned.

    Parameters:
    - GameID (str): ID of the game to be checked.
    - customerID (str): ID of the customer trying to return the game.

    Returns:
    - Value (bool): True if the game is rented by the customer, False otherwise.
    """
    Rental_Games_List = DATA.Read_File("Rental.txt")
    Value = False
    for i in range(1,len(Rental_Games_List)):
        if (Rental_Games_List[i][2] == "NULL" and
            Rental_Games_List[i][0] == GameID and
            Rental_Games_List[i][3] == customerID):
                Value = True
    return Value

def add_feedback(GameID,rating,comments):
    '''
    Adds feedback for the returned game to the 'Game_Feedback.txt' file with
    comments and ratings.

    Parameters:
    - GameID (str): ID of the game for which feedback is being provided.
    - rating (int): Rating given by the customer for the returned game.
    - comments (str): Comments or feedback provided by the customer for the
    returned game.

    Returns:
    - No return value.
    '''
    FM.add_feedback(GameID,rating,comments,"Game_Feedback.txt")

def update_rental_file(customerID,GameID):
    '''
    Updates the rental file after a game is returned by a customer.

    Parameters:
    - customerID (str): ID of the customer returning the game.
    - GameID (str): ID of the game being returned.

    Returns:
    - No return value.
    '''
    Rental_Games_List = DATA.Read_File("Rental.txt")
    return_date = str(datetime.datetime.now().strftime("%d-%m-%Y"))
    for i in range(1,len(Rental_Games_List)):
        if (Rental_Games_List[i][0] == GameID and
            Rental_Games_List[i][2] == "NULL" and
            Rental_Games_List[i][3] == customerID):
            Rental_Games_List[i][2] = return_date
    DATA.WriteList_File(Rental_Games_List,"Rental.txt")
    print("Rental file successfully updated")

if __name__ == "__main__":
    # Test cases or demonstration for the functions in gameReturn module

    # Demonstrating game_return function which utilises every function in this module
    print("Testing game_return function using \"yvqn\",\"NBA19\",\"4\""
          ",\"Enjoyed the attacking features\":")
    game_return("yvqn","NBA19","4","Enjoyed the attacking features")
    print("Function works correctly as you can see above")
    print("\n")
    
    # Demonstrating verify_games function
    print("Testing verify_games function using \"NBA19\":")
    print("Will return True if game is verified, otherwise"
          " false:", verify_games("NBA19"))
    print("Function works correctly as you can see above")
    print("\n") 
    
    # Demonstrating game_not_available function
    print("Testing game_not_available function using \"PGA00\" and \"JEFF\":")
    print("Returns True if game can be rented but false"
          " if the game cannot:", game_not_available("PGA00","JEFF"))
    print("Function works correctly as you can see above")
    print("\n")

    #Demonstrating add_feedback function
    print("Testing add_feedback function using \"PGA02\", \"5\","
          " \"Really nice swing mechanics\":")
    add_feedback("PGA02","5","Really nice swing mechanics")
    print("File has been successfully updated, and so"
          " the function works correctly")
    print("\n")

    #Demonstrating update_rental_file function
    print("Testing verify_games function using \"cwsj\" and \"Cricket02\":")
    update_rental_file("cwsj","Cricket02")
    print("The function works correctly.")
    
