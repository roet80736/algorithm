# 首先，创建一个列表，其中包含要覆盖的州
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
# 还需要有可供选择的广播台清单，我选择使用散列表来表示它。
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])
# 使用一个集合来存储最终选择的广播台
final_stations = set()
# 需要遍历所有的广播台，从中选择覆盖了最多的未覆盖州的广播台。将这个广播台存储在best_station中
while states_needed:
    best_station = None
    states_covered = set()
    # states_covered 是一个集合，包含该广播台覆盖的所有未覆盖的州。for循环迭代每个广播台，并确定它是否是最佳的广播台。
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station # 计算交集
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)
print(final_stations)