algorithm jarvis(S) is
    // S is the set of points
    // P will be the set of points which form the convex hull.
    pointOnHull = leftmost point in S 
    i := 0
    repeat
        P[i] := pointOnHull
        endpoint := S[0]      
        for j from 0 to |S| do
            if (endpoint == pointOnHull) or
            (S[j] is on left of line from P[i] to endpoint) then
                endpoint := S[j]   
        i := i + 1
        pointOnHull = endpoint
    until endpoint = P[0]      
