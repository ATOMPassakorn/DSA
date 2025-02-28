import json
def bubbleSort(list,last):
    current=0
    compare=0
    sorted=False
    while current<=last and sorted is False:
        walker=last
        sorted=True
        while walker>current:
            if list[walker]<list[walker-1]:
                sorted=False
                list[walker],list[walker-1]=list[walker-1],list[walker]
            walker-=1
            compare+=1
        current+=1
        print(list)
    print(f"Comparison times: {compare}")
bubbleSort(json.loads(input()),int(input()))