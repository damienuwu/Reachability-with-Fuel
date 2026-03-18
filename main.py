import heapq

def canReachTarget(numCities, cityConnections, chargingStations, startCity, targetCity, maxBattery):
    # bestBatteryLevel[i] stores the maximum battery we've had arriving at city i
    bestBatteryLevel = [-1] * (numCities + 1)
    bestBatteryLevel[startCity] = maxBattery
    
    # Max-heap (using negative values because Python's heapq is a min-heap by default)
    priorityQueue = [(-maxBattery, startCity)]
    
    while priorityQueue:
        currentBattery, currentCity = heapq.heappop(priorityQueue)
        currentBattery = -currentBattery
        
        # If we reached the destination city, a valid route exists!
        if currentCity == targetCity:
            return True
            
        # If we've already been to this city before with a BETTER battery level, ignore this path
        if currentBattery < bestBatteryLevel[currentCity]:
            continue
            
        # Explore outgoing roads from the current city
        for nextCity, batteryCost in cityConnections[currentCity]:
            
            # Check if our car has enough battery to survive this specific road
            if currentBattery >= batteryCost:
                newBattery = currentBattery - batteryCost
                
                # Instantly refill to full capacity if the next city has a supercharger
                if nextCity in chargingStations:
                    newBattery = maxBattery
                
                # If arriving at this next city gives us a new "high score" for battery life here:
                if newBattery > bestBatteryLevel[nextCity]:
                    # Update the record book
                    bestBatteryLevel[nextCity] = newBattery
                    # Put it in the queue to explore later
                    heapq.heappush(priorityQueue, (-newBattery, nextCity))
                    
    # If the queue empties and we never hit the target city, we are stranded.
    return False

# Helper function to build the map (adjacency list)
def buildMap(numCities, roads):
    cityConnections = {i: [] for i in range(1, numCities + 1)}
    for start, end, cost in roads:
        cityConnections[start].append((end, cost))
    return cityConnections

if __name__ == "__main__":
    print("Running test cases for EV Routing Simulation...\n")
    
    # Map 1: Reachable without needing to charge
    map1 = buildMap(3, [(1, 2, 2), (2, 3, 2)])
    print("Test 1 (Expected True):", canReachTarget(3, map1, set(), startCity=1, targetCity=3, maxBattery=5))
    
    # Map 2: Reachable ONLY if we use the charging station at city 2
    map2 = buildMap(3, [(1, 2, 4), (2, 3, 4)])
    print("Test 2 (Expected True):", canReachTarget(3, map2, chargingStations={2}, startCity=1, targetCity=3, maxBattery=5))
    
    # Map 3: Unreachable because the very first road costs 6, but max battery is only 5
    map3 = buildMap(3, [(1, 2, 6), (2, 3, 1)])
    print("Test 3 (Expected False):", canReachTarget(3, map3, chargingStations={2}, startCity=1, targetCity=3, maxBattery=5))