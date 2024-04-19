import mesa
import random

class Agent(mesa.Agent):

    def __init__(self, unique_id, model, num_1=2, num_2=2, ops="+"):
        super().__init__(unique_id, model)
        
        self.num_1 = num_1
        self.num_2 = num_2
        self.ops = ops
        self.result = 0


    def step(self):

        if (self.ops == '+'):
            other_agent = self.random.choice(self.model.schedule.agents)

            if other_agent is not None:
                other_agent.result = self.num_1 + self.num_2

        print(f"Hi! I'm agent number {str(self.unique_id)} and the result is {other_agent.result}.")


    