import json
def bubbleSort(list,last):
    current=0
    compare=0
    sorted=False
    while current<=last and sorted is False:
        walker=last
        sorted=True
        while walker>current:
            char1, num1 = list[walker][0], int(list[walker][1:])
            char2, num2 = list[walker-1][0], int(list[walker-1][1:])
            if char1 < char2 or (char1 == char2 and num1 < num2):
                sorted=False
                list[walker],list[walker-1]=list[walker-1],list[walker]
            walker-=1
            compare+=1
        current+=1
        print(list)
    print(f"Comparison times: {compare}")
bubbleSort(json.loads(input()),int(input()))