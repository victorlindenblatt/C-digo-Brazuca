class Student:
    def __init__(self, name, home):
        if not name:
            raise ValueError("Name was not given")
        if home not in ["Vila Isabel", "Rio de Janeiro", "Rio"]:
            raise ValueError("Invalid home")
        self.name = name
        self.home = home