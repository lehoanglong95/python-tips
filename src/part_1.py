# LIST COMPREHENSION

# Assignment: create a new list with only odd numbers from arr = [1, 2, 3, 4, 5]

arr = [1, 2, 3, 4, 5]

# junior
new_arr = []  # Đầu tiên, tạo một danh sách rỗng
for e in arr:  # Sau đó, dùng vòng lặp để đi qua từng phần tử trong danh sách
    if (
        e % 2 == 1
    ):  # Trong vòng lặp, kiểm tra xem phần tử đó có phải là số lẻ hay không ... Nếu đúng, thì thêm nó vào danh sách mới ...
        new_arr.append(e)

# senior
new_arr = [e for e in arr if e % 2 == 1]
