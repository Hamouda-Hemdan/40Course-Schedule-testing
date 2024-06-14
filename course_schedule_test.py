import unittest
from collections import defaultdict, deque

def canFinish(numCourses, prerequisites):
    """
    Determines if all courses can be finished given the prerequisites.

    Args:
    numCourses (int): Total number of courses.
    prerequisites (List[List[int]]): List of prerequisite pairs.

    Returns:
    bool: True if all courses can be finished, False otherwise.
    """
    graph = defaultdict(list)
    indegree = {i: 0 for i in range(numCourses)}
    
    # Build the graph and compute the in-degrees of each node
    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1
    
    # Initialize the queue with nodes having in-degree of 0
    queue = deque([i for i in indegree if indegree[i] == 0])
    
    count = 0
    while queue:
        node = queue.popleft()
        count += 1
        
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
                
    return count == numCourses

class TestCourseSchedule(unittest.TestCase):
    """
    Unit test class for canFinish function.
    """
    
    def test_example1(self):
        """Test case from the problem statement (expected True)."""
        self.assertTrue(canFinish(2, [[1,0]]))
    
    def test_example2(self):
        """Test case from the problem statement with a cycle (expected False)."""
        self.assertFalse(canFinish(2, [[1,0], [0,1]]))
    
    def test_no_prerequisites(self):
        """Test with no prerequisites (expected True)."""
        self.assertTrue(canFinish(3, []))
    
    def test_single_course(self):
        """Test with a single course (expected True)."""
        self.assertTrue(canFinish(1, []))
    
    def test_circular_dependency(self):
        """Test with a circular dependency among three courses (expected False)."""
        self.assertFalse(canFinish(3, [[0,1], [1,2], [2,0]]))
    
    def test_multiple_courses_with_no_circular_dependency(self):
        """Test with multiple courses and no circular dependency (expected True)."""
        self.assertTrue(canFinish(4, [[1,0], [2,1], [3,2]]))
    
    def test_all_courses_interdependent(self):
        """Test with all courses interdependent creating a cycle (expected False)."""
        self.assertFalse(canFinish(3, [[0,1], [1,2], [2,0], [0,2]]))
    
    def test_large_input(self):
        """Test with large number of courses with a simple linear dependency (expected True)."""
        self.assertTrue(canFinish(2000, [[i, i+1] for i in range(1999)]))
    
    def test_disconnected_graph(self):
        """Test with a disconnected graph (expected True)."""
        self.assertTrue(canFinish(5, [[1, 0], [3, 2]]))
    
    def test_single_chain(self):
        """Test with a single long chain of dependencies (expected True)."""
        self.assertTrue(canFinish(5, [[1, 0], [2, 1], [3, 2], [4, 3]]))
    
    def test_single_course_with_self_dependency(self):
        """Test with a single course having a self-dependency (expected False)."""
        self.assertFalse(canFinish(1, [[0, 0]]))
    
    def test_two_disconnected_components(self):
        """Test with two disconnected components (expected True)."""
        self.assertTrue(canFinish(6, [[1, 0], [2, 1], [4, 3], [5, 4]]))
    
    def test_long_chain_with_one_cycle(self):
        """Test with a long chain with one cycle (expected False)."""
        self.assertFalse(canFinish(4, [[1, 0], [2, 1], [3, 2], [1, 3]]))
    
    def test_empty_course_list(self):
        """Test with no courses (expected True)."""
        self.assertTrue(canFinish(0, []))
    
    def test_all_courses_with_no_dependencies(self):
        """Test with all courses having no dependencies (expected True)."""
        self.assertTrue(canFinish(5, []))
    
    def test_large_input_with_circular_dependency(self):
        """Test with large input and a circular dependency (expected False)."""
        self.assertFalse(canFinish(2000, [[i, i+1] for i in range(1999)] + [[1999, 0]]))
    
    def test_large_number_of_courses_with_random_dependencies(self):
        """Test with large number of courses and random dependencies (expected False)."""
        prerequisites = [[i, (i+1) % 2000] for i in range(2000) if i % 2 == 0]
        self.assertFalse(canFinish(2000, prerequisites))

if __name__ == '__main__':
    unittest.main()
