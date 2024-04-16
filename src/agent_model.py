import mesa
from src.computation_agent import ComputationAgent


class AgentModel(mesa.Model):

    def __init__(self, N=2):
        self.agents_numbers = N


        for i in range(self.agents_numbers):
            agent = ComputationAgent()