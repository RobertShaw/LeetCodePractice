class Solution:
        
    def bfsLevels(self,graph: List[List[int]], player: int, end: int) -> List[int]:
        seen = {}
        seen[player] = 0
        nodesToCheck = [player]
        
        levels = {}
        
        while nodesToCheck:
            
            current_space = nodesToCheck.pop(0)
            if current_space not in seen:
                seen[current_space] = seen[current_space] + 1
            for second in graph[current_space]:
                if second not in seen:
                    seen[second] = seen[current_space] + 1
                    nodesToCheck.append(second)
                if second == end and current_space not in levels:
                    levels[current_space] = seen[current_space]
        
        return levels
    
    def bfsLevel(self,graph: List[List[int]], player: int, end: int) -> int:
        seen = {}
        seen[player] = 0
        nodesToCheck = [player]
      
        
        while nodesToCheck:
            
            current_space = nodesToCheck.pop(0)
            if current_space not in seen:
                seen[current_space] = seen[current_space] + 1
            for second in graph[current_space]:
                if second not in seen:
                    seen[second] = seen[current_space] + 1
                    nodesToCheck.append(second)
                if second == end:
                    return seen[second]
        
        return -1
    def isInBigLoop(self,graph: List[List[int]], current: int) -> bool:
        for adj in graph[current]:
            for nextAdj in graph[adj]:
                if nextAdj in graph[current]:
                    return False
        if len(graph[current]) < 2:
            return False
        seen = set([])
        return self.isInBigLoopHelper(graph, current, seen, 0, current)
       
            
        
    def isInBigLoopHelper(self,graph: List[List[int]], current: int, seen, level, original) -> bool:
        for adj in graph[current]:
            if adj != 0:
                if adj == original and level >= 3:
                    return True
                if adj not in seen:
                    seen.add(adj)
                    if self.isInBigLoopHelper(graph, adj, seen, level+1, original):
                        return True
                    seen.remove(adj)
        return False
        
        
    def catMouseGame(self, graph: List[List[int]]) -> int:
        if 0 in graph[1]:
            return 1
    
        mouseLevels = self.bfsLevels(graph, 1,0)
        catLevels = self.bfsLevels(graph, 2,0)
        for adjacentHole in graph[0]:
            if mouseLevels[adjacentHole] < catLevels[adjacentHole]:
                return 1
            
        bigLoop = []
        for x in range(len(graph)):
            if self.isInBigLoop(graph, x) and self.bfsLevel(graph, 1,x) < self.bfsLevel(graph, 2,x):
                print(x)
                print( self.bfsLevel(graph, 1,x))
                print( self.bfsLevel(graph, 2,x))
                print("stop")
                return 0
                
        
        return 2
        
        
        
   
