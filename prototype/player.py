class Player:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.name = "PLAYER"
        self.current_location_id = 0

    def set_name(self, name):
        self.name = name

    def set_location_id(self, location_id):
        self.current_location_id = location_id

    def __str__(self):
        return f"Player: {self.name}, location: {self.current_location_id}"
