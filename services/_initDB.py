from Environments import Environment
from Equipments import Equipment
from Users import User
from horarios import Horarios

def createDB():
    User.initTable()
    Environment.initTable()
    Equipment.initTable()
    Horarios.initTable()


if __name__ == "__main__":
    createDB()
