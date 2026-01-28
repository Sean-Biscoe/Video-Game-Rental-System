'''



Inventory Pruning Module

This module allows the manager to see how games are rated in a graph and
outputs to the user which games are poorly rated. This module also goes
through the rental file to see how many times each game has been rented
and outputs the most and least rented games.

Key Features:
- Creates a graph with ratings of games from the game feedback file.
- Ouputs the most rented games and least rented games and least
popular games, suggesting the user to remove games to save space.

Functions:
- create_graph(): Goes through the game feedback file and creates a list of
ratings and then a list of games. Creates a table with the lists as axis.
Calls the Bad_Game
and Popular_and_unpopular_Games functions.
- Bad_Game(x,y): Accepts x and y as inputs and identifies bad games if their
rating is less than or equal to 2.
- Popular_and_unpopular_Games(): Goes through the rental file and creates a
dictionary of the gameID and how many times the game was rented. Then outputs
the games that are the most and least rented.
'''
import matplotlib.pyplot as plt
import Database as DATA

def create_graph():
    '''
    Generates a bar chart showing game popularity based on ratings.

    Reads game feedback data from 'Game_Feedback.txt' file and calculates
    average ratings for each game. Creates a bar chart using Matplotlib
    to display game ratings. Calls 'Bad_Game' and 'Popular_and_unpopular_Games'
    functions for additional analysis.
    
    Parameters:
    - No parameters needed.
    
    Returns:
    - No return value.
    '''
    plt.title("Graph showing game popularity")
    plt.xlabel("Games")
    plt.ylabel("Rating")

    game_feedback_list = DATA.Read_File("Game_Feedback.txt")
    x = []
    y = []
    NBA = 0
    NBA_rating = 0
    Cricket = 0
    Cricket_rating = 0
    GTA = 0
    GTA_rating = 0
    PGA = 0
    PGA_rating = 0
    Apex = 0
    Apex_rating = 0

    for i in range(1,len(game_feedback_list)):
        if game_feedback_list[i][0][0:3] == "NBA":
            NBA_rating += int(game_feedback_list[i][1])
            NBA +=1
        elif game_feedback_list[i][0][0:7] == "Cricket":
            Cricket_rating += int(game_feedback_list[i][1])
            Cricket +=1
        elif game_feedback_list[i][0][0:3] == "GTA":
            GTA_rating += int(game_feedback_list[i][1])
            GTA +=1
        elif game_feedback_list[i][0][0:3] == "PGA":
            PGA_rating += int(game_feedback_list[i][1])
            PGA +=1
        elif game_feedback_list[i][0][0:4] == "Apex":
            Apex_rating += int(game_feedback_list[i][1])
            Apex +=1
    NBA_rating = NBA_rating/NBA
    y.append(NBA_rating)
    x.append("NBA")
    Cricket_rating = Cricket_rating/Cricket
    y.append(Cricket_rating)
    x.append("Cricket")
    GTA_rating = GTA_rating/GTA
    y.append(GTA_rating)
    x.append("GTA")
    PGA_rating = PGA_rating/PGA
    y.append(PGA_rating)
    x.append("PGA")
    Apex_rating = Apex_rating/Apex
    y.append(Apex_rating)
    x.append("Apex")

    
    plt.style.use('classic')
    plt.grid() 
    plt.ylim(0, 5)
    plt.bar(x,y,color = 'red')
    
    plt.show()
    Bad_Game(x,y)
    Popular_and_unpopular_Games()


def Bad_Game(x,y):
    '''
    Identifies games with ratings <= 2 and suggests their potential removal.

    Parameters:
    - x (list): List containing game names.
    - y (list): List containing game ratings.

    Returns:
    - No return value.
    '''
    bad_games_list = []
    for i in range(1,len(x)):
        if int(y[i])<=2:
            bad_games_list.append(x[i])
    if len(bad_games_list)==0:
        print("All the games are doing well. Congradulations!")
    elif len(bad_games_list) == 1:
        print(str(bad_games_list[0]), "is the game that unfortunately is not"
              "doing as well. So maybe think about"
              "removing",str(bad_games_list[0]))
    else:
        print(str(bad_games_list).replace("[","").replace("\'","")
              .replace("]","").replace(", \'",","), "are"
        " the games that are not doing as well. So maybe"
              " think about removing them")

def Popular_and_unpopular_Games():
    '''
    Identifies most and least popular games based on rental frequency.

    Reads rental data from 'Rental.txt' file and counts the number of
    rentals for each game.
    Identifies and displays the least rented and most popular games.

    Parameters:
    - No parameters needed
    
    Returns:
    - No return value.
    '''
    print("\n")
    print("Below is based on how often the games are rented.")
    Rental_List =DATA.Read_File("Rental.txt")
    game_id_count = {}

    for line in Rental_List:
        game_id = line[0]
        if game_id in game_id_count:
            game_id_count[game_id] += 1
        else:
            game_id_count[game_id] = 1

    game_id_count.pop("Game_ID")
    
    min_count = min(game_id_count.values())
    least_rented_games = [game_id for game_id, count in game_id_count
                          .items() if count == min_count]
    print(f"Least rented game(s) with {min_count} rental(s):")
    for game_id in least_rented_games:
        print(game_id)
    print("You should probably think about removing these games to save space")
    print("\n")
    
    max_count = max(game_id_count.values())
    most_popular_games = [game_id for game_id, count in game_id_count
                          .items() if count == max_count]
    print(f"Most popular game(s) with {max_count} rental(s):")
    for game_id in most_popular_games:
        print(game_id)

if __name__ == "__main__":
    # Test cases or demonstration for the functions in InventoryPruning module

    # Demonstrating create_graph function which utilises every function
    print("Testing create_graph function:")
    create_graph()
    print("So the function works")
