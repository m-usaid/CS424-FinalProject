let points be the list of points
let stack = empty_stack()

find the lowest y-coordinate and leftmost point, called P0
sort points by polar angle with P0, 
if several points have the same polar angle then only keep the farthest

for point in points:
    while count stack > 1 and
    ccw(next_to_top(stack), top(stack), point) <= 0:
        pop stack
    push point to stack
end
