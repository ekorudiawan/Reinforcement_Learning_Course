import math 
import random

def findMaxSubsequential(list_input):
    sublist = []
    sum_list = 0
    max_num = 0
    max_list = []
    for i in range(len(list_input)-1):
        for j in range(i+2, len(list_input)+1):
            sublist = list_input[i:j]
            sum_list = sum(sublist)
            # print(sum_list, sublist)
            if sum_list > max_num:
                max_num = sum_list
                max_list = sublist
    return max_num, max_list

def create_random_list(n):
    lst = []
    for i in range(n):
        lst.append(random.randint(-10,10))
    return lst

def main():
    print("Find Max Sub Sequential")
    # random_list = [2,5,-7,3,-2,9,-1,3]
    random_list = create_random_list(5)
    max_val, sublist = findMaxSubsequential(random_list)
    print("Max Val :" + str(max_val))
    print("Sublist :" + str(sublist))

if __name__ == "__main__":
    main()