class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dct = [[position[i], speed[i]] for i in range(len(position))]
        time = [(target - pair[0]) / pair[1] for pair in sorted(dct, reverse= True)]
        temp = []
        for idx in range(len(time)):    
            if not temp or time[idx] > temp[-1]:
                temp.append(time[idx])
        return len(temp)
