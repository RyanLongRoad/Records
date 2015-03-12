import pickle

class Game:

    def __init__(self):
    
    
        self.name = " "
        self.platform = " "
        self.genre = " "
        self.cost = " "
        self.number_of_players = " "
        self.online_functionality = " "    
    

def load_games(filename):
    
                     
##    games_database.dat
    
    with open(filename, mode = "rb") as game_file:
        loaded_games = pickle.load(game_file)

    

    return loaded_games
        

def save_games(games):
    
    with open("games_database.dat", mode = "wb") as game_file:
        pickle.dump(games, game_file)

        



#the parameter is games because eventually you will be displaying
#multiple games using this function

def display_games(games):    
        print("|{0:<10}|{1:<10}|{2:<10}|{3:<10}|{4:<20}|{5:<20}".format("Name", "Platform", "Genre", "Cost", "Number of players", "Online functionality|"))
        print()
        for each in games:

            print("|{0:<10}|{1:<10}|{2:<10}|{3:<10}|{4:<20}|{5:<20}|".format(each.name, each.platform, each.genre, each.cost, each.number_of_players, each.online_functionality))

        


    

def get_game_from_user(games):

    Exit = "0"

    while Exit != "-1":

        game = Game()
    
        Name = input("Please enter the name of the game: ")
        Platform = input("Please enter the platform on the game: ")
        Genre = input("Please enter the genre of the game: ")
        Cost = input("Please enter the cost of the game: ")
        Number_of_players = input("Please enter the maximum number of players: ")
        Online = input("Does the game have online functionality? ")
        

        game.name = Name
        game.platform = Platform
        game.genre = Genre
        game.cost = Cost
        game.number_of_players = Number_of_players
        game.online_functionality = Online      

        games.append(game)

        
        Exit = input("Enter '-1' to exit or enter to continue.")

    return games


def display_menu():
    print()
    print("***Welcome to the Computer and Video Game Database***")
    print()
    print("1. Add new games")
    print("2. Display games")
    print("3. Exit program")
    print()

def main():
    exit_program = False

    games = []
       

    try:
        filename = input("please enter the file name: ")
        games = load_games(filename)
        
        
        print(games)
        
        
    except:
        FileNotFoundError
        print("no file found")
        
    
    
    
    while not exit_program:
        display_menu()
        selected_option = int(input("Please select a menu option: "))
        print(" ")
        if selected_option == 1:
            get_game_from_user(games)
            
            
        elif selected_option == 2:
            display_games(games)
            
        elif selected_option == 3:
            save_games(games)
            exit_program = True
            
            print("You have exited the program")
        else:
            print("Please enter a valid option (1-3)")
            print()


#program

if __name__ == "__main__":
    main()
