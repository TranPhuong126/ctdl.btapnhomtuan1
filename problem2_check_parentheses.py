from stack_array import StackArray

def is_valid_parentheses(expr):
    stack = StackArray()
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in expr:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.is_empty():
                return False
            top = stack.pop()
            if mapping[char] != top:
                return False
    return stack.is_empty()

if __name__ == "__main__":
    expr = input("Nhập biểu thức cần kiểm tra dấu ngoặc: ")
    if is_valid_parentheses(expr):
        print("Biểu thức hợp lệ!")
    else:
        print("Biểu thức không hợp lệ!")
