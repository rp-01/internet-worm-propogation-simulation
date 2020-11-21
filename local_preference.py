from enum import Enum
import random
import numpy
SIM_NUM = 3
OMEGA = 100000
SIM_TIME = 100
node_status = []
infected_num = 1
current_infected = 0

# initialize array to record results
# trailing elements have value 1000 for graph requirements
sim_result = numpy.asanyarray([[1000 for x in range(SIM_TIME)] for x in range(SIM_NUM)])

# assign integer value to status
class Node_enum:
    immune = 0
    infectious = 1
    susceptible = 2

#sunction to initialize variables
def node_modify():
    print("\nSetting up lists and variables for simulation....")
    for i in range(OMEGA + 1):
        node_status.insert(i, Node_enum.immune)
    node_status.insert(1001, Node_enum.infectious)
    for j in range(99):
        for k in range(1, 11):
            i = k + j * 1000
            node_status.insert(i, Node_enum.susceptible)

for i in range(0, SIM_NUM):
    print("---------------------------")
    print("\nBeginning Simulation {}".format(i+1))

    node_modify()
    for j in range(SIM_TIME):
        current_infected = infected_num
        for k in range(current_infected):
            rand_prob = random.uniform(0,1)

            if rand_prob <= 0.80:
                for l in range(0, 3):
                    rand = random.randrange(infected_num-10, infected_num+10)
                    if node_status[rand] == Node_enum.immune:
                        continue
                    elif node_status[rand] == Node_enum.infectious:
                        continue
                    elif node_status[rand] == Node_enum.susceptible:
                        node_status.insert(rand, Node_enum.infectious)
                        infected_num = infected_num + 1

            elif rand_prob <= 0.20:
                for l in range(0, 3):
                    rand = random.randrange(1, len(node_status))
                    if node_status[rand] == Node_enum.immune:
                        continue
                    elif node_status[rand] == Node_enum.infectious:
                        continue
                    elif node_status[rand] == Node_enum.susceptible:
                        node_status.insert(rand, Node_enum.infectious)
                        infected_num = infected_num + 1
            if infected_num == 1000:
                break

        sim_result[i][j] = infected_num

        if infected_num == 1000:
            print("Last time tick: {}".format(j))
            print("{} infected Computers at time tick: {}".format(infected_num,j))
            break

    print("\n Resetting variable for next simulation....")
    node_status.clear()
    infected_num = 1
    print("---------------------------")
# Save results to csv file
numpy.savetxt('local_scanner_output.csv', sim_result, delimiter=",", fmt="%d")
print("Simulation Results saved in local_preference_results.csv")