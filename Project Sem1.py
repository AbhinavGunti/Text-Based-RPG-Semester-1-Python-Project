""" 8X7 Map (8 rows and7 columns)
    Total=56
    Floor=23
    Room=3
    Enemy=3
    Start=1
    Wall=26"""
"""Start=(4,3)
    (x,y)
    (row,column)"""

map=[["Wall","Wall","Wall","Wall","Wall","Wall","Wall"],
    ["Wall","Floor","Floor","Floor","Room","Floor","Wall"],
    ["Wall","Floor","Room","Floor","Floor","Floor","Wall"],
    ["Wall","Floor","Floor","Floor","Enemy","Floor","Wall"],
    ["Wall","Enemy","Floor","Start","Floor","Floor","Wall"],
    ["Wall","Floor","Floor","Floor","Room","Floor","Wall"],
    ["Wall","Floor","Floor","Enemy","Floor","Floor","Wall"],
    ["Wall","Wall","Wall","Wall","Wall","Wall","Wall"]]
map_row=4
map_column=3
gold_coins=0
player_health=100
player_score=0
map_walls=[(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(1,0),(2,0),
           (3,0),(4,0),(5,0),(6,0),(7,0),(1,6),(2,6),(3,6),(4,6),
           (5,6),(6,6),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6)]
def player_movement(player_input):
    global map_row
    global map_column
    #def movement(player_input):
    corodinates =map_row, map_column
    #if corodinates in map_walls==False:
    if player_input=="UP":
        if corodinates not in [(1,1),(1,2),(1,3),(1,4),(1,5)]:
            map_row=map_row-1
        else:
            print("There is a wall in front of you and cannot proceed in that direction!")
            player_input = input("Enter your option (Down,Left,Right,Health,Gold Coins,Quit): ").upper().strip()
            player_movement(player_input)
    elif player_input=="DOWN":
        if corodinates not in [(6,1), (6,2), (6,3), (6,4), (6,5)]:
            map_row=map_row+1
        else:
            print("There is a wall in front of you and cannot proceed in that direction!")
            player_input = input("Enter your option (Up,Left,Right,Health,Gold Coins,Quit): ").upper().strip()
            player_movement(player_input)
    elif player_input=="RIGHT":
        if corodinates not in [(1,5), (2,5), (3,5), (4,5), (5,5),(6,5)]:
            map_column=map_column+1
        else:
            print("There is a wall in front of you and cannot proceed in that direction!")
            player_input = input("Enter your option (Up,Down,Left,Health,Gold Coins,Quit): ").upper().strip()
            player_movement(player_input)
    elif player_input=="LEFT":
        if corodinates not in [(1,1), (2,1), (3,1), (4,1), (5,1), (6,1)]:
            map_column=map_column-1
        else:
            print("There is a wall in front of you and cannot proceed in that direction!")
            player_input = input("Enter your option (Up,Down,Right,Health,Gold Coins,Quit): ").upper().strip()
            player_movement(player_input)
    elif player_input=="HEALTH":
        print(player_health)
    elif player_input=="GOLD COINS":
        print(gold_coins)
    elif player_input=="QUIT":
        print("Thank You for playing the game!")
        exit()
    else:
        player_input = input("Please enter a valid input! (Up,Down,Left,Right,Health,Gold Coins,Quit): ").upper().strip()
        player_movement(player_input)


def player_interaction():
    global gold_coins
    global player_health
    def room():
        global gold_coins
        player_input=input("You have entered a room! Would you like to explore? (Yes/No)").upper().strip()
        if player_input=="YES":
            print("You have found a sack containing 100 gold coins!")
            gold_coins=gold_coins+100
            print("Your Gold Coins : ",gold_coins)
        elif player_input=="NO":
            print("You chose not to explore the room ")
            player_input = input("Enter your option (Up,Down,Left,Right,Health,Gold Coins,Quit): ").upper().strip()
            player_movement(player_input)
        else:
            print("Please a valid input!")
            room()
    def enemy():
        global player_health
        global player_score
        player_input=input("You have encountered an enemy! Would you like to fight (Yes/No) : ").upper().strip()
        if player_input=="YES":
            print("You fought with the enemy and won!")
            player_score=player_score+100
            print("Your score : ",player_score)
        elif player_input=="NO":
            print("You chose to flee!")
            player_health=player_health-20
            print("Your health : ",player_health)
        else:
            print("Please enter a valid input!")
            enemy()
    if map[map_row][map_column] == "Room":
        room()
    elif map[map_row][map_column]=="Enemy":
        enemy()


while True:
    player_input=input("Enter your option (Up,Down,Left,Right,Health,Gold Coins,Quit): ").upper().strip()
    player_movement(player_input)
    print(map_row,map_column)
    player_interaction()

"""
Explanation:
Map is implemented using nested list(2D Array)
There are 4 tiles-Floor,Room,Enemy,Start
Start is where u are present on the map inititially (4,3)==(row,colomn)
Enemy tiltes are where the enimies are present
Room tiles are where Rooms are present
Enemy-
when u come across an enemy== Fight/do not fight
fight=Score increases by 100
Do not fight=Health decreases by 20
Room-
when you come across a room==Explore/Do not explore
explore=100 gold coins
do not explore=nothing happens
"""