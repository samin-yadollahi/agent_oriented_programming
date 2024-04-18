import mesa


class Agent(mesa.Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)


    def add_numbers(self, num1, num2):
        return num1+num2
    

    def deffirence(self, num1, num2):
        return num1-num2
    

    def multiply(self, num1, num2):
        return num1*num2
    