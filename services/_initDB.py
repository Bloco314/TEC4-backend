from environments import Environment
from equipments import Equipment
from users import User


def createDB():
    User.createUser()
    Environment.createEnvironment()
    Equipment.createEquipment()


createDB()
