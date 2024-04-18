import mesa
import random

from src.agent import Agent


class AgentModel(mesa.Model):

    def __init__(self, N=2):
        super().__init__()
        self.agents_numbers = N

        for i in range(self.agents_numbers):
            unique_id = random.randint(1, 99)
            agent = Agent(i, self)
        