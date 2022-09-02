class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # if n == 0: return len(tasks)
        # else:
        #     sch = [tasks.pop(0)]
        #     tasks.sort()
        #     while len(tasks) != 0:
        #         if tasks[0] == sch[-1]:
        #             sch.append(tasks.pop())
        #         else: sch.append(tasks.pop(0))
        # print(sch)
        
        time=0
        map_={}
        for i in tasks:
            if i in map_:
                map_[i]+=1
            else:
                map_[i]=1
        new_list=list(map_.items())
        heap=[]
        for x,y in new_list:
            heap.append([-y,x])
        heapify(heap)
        wait=n
        while len(heap)>=1:
            val1,char1=heappop(heap)
            to_add=[]
            val1=-1*val1
            if val1:
                time+=1
            else:
                continue
            while len(heap)>=1 and wait:
                val,char=heappop(heap)
                val=-1*val
                if not val:
                    break
                wait-=1
                if val-1:
                    to_add.append([val-1,char])
                time+=1
            for x,y in to_add:
                heappush(heap,[-x,y])
            heappush(heap,[-(val1-1),char1])
            
            while wait and len(heap) >=1 and heap[0][0]!=0:
                time+=1
                wait-=1
            wait=n
                
        return time
                    
