import json
def insertionSort(list,last):
    current=1
    compare=0
    while current<=last:
        hold=list[current]
        walker=current-1
        while walker>=0 and hold<list[walker]:
            char1, num1 = hold[0], int(hold[1:])
            char2, num2 = list[walker][0], int(list[walker][1:])
            if char1 < char2 or (char1 == char2 and num1 < num2):
                list[walker+1]=list[walker]
                walker-=1
                compare+=1
            else:
                break
        if walker>=0:
            compare+=1
        list[walker+1]=hold
        current+=1
        print(list)
    print(f"Comparison times: {compare}")
insertionSort(json.loads(input()),int(input()))