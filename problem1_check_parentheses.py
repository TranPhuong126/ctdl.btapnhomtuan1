from stack_array import StackArray  # Dùng Stack cài bằng mảng

def is_valid_parentheses(expr):
    stack = StackArray()
    # Bảng đối chiếu ngoặc đóng với ngoặc mở tương ứng
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in expr:
        if char in '([{':        # Nếu là ngoặc mở, push vào stack
            stack.push(char)
        elif char in ')]}':      # Nếu là ngoặc đóng, kiểm tra với đỉnh stack
            if stack.is_empty():  # Nếu stack rỗng thì biểu thức sai
                return False
            top = stack.pop()
            if mapping[char] != top:  # Nếu ngoặc mở không tương ứng với ngoặc đóng
                return False

    # Nếu sau khi duyệt hết, stack rỗng → biểu thức hợp lệ
    return stack.is_empty()

# Test chương trình
expr1 = "{[(a+b)*(c-d)]}"
expr2 = "{[(a+b]*[c-d)]}"

print(f"Biểu thức 1: {'Hợp lệ' if is_valid_parentheses(expr1) else 'Không hợp lệ'}")
print(f"Biểu thức 2: {'Hợp lệ' if is_valid_parentheses(expr2) else 'Không hợp lệ'}")
