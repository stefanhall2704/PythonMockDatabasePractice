from database import Database


class PlayerChampionships:
    # The database variable is our Database connection
    database = Database()

    # The "add_user" function is taking in 2 parameters: player_name, championships.
    # We are adding the championships value to the database by player_name.
    def add_player(self, player_name, championships):
        self.database.add(player_name, championships)

    # The "get_user" function is taking in 1 parameters: player_name.
    # This will return the championships by the players name.
    def get_player(self, player_name):
        return self.database.get(player_name)
 
    # The "delete_user" function is taking in 1 parameters: player_name.
    # This will delete the player and championships by player_name.
    def delete_player(self, player_name):
        self.database.delete(player_name)

    # The "patch_user" function is taking in 2 parameters: player_name, championships.
    # This will update the championships by player_name.
    def patch_player(self, player_name, championships):
        self.database.patch(player_name, championships)

    # The "put_user" function is taking in 3 parameters: player_name, new_player_name, championships.
    # This is going to update the player_name and the championships and dispose of player_name.
    def put_player(self, player_name, new_player_name, championships):
        self.database.put(player_name, new_player_name, championships)
