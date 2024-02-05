from environments import Environment
from equipments import Equipment
from users import User
from horarios import Horarios

def createDB():
    User.initTable()
    Environment.initTable()
    Equipment.initTable()
    Horarios.initTable()


if __name__ == "__main__":
    createDB()
