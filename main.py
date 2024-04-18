from src.agent_model import AgentModel


def main():

    number_of_agents = int(input("please the number of agents: "))
    
    agent = AgentModel(number_of_agents)

    for i in range(number_of_agents):
        print(agent)
        
    return agent


main()