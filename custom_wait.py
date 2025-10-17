class Node:
    def __init__(self, customer):
        self.customer = customer
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, customer):
        new_node = Node(customer)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        data = self.front.customer
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def is_empty(self):
        return self.front is None

    def display(self):
        current = self.front
        if current is None:
            print("Không có khách hàng trong hàng chờ.")
            return
        print("Danh sách hàng chờ:")
        while current:
            print(f"- {current.customer}")
            current = current.next

# --- Chạy thử ---
if __name__ == "__main__":
    queue = Queue()
    while True:
        print("\n--- MENU QUẦY GIAO DỊCH ---")
        print("1. Thêm khách hàng")
        print("2. Phục vụ khách hàng")
        print("3. Xem hàng đợi")
        print("4. Thoát")
        choice = input("Chọn chức năng (1-4): ")

        if choice == '1':
            name = input("Nhập tên khách hàng: ")
            queue.enqueue(name)
            print(f"Đã thêm khách: {name}")
        elif choice == '2':
            served = queue.dequeue()
            if served:
                print(f"Đang phục vụ: {served}")
            else:
                print("Không có khách để phục vụ.")
        elif choice == '3':
            queue.display()
        elif choice == '4':
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ.")
