# Clone Graph
def cloneGraph(node: 'Node') -> 'Node':
    visited = {}

    def clone(node):
        if not node:
            return node

        if node in visited:
            return visited[node]

        clone_node = Node(node.val, [])
        visited[node] = clone_node

        if node.neighbors:
            clone_node.neighbors = [clone(n) for n in node.neighbors]

        return clone_node

    return clone(node)

# Course Schedule
def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = [[] for _ in range(numCourses)]
    visited = [0 for _ in range(numCourses)]

    for x, y in prerequisites:
        graph[x].append(y)

    def dfs(i):
        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True

        visited[i] = -1

        for j in graph[i]:
            if not dfs(j):
                return False

        visited[i] = 1
        return True

    for i in range(numCourses):
        if not dfs(i):
            return False

    return True

# Pacific Atlantic Water Flow
def pacificAtlantic(matrix: List[List[int]]) -> List[List[int]]:
    if not matrix or not matrix[0]:
        return []

    def dfs(i, j, visited, prevHeight):
        if (i, j) in visited or i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] < prevHeight:
            return
        visited.add((i, j))
        for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            dfs(i + direction[0], j + direction[1], visited, matrix[i][j])

    pacific, atlantic = set(), set()
    for i in range(len(matrix)):
        dfs(i, 0, pacific, matrix[i][0])
        dfs(i, len(matrix[0]) - 1, atlantic, matrix[i][len(matrix[0]) - 1])
    for j in range(len(matrix[0])):
        dfs(0, j, pacific, matrix[0][j])
        dfs(len(matrix) - 1, j, atlantic, matrix[len(matrix) - 1][j])

    return list(pacific & atlantic)

# Number of Islands
def numIslands(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    def dfs(i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1

    return count

# Longest Consecutive Sequence
def longestConsecutive(nums: List[int]) -> int:
    nums_set = set(nums)
    max_len = 0

    for num in nums_set:
        if num - 1 not in nums_set:
            current_len = 1
            while num + current_len in nums_set:
                current_len += 1
            max_len = max(max_len, current_len)

    return max_len

# Alien Dictionary (Leetcode Premium)
def alienOrder(words: List[str]) -> str:
    graph = {}
    indegree = {}

    for word in words:
        for char in word:
            graph[char] = set()
            indegree[char] = 0

    for i in range(1, len(words)):
        word1, word2 = words[i - 1], words[i]
        min_len = min(len(word1), len(word2))
        for j in range(min_len):
            char1, char2 = word1[j], word2[j]
            if char1 != char2:
                if char2 not in graph[char1]:
                    graph[char1].add(char2)
                    indegree[char2] += 1
                break
        else:
            if len(word1) > len(word2):
                return ""

    queue = [char for char in indegree if indegree[char] == 0]
    order = []
    while queue:
        char = queue.pop(0)
        order.append(char)
        for neighbor in graph[char]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != len(indegree):
        return ""

    return "".join(order)

# Graph Valid Tree (Leetcode Premium)
def validTree(n: int, edges: List[List[int]]) -> bool:
    if len(edges) != n - 1:
        return False

    graph = {i: [] for i in range(n)}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if neighbor in visited:
                return False
            if not dfs(neighbor, node):
                return False
        return True

    return dfs(0, -1) and len(visited) == n

# Number of Connected Components in an Undirected Graph (Leetcode Premium)
def countComponents(n: int, edges: List[List[int]]) -> int:
    graph = {i: [] for i in range(n)}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)

    count = 0
    for i in range(n):
        if i not in visited:
            dfs(i)
            count += 1

    return count
