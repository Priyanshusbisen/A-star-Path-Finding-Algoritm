# A-star-Path-Finding-Algorithm
The Application finds the shortest path between two points using the A-star algorithm. 

A* path finding algorithm created using python ,pygame and tkinter.

A Star Algorithm-
This is the most optimal algorithm for path finding. A* algorithm is just an upgrade to Dikstara's Algorithm the only diffrence being in Dikstra's algo we do not consider the distance between the current node and destination which is called heuristic distance which can be calculated easily by using either Eucledian distance , Manhattan distance or more.The addition of heuristic distance improves the speed of algorithm.

The Pseudo code of astar algorithm is given below:
    
    // A* (star) Pathfinding
    // Initialize both open and closed list
    let the openList equal empty list of nodes
    let the closedList equal empty list of nodes
    // Add the start node
    put the startNode on the openList (leave it's f at zero)
    // Loop until you find the end
    while the openList is not empty
        // Get the current node
        let the currentNode equal the node with the least f value
        remove the currentNode from the openList
        add the currentNode to the closedList
        // Found the goal
        if currentNode is the goal
            Congratz! You've found the end! Backtrack to get path
        // Generate children
        let the children of the currentNode equal the adjacent nodes
    
    for each child in the children
        // Child is on the closedList
        if child is in the closedList
            continue to beginning of for loop
        // Create the f, g, and h values
        child.g = currentNode.g + distance between child and current
        child.h = distance from child to end
        child.f = child.g + child.h
        // Child is already in openList
        if child.position is in the openList's nodes positions
            if the child.g is higher than the openList node's g
                continue to beginning of for loop
        // Add the child to the openList
        add the child to the openList


Packages Required-
1)pygame
2)tkinter

If these packages are not installed on your PC 

RUN install_requirements.py

RUN PathFinder.py to run the application.
