# 1 把节点的所以邻居都存储到散列表
graph = {}  # 散列表
graph["start"] = {}  # 开始位置的散列表
graph["start"]["a"] = 6
graph["start"]["b"] = 2
print(graph["start"].keys())
graph["a"] = {}  # 起点a能到达哪些点的散列表
graph["a"]["fin"] = 1  # 起点a到终点的权重

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}  # 终点的散列表没有邻居
# 2 用一个散列表来存储每个节点的开销,不知道的开销设为无穷大
infinity = float("inf")  # python中表示无穷大
# 创建开销表的散列表
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity
# 3 还需要一个存储父节点的散列表
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# 4 需要一个数组,用于记录处理过的节点,因为对于同一个节点,不用处理多次
processed = []


# 算法实现思路 1:只要还有要处理的节点 --> 2: 获取离起点最近的节点 --> 3: 更新其邻居的开销  --> 4:如果有邻居的开销被更新,同时更新
# 其父节点  ---> 5:将该节点标记为处理过 回到第一点
# 找出开销最低的节点
def find_lower_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:  # 遍历所有的节点
        cost = costs[node]
        if cost < lowest_cost and node not in processed:  # 如果当前节点的开销更低且未处理过
            lowest_cost = cost  # 就将其视为开销最低的节点
            lowest_cost_node = node
    return lowest_cost_node


node = find_lower_cost_node(costs)   # 在未处理的节点中找出开销最小的节点
while node is not None:  # 这个while循环在所有节点都被处理过后结束
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys(): # 遍历当前节点的所有邻居
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:  # 如果经当前节点前往该邻居更近
            costs[n] = new_cost  # 就更新该邻居的开销
            parents[n] = node    # 同时将该邻居的父节点设置为当前节点
    processed.append(node)       # 将该节点标记为处理过
    node = find_lower_cost_node(costs)  # 找出接下来要处理的节点,并循环
print("最小的权重:", costs["fin"])
nodeTmp = "fin"
luxian = []
luxian.append(nodeTmp)
while nodeTmp != "start":
    nodeTmp = parents[nodeTmp]
    luxian.append(nodeTmp)
print(luxian)