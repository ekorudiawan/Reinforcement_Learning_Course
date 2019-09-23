__author__  = "Eko Rudiawan Jamzuri"
__email__   = "ekorudiawan@gmail.com"

import math 
import random

def find_max_subsequential(list_input):
    sub_list = []
    sum_list = 0
    max_num = -999
    max_list = []
    for i in range(len(list_input)-1):
        for j in range(i+1, len(list_input)+1):
            sub_list = list_input[i:j]
            sum_list = sum(sub_list)
            # print(sum_list, sub_list)
            if sum_list > max_num:
                max_num = sum_list
                max_list = sub_list
    return max_num, max_list

def create_random_list(len_list):
    random_list = []
    for i in range(len_list):
        random_list.append(random.randint(-10,10))
    return random_list

def main():
    print("Find Max Sub Sequential")
    # random_list = [2,5,-7,3,-2,9,-1,3]
    random_list = create_random_list(5)
    max_val, sub_list = find_max_subsequential(random_list)
    print("Max Val :" + str(max_val))
    print("sub_list :" + str(sub_list))

if __name__ == "__main__":
    main()