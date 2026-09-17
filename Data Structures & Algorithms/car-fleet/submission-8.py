class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speedDict = {}
        for i in range(len(position)):
            val = position[i]
            speedDict[val] = speed[i]
        position = sorted(position)  
        fleets = [[(target - position[-1])/speedDict[position[-1]]]]
        # we need to check every car in reverse position order
        #and check if it can join the fleet/cars infornt of it
        for i in range(1,len(position)):
            flag = 0 
            current_car_pos = position[-1-i]
            curr_time = (target - current_car_pos)/speedDict[current_car_pos]
            for fleet in fleets:
                fleet_time = fleet[0]
                if fleet_time >= curr_time:
                    fleet.append(fleet_time)
                    flag = 1
                    break
            if flag==0:
                fleets.append([curr_time])
        return len(fleets)