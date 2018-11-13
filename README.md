We are given a map of cities connected with each other via cable lines such that there is no cycle between any two cities. We need to find the maximum length of cable between any two cities for given city map.

This solution is for a graph provided as an adjacency matrix.

This problem comes from https://www.geeksforgeeks.org/longest-path-between-any-pair-of-vertices where the official solution is O(V * (V+E)). My solution is a superior O(V^2). (Note that if the graph is provided as an adjacency list, we could get O(V + E); The additional adjustment to this algorithm is trivial.)

Here is a proof of the method:

Because the graph is acyclic and undirected, we can choose any node and consider it the root, and the graph becomes a tree. Let's call the root R. The node furthest from R node can be found by DFS. Let's call that farthest node N.

My claim is that N is one end of the longest path. Let's assume it isn't, and prove by contradiction. If it isn't, then let's say the actual longest path goes from node X to node Y, neither of which are N. Let A be the least common ancestor of X and Y, such that A is on the longest path XAY. Then the longest path = XA + AY. Now let B be the common ancestor of X and N. Note that N being the farthest node means the distance NR >= XR, which means NB >= XB.

If B is an ancestor of (or equal to) A, remembering that XB <= NB, since XA + AB = XB, this means XA <= XB <= NB. It follows that the path NBAY > XAY. Contradiction.

If A is an ancestor of B, then B is also on the longest path XBAY. N being the farthest node means NR >= XR, which means NB >= XB, which means that the path NBAY >= XBAY. Contradiction.

if A = B, then let C be the least common ancestor of N and Y. The logic in the previous paragraph above applies by symmetry (even if A = B = C), just replace B with C and X with Y.

Now that we've proven N is one end of the longest path, then the longest path must be the path from N to the node farthest from N, which can be determined with a second DFS starting at N.
