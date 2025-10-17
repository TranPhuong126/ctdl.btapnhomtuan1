class QueueArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            print("Hàng đợi yêu cầu đã đầy.")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1
        print(f"Đã nhận yêu cầu: '{item}'")

    def dequeue(self):
        if self.is_empty():
            print("Không có yêu cầu nào để xử lý.")
            return None
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def display(self):
        if self.is_empty():
            print("Không có yêu cầu nào.")
            return
        print("Danh sách yêu cầu chờ xử lý:")
        idx = self.front
        for _ in range(self.size):
            print(f"- {self.queue[idx]}")
            idx = (idx + 1) % self.capacity

# Danh sách sản phẩm mẫu
products = [
    {"name": "iPhone 15", "tags": ["điện thoại", "iphone", "apple"]},
    {"name": "Samsung Galaxy S23", "tags": ["điện thoại", "samsung"]},
    {"name": "MacBook Air M2", "tags": ["laptop", "apple", "mỏng nhẹ"]},
    {"name": "ASUS ROG Strix", "tags": ["laptop", "gaming", "hiệu năng"]},
    {"name": "Canon PIXMA", "tags": ["máy in", "giá rẻ", "văn phòng"]},
    {"name": "HP LaserJet", "tags": ["máy in", "văn phòng", "đen trắng"]}
]

def find_product_by_keyword(keyword):
    keyword = keyword.lower()
    result = []
    for product in products:
        if any(keyword in tag for tag in product["tags"]):
            result.append(product["name"])
    return result

# Giao diện chính
def main():
    queue = QueueArray(10)

    while True:
        print("\n--- MENU ĐỀ XUẤT SẢN PHẨM ---")
        print("1. Gửi yêu cầu sản phẩm")
        print("2. Xử lý yêu cầu tiếp theo")
        print("3. Xem danh sách yêu cầu")
        print("4. Thoát")

        choice = input("Chọn chức năng (1-4): ")

        if choice == '1':
            keyword = input("Nhập từ khóa sản phẩm bạn muốn tìm: ")
            queue.enqueue(keyword)

        elif choice == '2':
            request = queue.dequeue()
            if request:
                print(f"\nXử lý yêu cầu: '{request}'")
                matches = find_product_by_keyword(request)
                if matches:
                    print("Sản phẩm gợi ý:")
                    for p in matches:
                        print(f"- {p}")
                else:
                    print("Không tìm thấy sản phẩm phù hợp.")

        elif choice == '3':
            queue.display()

        elif choice == '4':
            print("Đã thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ.")
if __name__ == "__main__":
    main()
