# datbase.py is meant to have all the CRUD functions to the database.
class Database:
    # We are using the database dictionary variable to be used as a Database.
    database = dict()

    # The "add" function is taking in 2 parameters: key, value.
    # We can think of it as "key" is the PRIMARY KEY.
    # We can think value is a value within this "row" of the database.
    # Than finally we add the "value" in the "database" along with its "PRIMARY KEY", "key".
    def add(self, key, value):
        self.database[key] = value

    # The "get" function is taking in a parameter: key.
    # This is going to ensure the "key" exists in the database.
    # If the "key" exists in the database, it will return the value.
    # If the "key" does not exist in the database, it will return None.
    def get(self, key):
        if key in self.database:
            value = self.database[key]
            return value
        else:
            return None

    # The "delete" function is taking in the parameter: key.
    # This is going to ensure the "key" exists in the database.
    # We are going to remove the "key" & "value" from the database by "key".
    # If the "key" does not exist in the database, it will return None.
    def delete(self, key):
        if key in self.database:
            self.database.pop(key)
        else:
            return None

    # The "patch" function is taking in 2 parameters: key, value.
    # This is going to ensure the "key" exists in the database.
    # We are going to update the "value" in the database by "key".
    # If the "key" does not exist in the database, it will return None.
    def patch(self, key, value):
        if key in self.database:
            self.database[key] = value
        else:
            return None

    # The "patch" function is taking in 3 parameters: key, new_key, value.
    # This is going to ensure the "key" exists in the database.
    # We are first going to change the "key" value in the database to "new_key".
    # We are going to update the "value" in the database by "new_key".
    # If the "key" does not exist in the database, it will return None.
    def put(self, key, new_key, value):
        if key in self.database:
            self.database[new_key] = self.database.pop(key)
            self.database[new_key] = value
        else:
            return None
