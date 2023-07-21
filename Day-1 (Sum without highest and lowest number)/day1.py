##Problem statement:

"""Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).
The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.
Example
{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6 """

## Solution

def sum_array(arr):
    try:
        arr.remove(max(arr))
        arr.remove(min(arr))
        return sum(arr)
    except:
        return 0

## Testing
print(sum_array([2,4,5,1,3,5,6,]))