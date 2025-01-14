from typing import List 

def canFinish(numCourses, prerequisites):
    #create adjacency list
    graph = [[] for _ in range(numCourses)]
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    #track visited courses and current path 
    visited = set()
    path = set()

    def dfs(course):
        #if course is in current path, we found a cycle 
        if course in path:
            return False 
        #if couser is already visited, it's safe    
        if course in visited:
            return True
        #add course to current path 
        path.add(course)
        #check all prerequisites
        for prereq in graph[course]:
            if not dfs(prereq):
                return False 
        #remove course from current path 
        path.remove(course)
        #mark course as visited 
        visited.add(course)
        return True
    
    #check all courses 
    for course in range(numCourses):
        if not dfs(course):
            return False 
    return True

print(canFinish(2, [[1,0], [0,1]]))