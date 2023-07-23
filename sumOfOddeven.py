1)Execute the given function.
def LargeSmallSum(arr)

The function takes an integral arr which is of the size or length of its arguments. Return the sum of the second smallest element at odd position ‘arr’ and the second largest element at the even position.

Assumption

Every array element is unique.
Array is 0 indexed.
Note:

If the array is empty, return 0.
If array length is 3 or <3, return 0.
 
Example

Input:
Arr: 3 2 1 7 5 4

Output:
7
Coding:
*******
def sumOfMaximum(arr):
    odd=[]
    even=[]
    for i in range(len(arr)):
        if i%2==0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    even.sort()
    odd.sort()
    return even[-2]+odd[1]
n=int(input('Enter range : '))
lst=[]
for i in range(n):
    a=int(input())
    lst.append(a)
print("The sum is = ",end=" ")
print(sumOfMaximum(lst))
----------------------------------------------------------------------------------------------------------------------------------------
2)Perform the following function. 
def Productsmallpair(sum,arr)

This function accepts the integers sum and arr. It is used to find the arr(j) and arr(k), where k ! = j. arr(j) and arr(k) should be the smallest elements in the array.

Keep this in mind:

If n<2 or empty, return –1.
If these pairs are not found, then return to zero.
Make sure all the values are within the integer range.
 
Example

Input:
Sum: 9
Arr: 5 4 2 3 9 1 7

Output:
2

Explanation

From the array of integers, we have to select the two smallest numbers, i.e 2 and 1. Sum of these two (2 + 1) = 3. This is less than 9 (3 < 9). The product of these two is 2 (2 x 1 = 2) Hence the output is integer 2.

Sample input:
Sum: 4
Arr: 9 8 –7 3 9 3

Sample output:
–21
Coding:
******
