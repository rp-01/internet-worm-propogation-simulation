from enum import Enum
import random
import numpy

SIM_NUM = 3
OMEGA = 100000
SIM_TIME = 400
node_status = []
infected_num = 1
current_infected = 0
sim_result = numpy.asanyarray([[1000 for x in range(SIM_TIME)] for x in range(SIM_NUM)])

class Node_enum:
    immune = 0
    infectious = 1
    susceptible = 2

# initialize ip array and variables
def node_modify():
    print("\nSetting up lists and variables for simulation....")
    for i in range(OMEGA + 1):
        node_status.insert(i, Node_enum.immune)
    node_status.insert(1001, Node_enum.infectious)
    for j in range(99):
        for k in range(1, 11):
            i = k + j * 1000
            node_status.insert(i, Node_enum.susceptible)

# begin simulation
for i in range(0, SIM_NUM):
    print("---------------------------")
    print("\nBeginning Simulation {}".format(i+1))

    node_modify()
    for j in range(SIM_TIME):

        # scan 3 random ip per infected computer
        current_infected = infected_num
        for k in range(current_infected):
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
            # stop newly infected ip from spreading worm in current time tick


        # save # of infected computer at current time rick
        sim_result[i][j] = infected_num

        # stop simulation if max number reached
        if infected_num == 1000:
            print("Last time tick: {}".format(j))
            print("{} infected Computers at time tick: {}".format(infected_num,j))
            break

    # reset variable for next sim. run
    infected_num = 1
    node_status.clear()
    print("---------------------------")
numpy.savetxt('random_scanner_output.csv', sim_result, delimiter=",", fmt="%d")
print("Simulation Results saved in random_scan_results.csv")