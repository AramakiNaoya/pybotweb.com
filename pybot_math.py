import math

def sqrt_command(command):
    sqrt, number_str = command.split()
    x = int(number_str)
    sqrt_x = math.sqrt(x)
    response = "{} ノ平方根ハ {} デス".format(x, sqrt_x)
    return response