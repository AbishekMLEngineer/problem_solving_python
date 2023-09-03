
def ducthflag_partition(pivot_index :int , A: list[int]):
    pivot = A[pivot_index]
    
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j]<pivot:
                A[i], A[j]= A[j], A[i]
                break
    print(A)
    #2nd pass
    # for i in reversed(range(len(A))):
    #     print(i)
    #     for j in reversed(range(i)):
    #         if A[j] > pivot:
    #             A[i] , A[j] = A[j] ,A[i]
    #         break
    for i in range(len(A)):
        print(i)
        for j in range(i):
            if A[j] > pivot:
                A[i] , A[j] = A[j] ,A[i]
            break



# ducthflag_partition(2, [1,3,4, 0 ,3])
# much improved version with O(N) time complexity                      

def dutchflag( pivot_index :int , A: list[int]) -> None:
    pivot = A[pivot_index]
    smaller = 0
    for i in range(len(A)):
        if A[i] <pivot :
            A[i] , A[smaller] = A[smaller], A[i]
            smaller+=1
    larger = len(A) -1

    for i in reversed(range(len(A))):
        if A[i] >pivot:
            A[i] , A[larger] = A[larger],A[i]
            larger -=1



