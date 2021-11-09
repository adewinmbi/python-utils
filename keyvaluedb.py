import json
import os

class DataBase():
    def __init__(self, path):
        self.path = os.path.expanduser(path)
        self.load(self.path)

    def load(self, path):
        if os.path.exists(path):
            self._load()
        else:
            self.db = {} # Create key, value database 
        return True

    def _load(self):
        self.db = json.load(open(self.path, "r"))

    def dump(self): # Call every time dictionary is changed
        try:
            json.dump(self.db, open(self.location, "w+"))
            return True
        except:
            return False

    def resetdb(self):
        self.db = {}
        self.dump()
        print("Database cleared and reset.")

    def set(self, key, value):
        try:
            self.db[str(key)] = value
            self.dump()
        except Exception as e:
            print("Error setting database value:", str(e))

    def get(self, key):
        try:
            return self.db[key]
        except Exception as e:
            print("Error retrieving value from database:", str(e))
            return False
        
    def delete(self, key):
        if key in self.db:
            del self.db[key]
            self.dump()
            return True
        else:
            return False
