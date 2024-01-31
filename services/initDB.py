from Environments import Environment
from Equipments import Equipment
from Users import User


def createDB():
    User.createUser()
    Environment.createEnvironment()
    Equipment.createEquipment()


createDB()
