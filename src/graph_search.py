import numpy as np
from collections import deque
from .graph import Cell
from .utils import trace_path

"""
General graph search instructions:

First, define the correct data type to keep track of your visited cells
and add the start cell to it. If you need to initialize any properties
of the start cell, do that too.

Next, implement the graph search function. When you find a path, use the
trace_path() function to return a path given the goal cell and the graph. You
must have kept track of the parent of each node correctly and have implemented
the graph.get_parent() function for this to work. If you do not find a path,
return an empty list.

To visualize which cells are visited in the navigation webapp, save each
visited cell in the list in the graph class as follows:
     graph.visited_cells.append(Cell(cell_i, cell_j))
where cell_i and cell_j are the cell indices of the visited cell you want to
visualize.
"""


def depth_first_search(graph, start, goal):
    """Depth First Search (DFS) algorithm. This algorithm is optional for P3.
    Args:
        graph: The graph class.
        start: Start cell as a Cell object.
        goal: Goal cell as a Cell object.
    """
    graph.init_graph()  # Make sure all the node values are reset.

    """TODO (P3): Implement DFS (optional)."""

    # If no path was found, return an empty list.
    return []


def breadth_first_search(graph, start, goal):
    """Breadth First Search (BFS) algorithm.
    Args:
        graph: The graph class.
        start: Start cell as a Cell object.
        goal: Goal cell as a Cell object.
    """
    graph.init_graph()  # Make sure all the node values are reset.
    
    # Queue (FIFO) for BFS
    q = deque()

    # Start and goal indices
    si, sj = start.i, start.j
    gi, gj = goal.i, goal.j

    # Optional: if start or goal are in collision, abort
    if graph.check_collision(si, sj) or graph.check_collision(gi, gj):
        return []

    # Initialize the start node
    graph.visited[sj, si] = True
    graph.dist[sj, si] = 0.0
    graph.parent_i[sj, si] = -1
    graph.parent_j[sj, si] = -1

    # Log start as visited for visualization
    graph.visited_cells.append(Cell(si, sj))

    # Put start into queue
    q.append(Cell(si, sj))

    while q:
        current = q.popleft()
        ci, cj = current.i, current.j

        # Check for goal
        if ci == gi and cj == gj:
            # Build path from goal back to start using parents
            return trace_path(current, graph)

        # Expand neighbors
        for ni, nj in graph.find_neighbors(ci, cj):
            # Skip cells that are in collision
            if graph.check_collision(ni, nj):
                continue

            # Skip already visited cells
            if graph.visited[nj, ni]:
                continue

            # Mark neighbor as visited
            graph.visited[nj, ni] = True
            graph.dist[nj, ni] = graph.dist[cj, ci] + 1.0
            graph.parent_i[nj, ni] = ci
            graph.parent_j[nj, ni] = cj

            # Log visited cell for web app visualization
            graph.visited_cells.append(Cell(ni, nj))

            # Add neighbor to queue
            q.append(Cell(ni, nj))

    """TODO (P3): Implement BFS."""

    # If no path was found, return an empty list.
    return []


def a_star_search(graph, start, goal):
    """A* Search (BFS) algorithm.
    Args:
        graph: The graph class.
        start: Start cell as a Cell object.
        goal: Goal cell as a Cell object.
    """
    graph.init_graph()  # Make sure all the node values are reset.

    """TODO (P3): Implement A*."""

    # If no path was found, return an empty list.
    return []
