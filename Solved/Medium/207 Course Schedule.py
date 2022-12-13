# Course Schedule

# https://leetcode.com/problems/course-schedule/

# DFS - Depth First Search

def canFinishDFS(numCourses, prerequisites):
    preDict = {i:[] for i in range(numCourses)}
    for course, pre in prerequisites:
        preDict[course].append(pre)
    visitSet = set()

    def dfs(course):
        if course in visitSet: return False
        if preDict[course] == []: return True
        visitSet.add(course)

        for pre in preDict[course]:
            if not dfs(pre):return False

        preDict[course] = []
        visitSet.remove(course)
        return True
    
    for course in range(numCourses):
        if not dfs(course): return False
    return True


def canFinishBFS(numCourses,prerequisites):
    complete = {num for num in range(numCourses)}
    graph = {}
    for course, prereq in prerequisites:
        if course in complete:
            complete.remove(course)
        if graph.get(course):
            graph[course].add(prereq)
        else:
            graph[course] = {prereq}

    queue = []

    def topologicalSort(course, stack):
        if course not in complete:
            for nextCourse in graph.get(course):
                if nextCourse in stack:
                    continue
                stack.add(course)
                topologicalSort(nextCourse, stack)

            queue.append(course)
    for course in graph:
        topologicalSort(course, set())
    for course in queue:
        if graph[course]-complete:
            return False
        complete.add(course)
    return len(complete)==numCourses