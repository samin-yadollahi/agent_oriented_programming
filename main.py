from src.agent_model import AgentModel


def main():

    number_of_agents = int(input("please the number of agents: "))
    
    agent = AgentModel(number_of_agents)
    agent.step()


if __name__ == "__main__":
    main()