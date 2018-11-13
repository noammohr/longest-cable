Longest path between any pair of vertices

We are given a map of cities connected with each other via cable lines such that there is no cycle between any two cities. We need to find the maximum length of cable between any two cities for given city map.

This solution is for a graph provided as an adjacency matrix.

This problem comes from https://www.geeksforgeeks.org/longest-path-between-any-pair-of-vertices/#comment-4023526658 where the official solution is O(V * (V+E)). My solution is a superior O(V^2). (Note that if the graph is provided as an adjacency list, we could get O(V + E). The additional adjustment to this algorithm is trivial.)
