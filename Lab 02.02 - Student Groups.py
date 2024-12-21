class ArrayStack():
    def __init__(self):
        self.size = 0
        self.data = list()
    def push(self, input_data):
        """Stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1
    def pop(self):
        if self.data:
            last=self.data.pop()
            self.size -= 1
            return last
        else:
            print("Underflow: Cannot pop data from an empty list")
            return None
    def is_empty(self):
        if not self.data:
            return True
        return False
    def get_stack_top(self):
        if self.data:
            top_element = self.data.pop()
            self.data.append(top_element)
            return top_element
        else:
            print("Underflow: Cannot get stack top from an empty list")
            return None
    def get_size(self):
        return len(self.data)
    def print_stack(self):
        print(self.data)
def main():
    stacks=ArrayStack()
    student_group=list()
    group=int(input())
    student=int(input())
    for _ in range(student):
        name=input()
        stacks.push(name)
    for _ in range(group):
        student_group.append(ArrayStack())
    count=1
    while count<=student:
        for choose in student_group:
            choose.push(stacks.pop())
            count+=1
            if count > student:
                break
        if count > student:
            break
    for group_number, student_name in enumerate(student_group,1):
        print(f"Group {group_number}:", end=" ")
        print(*student_name.data, sep=", ")
main()
