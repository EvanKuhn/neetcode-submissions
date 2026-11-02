# Are we just looking for cycles?

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        # Build dict, mapping course to all its prerequisites
        course_to_prereqs = defaultdict(list)
        for a,b in prerequisites:
            if a == b:
                return False
            course_to_prereqs[a].append(b)

        print(course_to_prereqs)

        # Helper method to search prereqs
        all_visited = set()

        def dfs(course: int, path: set) -> bool:            
            if course in path:
                return False

            # Update path
            path.add(course)

            # Record that this course was visited
            all_visited.add(course)

            # Search all prereqs, as a separate path
            for pr in course_to_prereqs[course]:
                if course == pr:
                    return False
                if not dfs(pr, path.copy()):
                    return False

            # Mark course as "done" by clearing its prereqs
            course_to_prereqs[course] = []
            return True
        
        for course, _ in prerequisites:
            if course not in all_visited:
                if not dfs(course, set()):
                    return False

        return True
