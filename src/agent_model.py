import mesa
import random

from src.computation_agent import ComputationAgent


class AgentModel(mesa.Model):

    def __init__(self, N=2):
        self.agents_numbers = N


        for i in range(self.agents_numbers):
            unique_id = random.randint(1, 99)
            agent = ComputationAgent(i, self)