"""Lab 01.02 - Max…m1n…Avg"""
import json
def spam():
    """Lab 01.02 - Max…m1n…Avg"""
    my_list = json.loads(input())
    for step in range(len(my_list)):
        m1n_idx = step
        for i in range(step + 1, len(my_list)):
            if my_list[i] < my_list[m1n_idx]:
                m1n_idx = i
        (my_list[step], my_list[m1n_idx]) = (my_list[m1n_idx], my_list[step])
    maksud=round(my_list[-1],2)
    noysud=round(my_list[0],2)
    avg=round(sum(my_list)/len(my_list),2)
    print(f"({maksud}, {noysud}, {avg})")
spam()
