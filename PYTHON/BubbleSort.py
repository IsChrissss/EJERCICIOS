def main():
    arr = [7,6,4,3]
    bubble_sort(arr)
    print(arr)

def bubble_sort(l):
    n = len(l)
    flag = True
    while flag:
        flag = False
        for i in range(1, n):
            if l[i-1] > l[i]:
                flag = True
                l[i-1], l[i] = l[i], l[i-1]
    
main()