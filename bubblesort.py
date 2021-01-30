def bubble_sort(array):
    for i in range(len(array)):
        swapped = True
        for j in range(0, len(array) - i - 1):
            
            if array[j] > array[j + 1]:
                (array[j], array[j + 1]) = (array[j + 1], array[j])
                swapped = False

                if swapped:
                    break
        
lst = []

data = int(input("Enter the size of input = "))

for i in range(0, data):
    input_list = int(input("Enter the elements to be sorted = "))
    lst.append(input_list)     
        
bubble_sort(lst)
print("The sorted list is.....")
print(lst)