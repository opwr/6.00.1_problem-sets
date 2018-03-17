###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # create a list: a sorted version of all the cows according to their weight (descending order)
    sortedCows = sorted(cows.items(), key = lambda x: x[1])[::-1]    

    # initial set up
    totalWeight = 0
    result = []
    countedCows = []
    trip = []
            
    while len(countedCows) < len(sortedCows):
        for i in range(len(sortedCows)):
            # if the current relevant 'i' cow fits to the limit
            if totalWeight + sortedCows[i][1] <= limit and sortedCows[i][0] not in countedCows:
                # append the cow in the existing trip list and update the weight
                if len(trip) != 0:
                    trip.append(sortedCows[i][0])
                    countedCows.append(sortedCows[i][0])
                    totalWeight += sortedCows[i][1]
                    
                    # if it's the last, wrap up the trip anyway
                    if i == len(sortedCows) - 1:
                        result.append(trip)
                        totalWeight = 0
                        trip = []
                # append the cow in the new trip
                else: 
                    trip = []
                    trip.append(sortedCows[i][0])
                    countedCows.append(sortedCows[i][0])
                    totalWeight += sortedCows[i][1]
            # if the current 'i' cow doesn't fit:
            else:
                # if iteration reaches the end, wrap up the trip
                if i == len(sortedCows) - 1:
                    result.append(trip)
                    totalWeight = 0
                    trip = []
                pass
    return result
    

# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # initial setup
    bestCount = len(cows)
    bestCase = []
    countTrips = 0
    allCases = []
    for item in (get_partitions(cows)):
        allCases.append(item)
        
    for case in allCases:
        # print('CASE: ', case, '\n')
        for trip in case:
            # print('     TRIP: ', trip, '\n')
            # validate that this trip is legitimate, if so, count the trip
            cowWeightSum = 0
            for cow in trip:
                cowWeightSum += cows[cow]
                # print('     cowWeightSum: ', cowWeightSum)
            
            if cowWeightSum <= limit:
                countTrips += 1
                # print('     countTrips: ', countTrips, '\n')               
                # if the enumeration reaches to the last one
                if trip == case[len(case)-1]:
                    # print('     if the enumeration reaches to the last one', '\n')
                    if countTrips <= bestCount:
                        bestCount = countTrips
                        bestCase = case
                        countTrips = 0
                    countTrips = 0
            else:
                countTrips = 0
                break
    return bestCase
        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows("ps1_cow_data.txt")
    limit = 10

    
    ## code to be timed
    start = time.time()
    greedy_cow_transport(cows, limit=10)    
    end = time.time()
    print('greedy', end - start)

    start = time.time()
    brute_force_cow_transport(cows,limit=10)
    end = time.time()
    print('brute', end - start)
