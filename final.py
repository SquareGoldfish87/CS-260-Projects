#!/usr/bin/env python3
"""Make a graph class with the required functions."""

# We'll need sys later for something.
import sys

# This is our graph class.
class Graph:
    # We make each instance of the class able to take a dictionary as an argument.
    def __init__(self, graph_dict=None):
        # We set the default value of graph_dict to None, and this ensures that if no dictionary
        # is given as an argument, a blank dictionary will be created and used. 
        if graph_dict == None:
            graph_dict = {}
        # We then assign the given dictionary to this specific instance of the Graph class.
        self.graph_dict = graph_dict
    
    # This function gets a list of all our vertices, for testing purposes.
    def get_vertices(self):
        """Return a list of keys in graph_dict"""
        # This returns a list of every key(vertex) in the dictionary.
        return list(self.graph_dict.keys())

    # This function adds a vertex.
    def add_vertex(self, vertex):
        """Add a vertex to our graph"""
        # If the given vertex isn't in our graph_dict, we add it.
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    # This is our edge adding function.
    def add_edge(self, vertex_1, vertex_2):
        """Add an edge to our graph."""
        # We check if the first vertex is in our graph dictionary.
        if vertex_1 in self.graph_dict:
           # If it is, then we append our 2nd vertex to the 1st's value list, thus creating a "line", or edge,
           # linking the two.
            self.graph_dict[vertex_1].append(vertex_2)

    # This is the function used to find every edge in our graph.
    def get_edges(self):
      """Find the edges of the graph, place them in a list, and return that list."""
      # We start by defining an empty list for appending.
      edge_list = []
      # For every key in our dictionary, and for every value in our value list
      for vertex in self.graph_dict:
         for next_vertex in self.graph_dict[vertex]:
            # If this specific value pair isn't in our append list, we append it to the list.
            if {next_vertex, vertex} not in edge_list:
               edge_list.append({vertex, next_vertex})
      # Once we have every appended value pair (symbolizing every edge), we return our list.
      return edge_list

    # This is a shortcut function that just runs find_edges on an instance of the Graph class.
    def edges(self):
      """Run get_edges on the current class."""
      return self.get_edges()

    # This function finds all neighbors of a vertex and returns them as a list.
    def get_neighbors(self, vertex):
        "Returns the neighbors of a vertex."
        # To return a list of all the places a vertex touches, we just return the value stored
        # at that vertex's key.
        return list(self.graph_dict[vertex])

    # This function finds the value of an edge and returns it.
    def edge_value(self, vertex_1, vertex_2):
        "Returns the value of an edge between two vertices."
        # We try and return the assigned value of an edge between 2 vertices.
        # In the case that it isn't, we just return a default value, 1.
        try:
            return self.graph_dict[vertex_1][vertex_2]
        except TypeError:
            return 1
        # We use try/except here because sometimes the value of the edges isn't assigned, which throws a TypeError.

    # This is the Minimum Spanning Tree function. Depending on the value of "test", different values
    # will be returned for testing reasons. If "test" isn't inputted, we just set it to None and ignore it.
    def min_span_tree(self, test=None):
        """Create a Minimum Spanning Tree for the given graphical data."""
        # We start by making an empty list for appending, a list of all our edges, and a dictionary.
        edge_value_list = []
        edge_list = self.edges()
        edge_dict = {}
        # For every edge in our list, we assign it's 2 seperate variables as vertex 1 and 2.
        for edge in edge_list:
            vertex_1, vertex_2 = edge
            # We then try and find the value of that edge, and append this value to the value_list.
            edge_value_list.append(self.edge_value(vertex_1, vertex_2))
        # If we're running test 1, we return the edge list and the value list.
        if test == 1:
            return edge_list, edge_value_list
        # Now we have a complete list of our edges, and their corresponding values.

        # We create a counter
        counter = -1
        # For every edge in the list, we add 1 to the counter and add the edge to our edge dictionary with
        # it's corresponding value from the edge list.
        for edge in edge_list:
            counter += 1
            # Note: We need to make edge a tuple or it'll throw a TypeError.
            edge = tuple(edge)
            edge_dict[edge] = edge_value_list[counter]

        # If we run test 2, we return edge_dict.
        if test == 2:
            return edge_dict

        # Now we have a dictionary where every edge is a key, and the value is the corresponding edge value.
        # However, we first want to sort this dictionary by value.
        # We make another counter
        counter = 0
        # For every value in the list of values, we check to see if they're the same. If they are, we
        # skip the sorting part, since they're already in order. If they're not, we sort them.
        for value in edge_value_list:
            counter += 1
            try:
                next_value = edge_value_list[counter]
            except IndexError:
                pass
            if value == next_value:
                break
            # Alternatively, if there are multiples of a value in the list, we also can't sort it.
            # To check this, we pop the value and then search for it in the list.
            popped_value = edge_value_list.pop(counter-1)
            if popped_value in edge_value_list:
                # If we find the value, then it's in the list at least twice, so we break since
                # we can't sort it.
                break
                # If we don't find the same value twice, we keep going for every value in the edge list.

        # Note: The sorter won't work with a dictionary with multiples of the same value, meaning we can't
        # make a MST with any graph that has edges with the same value, unless they're all the same value.
        # Now we work on sorting. We make a list of sorted values, and a dictionary to place the sorted
        # values into.
        sorted_edge_dict = {}
        # We sort the values of the dictionary.
        sorted_values = sorted(edge_dict.values())
        # For every sorted value, we try to match it to it's key.
        for value in sorted_values:
            for key in edge_dict.keys():
                # Once they're matched, they're placed in the new dictionary.
                if edge_dict[key] == value:
                    sorted_edge_dict[key] = edge_dict[key]

        # If we're running test 3, we return the sorted dictionary.
        if test == 3:
            return sorted_edge_dict

        # From here, we can make our Minimum Spanning Tree.
        # First, a list of "visited" vertices and a list of values , we'll append both as we go
        visited_vertices = []
        value_list = []
        # We start by printing a message letting the user know we're about to tell them every edge in the MST.
        print("The edges used in our Minimum Search Tree are:")
        # The dictionary should be sorted, so we walk through it from the start and try to use the given
        # edge for our MST.
        for key in sorted_edge_dict:
            # We first get the value of the edge.
            sorted_edge_dict[key] = value
            # Then we seperate the key into the 2 vertices.
            vertex_1, vertex_2 = key
            # If vertex_1 is in visited_vertices, we need to check vertex_2.
            if vertex_1 in visited_vertices:
                # If both vertices have been visited, we can't use the current edge or we'd make a loop.
                # Thus, we break.
                if vertex_2 in visited_vertices:
                    pass
                else:
                    # If vertex_2 isn't visited, then we need to add it to the path and mark it as visited.
                    visited_vertices.append(vertex_2)
                    print(f"Edge: {vertex_1} to {vertex_2}, Value: {value}")
                    # In addition, we need to append the value to the value list.
                    value_list.append(value)
            else:
                # If vertex_1 isn't visited, then we can do the above for vertex_1.
                visited_vertices.append(vertex_1)
                # If vertex_2 isn't marked as visited, we need to do so.
                if vertex_2 not in visited_vertices:
                    visited_vertices.append(vertex_2)
                value_list.append(value)
                print((f"Edge: {vertex_1} to {vertex_2}, Value: {value}"))
                # Then, we loop until we have a complete list of every vertex marked as visited.
        
        # Once we've looped through all of them, we use the sum function to print the total value of our MST.
        print(f"The sum of our Minimum Spanning Tree is: {sum(value_list)}")
    
def shortest_path(graph, starting_vertex):
    """Use Dijkstra's Algorithm to find the shortest path between 2 vertices."""
    unvisited_vertices = graph.get_vertices()
 
    # We'll use this dictionary to save the cost of visiting each vertex and update it as we move along the graph 
    shortest_path = {}
 
    # We'll use this dictionary to save the shortest path to a vertex so far
    previous_vertices = {}
 
    # We'll use sys.maxsize as our "infinite" starting size.
    max_value = sys.maxsize
    # For each vertex in our list of unvisited vertices, we set the shortest path to infinity.
    for vertex in unvisited_vertices:
        shortest_path[vertex] = max_value
    # We then set the starting vertex's shortest path to 0.
    shortest_path[starting_vertex] = 0
    
    # This ensures we loop until we visit all the vertices.
    while unvisited_vertices:
        # We set the current minimum vertex to None, so we have a value to set it to.
        current_min_vertex = None
        # For every vertex in our unvisited vertices
        for vertex in unvisited_vertices:
            # If our current minimum vertex is None (meaning we just started), we set it to the
            # vertex we're using from the loop.
            if current_min_vertex == None:
                current_min_vertex = vertex
            # Otherwise, if the loop vertex's path is shorter than the current minimum vertex's 
            # path, we set the loop vertex as the current minimum.
            elif shortest_path[vertex] < shortest_path[current_min_vertex]:
                current_min_vertex = vertex
                
        # Then we get the vertices that neighbor our current minimum
        neighbors = graph.get_neighbors(current_min_vertex)
        # For every neighboring vertex, we take the shortest path to the current minimum vertex
        # and add the value of the edge between the current minimum and the neighbor.
        for vertex in neighbors:
            # We store this value in a placeholder value.
            placeholder = shortest_path[current_min_vertex] + graph.edge_value(current_min_vertex, vertex)
            # If this placeholder value is less than the shortest path to the current vertex, we update the
            # shortest path to reflect that.
            if placeholder < shortest_path[vertex]:
                shortest_path[vertex] = placeholder
                # We also update the best path to the current vertex
                previous_vertices[vertex] = current_min_vertex
 
        # After we visit it's neighbors, we remove the current minimum vertex from the list,
        # declaring it "visited"
        unvisited_vertices.remove(current_min_vertex)
    # Once we've done all that, we return our 2 dictionaries.
    return previous_vertices, shortest_path

# This function prints the results from our shortest_path function.
def print_result(previous_vertices, shortest_path, start_vertex, target_vertex):
    """Take the data from shortest_path and print it."""
    # First, we define a list for appending and a variable for making some checks.
    shortest_path_list = []
    vertex = target_vertex
    
    # While the vertex we're checking isn't the starting vertex, we append it to the shortest_path_list
    # and then set the vertex equal to the value stored in the previous_vertices dictionary.
    # This will give us a path from our target to the start, working backwards.
    while vertex != start_vertex:
        shortest_path_list.append(vertex)
        vertex = previous_vertices[vertex]
 
    # Since the above loop breaks when vertex = start_vertex, we have to add start_vertex manually.
    shortest_path_list.append(start_vertex)
    
    # This prints everything out nice and pretty, and also in reverse order so that it'll read forwards.
    print(f"The shortest path from {start_vertex} to {target_vertex} is as follows:")
    print(" -> ".join(reversed(shortest_path_list)))
    print(f"The number of edges in our shortest path is: {shortest_path[target_vertex]}")



graph_dict = { 
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}
g = Graph(graph_dict)

x, y = shortest_path(g, "a")
print_result(x, y, "a", "e")
print(g.min_span_tree())