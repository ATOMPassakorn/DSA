import json
def selectionSort(list,last):
    current=0
    compare=0
    while current<last:
        smallest=current
        walker=current+1
        while walker<=last:
            char1, num1 = list[walker][0], int(list[walker][1:])
            char2, num2 = list[smallest][0], int(list[smallest][1:])
            if char1 < char2 or (char1 == char2 and num1 < num2):
                smallest = walker
            walker+=1
            compare+=1
        if smallest!=current:
            list[current],list[smallest]=list[smallest],list[current]
        current+=1
        print(list)
    print(f"Comparison times: {compare}")
selectionSort(json.loads(input()),int(input()))