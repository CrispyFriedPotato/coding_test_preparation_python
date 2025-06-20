# topology sort

from collections import deque
import copy

def find_parent(parent,a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
# 노드 개수 입력
n = int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0]*(n+1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for _ in range(n+1)]

# 각 강의 시간을 0으로 초기화
time = [0] * (n+1)

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1,n+1):
    temp = list(map(int, input().split()))
    time[i] = temp[0]
    # if len(temp) == 2:
    #     lessons[i].append(temp[0])
    # else:
    #     lessons[i].append(temp[0])
    #     for j in temp[1:]:
    #         if j == -1:
    #             continue
    #         union(parent,i,j)
    for x in temp[1:-1]:
        indegree[i] += 1
        graph[x].append(i)
        
def topology_sort():
    result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
    q = deque()
    
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i])
            indegree[i] -= 1
            
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i])
    
topology_sort()      
# for i in range(1,n+1):
#     if find_parent(parent, i) != i:
#         print(lessons[find_parent(parent,i)][0]+lessons[i][0])
#     else:
#         print(lessons[i][0])

