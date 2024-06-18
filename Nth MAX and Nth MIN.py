# Practical 6
# Nth MAX and Nth MIN
print(">>> FINDING Nth MAX and Nth MIN")
print("")#...space
print("""the list will be in sortted manner
      array
     mylist = [1,2,9,7,5,1,8,3,6]""")
def nth_max_min_sorting(arr,n):
    sorted_arr = sorted(arr)
    print("---Sorted array :",sorted_arr)
    print("")#...space
    nth_max = sorted_arr[-n]
    nth_min = sorted_arr[n-1]
    return nth_max , nth_min

mylist = [1,2,9,7,5,1,8,3,6]
n = 3
nth_max,nth_min = nth_max_min_sorting(mylist,n)
print(">>> MAXIMUM ELEMENT")
print("---3rd max:",nth_max)
print("")#....space
print(">>>MINIMUM ELEMENT")
print("---3rd min:",nth_min)
