from database import Database


class PlayerChampionships:
    # The database variable is our Database connection
    database = Database()

    # The "add_user" function is taking in 2 parameters: player_name, championships.
    # We are adding the championships value to the database by player_name.
    def add_user(self, player_name, championships):
        self.database.add(player_name, championships)

    # The "get_user" function is taking in 1 parameters: player_name.
    # This will return the championships by the players name.
    def get_user(self, player_name):
        return self.database.get(player_name)

    # The "delete_user" function is taking in 1 parameters: player_name.
    # This will delete the player and championships by player_name.
    def delete_user(self, player_name):
        self.database.delete(player_name)

    # The "patch_user" function is taking in 2 parameters: player_name, championships.
    # This will update the championships by player_name.
    def patch_user(self, player_name, championships):
        self.database.patch(player_name, championships)

    # The "put_user" function is taking in 3 parameters: player_name, new_player_name, championships.
    # This is going to update the player_name and the championships and dispose of player_name.
    def put_user(self, player_name, new_player_name, championships):
        self.database.put(player_name, new_player_name, championships)


# Instantiating PlayerChampionships().
user = PlayerChampionships()

player_name = "Michael"
player_rings = "6 Championships"

# Adding Player.
user.add_user(player_name, player_rings)

player2_name = "Kobe"
player2_rings = "5 Championships"

# Adding Player.
user.add_user(player2_name, player2_rings)

player3_name = "Lebron"
player3_rings = "4 Championships"

# Adding Player.
user.add_user(player3_name, player3_rings)

player4_name = "Magic"
player4_rings = "4 Championships"

# Adding Player.
user.add_user(player4_name, player4_rings)

player4_rings = "5 Championships"

# Change player4_rings from "4 Championships" -> "5 Championships".
user.patch_user(player4_name, player4_rings)

player5_name = "Kareem"
playter5_rings = "6 Championships"

# Changing the entire player 4 -> player 5.
user.put_user(player4_name, player5_name, playter5_rings)
