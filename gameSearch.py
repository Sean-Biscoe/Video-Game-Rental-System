'''

Student ID: F325508

Game Search module

This module searches through the game info list depending on the user input,
either the title, genre or platform of the game. THis also checks if those
games are rentable and outputs it for the user to see.

Key Features:
- Searches through the game info file based on its title, genre and platform.
- Outputs to the user if the games are available or not.

Functions:
- Title_Search(Title): Accepts Title and searches through the game info file
by title and appends them to a list and returns a list of games
- Genre_Search(Genre): Accepts Genre and searches through the game info file
by genre and appends them to a list and returns a list of games
- Platform_Search(Platform): Accepts Platform and searches through the game
info file by platform and appends them to a list and returns a list of games
- rentable_single(GameID): Accepts GameID and searches through the rental text
file to check if the game is available be to rented or not
- rentable(List_of_games): Accepts lists of games and passes every game through
the rentable_single(GameID) function one by one and then updates the list if
they are available or not. Then outputs the list to the users.
'''
import sys
import Database as DATA


def Title_Search(Title):
    '''
    Searches for games by their title through the game info file and returns a
    list of games.

    Parameters:
    - Title (str): Title of the game being searched.

    Returns:
    - List_of_games (list): List of games matching the provided title.
    '''
    Game_list = DATA.Read_File("Game_info.txt")
    List_of_games = []
    for line in Game_list:
        if line[3] == Title:
            List_of_games.append(line)
    rentable(List_of_games)
    return List_of_games

def Genre_Search(Genre):
    '''
    Searches for games by their genre through the game info file and returns a
    list of games.

    Parameters:
    - Genre (str): Genre of the game being searched.

    Returns:
    - List_of_games (list): List of games matching the provided genre.
    '''
    Game_list = DATA.Read_File("Game_info.txt")
    List_of_games = []
    for line in Game_list:
        if line[2] == Genre:
            List_of_games.append(line)
    rentable(List_of_games)
    return List_of_games

def Platform_Search(Platform):
    '''
    Searches for games by their platform through the game info file and returns
    a list of games.

    Parameters:
    - Platform (str): Platform of the game being searched.

    Returns:
    - List_of_games (list): List of games matching the provided platform.
    '''
    Game_list = DATA.Read_File("Game_info.txt")
    List_of_games = []
    for line in Game_list:
        if line[1] == Platform:
            List_of_games.append(line)
    rentable(List_of_games)
    return List_of_games

def rentable_single(GameID):
    '''
    Checks if a specific game is available for rent by looking through the
    rental file.

    Parameters:
    - GameID (str): ID of the game being checked for availability.

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

def rentable(List_of_games):
    '''

    Updates game names in the list to indicate their availability status
    (available/unavailable) by using the rental file.

    Parameters:
    - List_of_games (list): List of games to check for availability.

    Returns:
    - No return value.
    '''
    Rental_Games_List = DATA.Read_File("Rental.txt")
    games_names = []
    for i in range(0,len(List_of_games)):
        games_names.append(List_of_games[i][0])
    for row in range(len(games_names)):
        if rentable_single(games_names[row])== True:
            games_names[row] = f"{games_names[row]} is available"
        else:
            games_names[row] = f"{games_names[row]} is unavailable"
    print(games_names)

if __name__ == "__main__":
    # Test cases or demonstration for the functions in gameSearch module

    # Demonstrating Title_Search function which utilises rentable function as well
    print("Testing Title_Search function using \"NBA\":")
    Title_Search("NBA")
    print("The functions works as shown above")
    print("\n")

    # Demonstrating Genre_Search function which utilises rentable function as well
    print("Testing Genre_Search function using \"Sports\":")
    Genre_Search("Sports")
    print("The functions works as shown above")
    print("\n")

    # Demonstrating Platform_Search function which utilises rentable function as well
    print("Testing Platform_Search function using \"PlayStation\":")
    Platform_Search("PlayStation")
    print("The functions works as shown above")
    print("\n")


    # Demonstrating rentable_single function 
    print("Testing rentable_single function using \"NBA19\":")
    print("True means available and False means"
          " unavailable:",rentable_single("NBA19"))
    print("The function works as shown above")
    print("\n")

    # Demonstrating rentable function which utilises rentable function as well
    print("Testing rentable function using \"NBA20,PlayStation,Sports,"
          "NBA,EA_Sports,01/07/2019\""
          " \"Cricket03,PlayStation,Sports,CRICKET,NACON,15/08/2003\""
          " \"NBA19,PlayStation,Sports,NBA,EA_Sports,23/07/2018\":")
    example_list = [["NBA20","PlayStation","Sports","NBA","EA_Sp"
                     "orts","01/07/2019"],
            ["Cricket03","PlayStation","Sports","CRICKET","NACON","15/08/2003"],
            ["NBA19","PlayStation","Sports","NBA","EA_Sports","23/07/2018"]]
    rentable(example_list)
    print("The function works as shown above")
