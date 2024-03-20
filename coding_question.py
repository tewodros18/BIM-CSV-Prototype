
def maximum_saving(input_network: str) -> int:
  #parse input and create network 
  network = Network(parseInput(input_network))
  #Sum original network weights
  totalWeight = sum([i[0] for i in network.network])
  #return total sum - minium sum 
  max_saving = totalWeight - network.minimumNetworkWeight()
  return max_saving

def parseInput(input):
    inputArray = input.split("\n")
    inputArray = [i.split(",") for i in inputArray]
    edges = []
    for i in range(len(inputArray)-1):
        for j in range(len(inputArray)-1):
            if(inputArray[i][j].isnumeric()):
                edges.append((int(inputArray[i][j]),i,j))
                inputArray[j][i] = "-"
    return [edges,len(inputArray)]

class Network:
    def __init__(self,parsedInput) -> None:
        self.nodeCount = parsedInput[1]
        self.network = sorted(parsedInput[0],key=lambda x: x[0])
    def minimumNetworkWeight(self):
        minimumNetworkWeight = 0
        parent = [i for i in range(self.nodeCount)]
        rank = [1 for i in range(self.nodeCount)]
        for weight, u, v in self.network:
            if self.find(parent,u) != self.find(parent,v) :
                self.union(parent,rank,u,v)
                minimumNetworkWeight += weight
        return minimumNetworkWeight
    def find(self, parent, i): 
        if parent[i] == i:
            return i
        parent[i] = self.find(parent, parent[i]) 
        return parent[i]
    def union(self, parent, rank, x, y):
        px = self.find(parent,x)
        py = self.find(parent,y)
        if(px == py): return
        if rank[px] > rank[py]:
            parent[py] = px
            rank[px] += rank[py]
        else:
            parent[px] = py
            rank[py] += rank[px]
    

input_network = '''-,14,10,19,-,-,-
14,-,-,15,18,-,-
10,-,-,26,,29,-
19,15,26,-,16,17,21
-,18,-,16,-,-,9
-,-,29,17,-,-,25
-,-,-,21,9,25,-
'''

max_saving = maximum_saving(input_network)
print(max_saving)