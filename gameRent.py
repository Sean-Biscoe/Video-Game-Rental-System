'''



gameRent Module

This module allows the a user to rent out a game based on if the game is
available, and if the user has not rented out more games than their
subscription limit.

Key Features:
- Verifies the if the customer and games are in the game files
- Checks to see if the game is already being rented and finds the customer
subsciption limit
- Checks to see if the customer can rent the game and then updates the rental
file

Functions:
- game_rent(customerID,GameID): Allows the customer to rent the game or not
based on the game availabilty and subscription limit of the user.
- verify_customer(customerID): Verifies if the customerID is real or not
by iterating tbrough the subscription type file.
- verify_games(GameID): Verifies if the GameID is real or not by iterating
through the game info file.
- game_rentable(GameID): Accepts GameID and goes through rental file to
see if the game is available to rent or not.
- check_rented_games(customerID): Accepts customerID and goes through rental
file and counts how many times the customer has rented games.
- check_customer_rental_limit(customerID): Accepts customerID and uses the
subscription manager to see the rental limit of the customer.
- check_customer_ID(customerID): Accepts customerID and compares the number
of games the user has rented to the rental limit of the user.
- renting_game(customerID,GameID): Accepts the customerID and GameID and
updates the rental file.

'''
import sys
import Database as DATA
import subscriptionManager as SM
import datetime

def game_rent(customerID,GameID):
    '''
    Manages the process of renting a game by a customer.

    Verifies the customer and game IDs. If both IDs are valid and
    the game is rentable, allows the customer to rent the game.
    Otherwise, displays a relevant error message.

    Parameters:
    - customerID (str): ID of the customer attempting to rent the game.
    - GameID (str): ID of the game to be rented.

    Returns:
    - No return value.
    '''
    if verify_customer(customerID) != True or verify_games(GameID)!=True:
        print("You entered either an incorrect game ID or customer ID,"
              " so you cannot rent the game out")
    else:
        if check_customer_ID(customerID) and game_rentable(GameID):
            renting_game(customerID,GameID)
            print(customerID,"is now renting the game",GameID)
        else:
            print("Unfortunately",customerID,"is not allowed to"
                  " rent the game",GameID)
    
def verify_customer(customerID):
    '''
    Verifies if the provided customer ID exists in the subscription information.

    Paramters:
    - customerID (str): ID of the customer to be verified.

    Returns:
    - customer (bool): True if the customer ID exists, False otherwise.
    '''
    SUBSCRIPTION = DATA.Read_File("Subscription_Info.txt")
    customer = False
    for i in range(1,len(SUBSCRIPTION)):
        if SUBSCRIPTION[i][0] == customerID:
                   customer = True
    return customer

def verify_games(GameID):
    '''
    Verifies if the provided game ID exists in the game information.

    Parameters:
    - GameID (str): ID of the game to be verified.

    Returns:
    - games (bool): True if the game ID exists, False otherwise.
    '''
    Game_Info_List = DATA.Read_File("Game_info.txt")
    games = False
    for i in range(1,len(Game_Info_List)):
        if Game_Info_List[i][0] == GameID:
                   games = True
    return games
    
def game_rentable(GameID):
    '''
    Checks if the provided game is available for rent.

    Parameters:
    - GameID (str): ID of the game to be checked.

    Returns:
    - Value (bool): True if the game is rentable, False otherwise.
    '''
    Rental_Games_List = DATA.Read_File("Rental.txt")
    Value = True
    for i in range(1,len(Rental_Games_List)):
        if (Rental_Games_List[i][2] == "NULL" and
        Rental_Games_List[i][0] == GameID):
                Value = False
    return Value

def check_rented_games(customerID):
    '''
    Counts the number of games rented by a customer.

    Parameters:
    - customerID (str): ID of the customer.

    Returns:
    - no_of_games (int): Number of games rented by the customer.
    '''
    Rental_Games_List = DATA.Read_File("Rental.txt")
    no_of_games = 0
    for i in range(1,len(Rental_Games_List)):
        if Rental_Games_List[i][3] == customerID:
            no_of_games +=1
    return no_of_games

def check_customer_rental_limit(customerID):
    '''
    Retrieves the rental limit for a specific customer by using the
    subscription manager.

    Parameters:
    - customerID (str): ID of the customer.

    Returns:
    - rental_limit (int): Rental limit for the customer.
    '''
    subscription_list = DATA.Read_File("Subscription_Info.txt")
    rental_limit = 0
    for i in range(1,len(subscription_list)):
        if subscription_list[i][0] == customerID:
            rental_limit = SM.get_rental_limit(subscription_list[i][1])
    return rental_limit

def check_customer_ID(customerID):
    '''
    Checks if a customer is eligible to rent a game based on their
    subscription and rental status.

    Parameters:
    - customerID (str): ID of the customer.

    Returns:
    - Can_rent (bool): True if the customer can rent a game, False otherwise.
    '''
    subscriptions = SM.load_subscriptions(file_name="Subscription_Info.txt")
    Can_rent = False
    if (check_rented_games(customerID)<check_customer_rental_limit(customerID)
    and SM.check_subscription(customerID,subscriptions)):
        Can_rent = True
    return Can_rent



def renting_game(customerID,GameID):
    '''
    Updates the rental information when a game is rented by a customer.

    Adds a rental record for the game with the customer's ID and current
    date in the rental file.

    Parameters:
    - customerID (str): ID of the customer renting the game.
    - GameID (str): ID of the game being rented.

    Returns:
    - No return value.
    '''
    current_date = str(datetime.datetime.now().strftime("%d-%m-%Y"))
    line = GameID+","+current_date+","+"NULL"+","+customerID
    DATA.AppendLine_File(line,"Rental.txt")

if __name__ == "__main__":
    # Test cases or demonstration for the functions in gameRent module

    # Demonstrating game_rent function which utilises every function
    print("Testing game_rent function:")
    game_rent("cwsj","GTA01")
    print("So this passed the test")
    print("\n")

    # Demonstrating verify_customer function
    print("Testing verify_customer function:")
    verified = verify_customer("JEFF")
    print("The customer is:",verified,"so the function works")
    print("\n")

    # Demonstrating verify_games function
    print("Testing verify_games function:")
    game_verified = verify_games("PGA99")
    print("The game is:",game_verified,"so the function works")
    print("\n")

    # Demonstrating game_rentable function
    print("Testing game_rentable function:")
    game_is_rentable = game_rentable("NBA16")
    print("NBA 16 is rentable and so game_rentable function"
          " ouputs:",game_is_rentable,"so the function works")
    print("\n")

    # Demonstrating check_rented_games function
    print("Testing check_rented_games function:")
    number_of_games = check_rented_games("JEFF")
    print("JEFF has rented/renting 3 games and the check_rented_games"
          " function says:", number_of_games,"games, so the function works")
    print("\n")

    # Demonstrating check_customer_rental_limit function    
    print("Testing the check_customer_rental_limit function:")
    rental_limit = check_customer_rental_limit("JEFF")
    print("JEFF has the premium subscription and has a rental limit of 7."
          " According to the check_customer_rental_limit function, JEFFs"
          " limit is",rental_limit," and so the function works")
    print("\n")

    # Demonstrating check_customer_ID function
    print("Testing the check_customer_ID function:")
    Allowed_to_rent = check_customer_ID("JEFF")
    print("JEFF should be able to rent based on his subscription limit and the"
          " amount of games JEFF has rented. According to the"
          " check_customer_ID function JEFF status is:",Allowed_to_rent,"so"
          " the function works")
    print("\n")

    # Demonstrating renting_game function
    print("Testing the renting_game function:")
    renting_game("rtin","PGA99")
    print("The rental file has been updated accordingly so the game works")
