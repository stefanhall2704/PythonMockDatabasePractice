from user import PlayerChampionships

# frontent.py will be the file that you would be creating your functions to render HTML and pass in context variables, 
# showing database data in the UI and interacting with the database through the framework of your choosing.

# Instantiating PlayerChampionships().
user = PlayerChampionships()

player_name = "Michael"
player_rings = "6 Championships"

# Adding Player.
user.add_player(player_name, player_rings)

player2_name = "Kobe"
player2_rings = "5 Championships"

# Adding Player.
user.add_player(player2_name, player2_rings)

player3_name = "Lebron"
player3_rings = "4 Championships"

# Adding Player.
user.add_player(player3_name, player3_rings)

player4_name = "Magic"
player4_rings = "4 Championships"

# Adding Player.
user.add_player(player4_name, player4_rings)

player4_rings = "5 Championships"

# Change player4_rings from "4 Championships" -> "5 Championships".
user.patch_player(player4_name, player4_rings)

player5_name = "Kareem"
playter5_rings = "6 Championships"

# Changing the entire player 4 -> player 5.
user.put_player(player4_name, player5_name, playter5_rings)

print(user.get_player(player_name))