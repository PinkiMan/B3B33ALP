import sys


def max_area_histogram(histogram):
    stack = list()
    max_area = 0
    index = 0

    x2=0
    x1=0
    while index < len(histogram):
        if (not stack) or (histogram[stack[-1]] <= histogram[index]):
            stack.append(index)
            index += 1
        else:
            top_of_stack = stack.pop()
            area = (histogram[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
            if max_area < area:
                x2 = index-1
                size_x=((index - stack[-1] - 1) if stack else index)
                x1= x2-size_x+1


            max_area = max(max_area, area)


    while stack:
        top_of_stack = stack.pop()
        area = (histogram[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
        if max_area < area:
            x2 = index-1
            size_x = ((index - stack[-1] - 1) if stack else index)
            x1 = x2 - size_x + 1
        max_area = max(max_area, area)


    return max_area,x1,x2



def maxRectangle(A):
    best_result, best_x1,best_x2 = max_area_histogram(A[0])
    best_y=0
    for i in range(1, len(A)):
        for j in range(len(A[i])):
            if (A[i][j]==1):
                A[i][j] += A[i - 1][j]
        result, x1,x2=max_area_histogram(A[i])
        if best_result<result:
            best_result=result
            best_x1=x1
            best_x2=x2
            best_y=i


    return (best_y-int(best_result/(best_x2-best_x1+1))+1,best_x1),(best_y,best_x2)



pole = []
f = open('matice/rectangle.txt', 'r')
for line in f:
    pole.append(list(map(int, line.split())))
f.close()


mOrig = [[1,  -9, -2,   8,  6,  1],
    [8,  -1,-11,  -7,  6,  4],
    [10, 12, -1,  -9, 12, 14],
    [8, 10, -3,  -5,  17,  8],
    [6,  4, 10, -13, -16, 19]]

m = [[1 if x < 0 else 0 for x in z] for z in pole]


a,b=maxRectangle(m)
c=[]
for item in a:
    c.append(str(item))
a=' '.join(c)

d=[]
for item in b:
    d.append(str(item))
b=' '.join(d)


print(a)
print(b)