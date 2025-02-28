import json
def selectionSort(list,last):
    current=0
    compare=0
    while current<last:
        smallest=current
        walker=current+1
        while walker<=last:
            if list[walker]<list[smallest]:
                smallest=walker
            walker+=1
            compare+=1
        if smallest!=current:
            list[current],list[smallest]=list[smallest],list[current]
        current+=1
        print(list)
    print(f"Comparison times: {compare}")
selectionSort(json.loads(input()),int(input()))