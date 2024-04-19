import mesa
import random

from src.agent import Agent


class AgentModel(mesa.Model):

    def __init__(self, N=2):
        super().__init__()
        self.agents_numbers = N
        self.schedule = mesa.time.RandomActivation(self)    # Create the scheduler and assign to the modle

        for i in range(self.agents_numbers):
            a = Agent(i, self)
            self.schedule.add(a)    # Add the agent to the scheduler



    def step(self):
        """ Advance the model ONE step """

        self.schedule.step()
        