# create a new list with only odd numbers from arr = [1, 2, 3, 4, 5]

arr = [1, 2, 3, 4, 5]

# junior
new_arr = [] # Đầu tiên, tạo một danh sách rỗng
for e in arr: # Sau đó, dùng vòng lặp để đi qua từng phần tử trong danh sách
    if e % 2 == 1: # Trong vòng lặp, kiểm tra xem phần tử đó có phải là số lẻ hay không ... Nếu đúng, thì thêm nó vào danh sách mới ...  
        new_arr.append(e)

# senior
new_arr = [e for e in arr if e % 2 == 1]

Chào mừng các bạn đến với video hôm nay ... Chủ đề hôm nay là list comprehension ... Đây là một tính năng mạnh mẽ của Python giúp bạn tạo mảng 1 cách ngắn gọn và dễ đọc hơn ...
Giả sử ta có một danh sách các số ... Nhiệm vụ là tạo một danh sách mới chỉ chứa các số lẻ từ danh sách trên...
Chúng ta bắt đầu với cách giải của lập trình viên junior ... -> Intro

Đầu tiên, tạo một danh sách rỗng ... => new_arr = []
Sau đó, dùng vòng lặp để đi qua từng phần tử trong danh sách => for e in arr:
Trong vòng lặp, kiểm tra xem phần tử đó có phải là số lẻ hay không ... Nếu đúng, thì thêm nó vào danh sách mới ...
=> if e % 2 == 1 
  new_arr.append(e)
Cách này hoàn toàn đúng, nhưng khá dài dòng và có thể viết ngắn gọn hơn ...
Bây giờ, hãy xem một lập trình viên senior sẽ giải quyết như thế nào ...
Lập trình viên senior sẽ sử dụng list comprehension giúp chúng ta tự động lặp qua danh sách, kiểm tra điều kiện, và thêm phần tử nếu điều kiện đúng chỉ trong một dòng code ...Về mặt kỹ thuật, list comprehension là một tính năng của Python giúp tạo ra danh sách mới bằng cách lọc và chuyển đổi phần tử từ danh sách có sẵn => new_arr = [e for e in arr if e % 2 == 1]
Nó nhanh hơn và "Pythonic" hơn so với việc dùng vòng lặp và append ...
Các bạn có thể checkout source code tại link mình để trong video nhé...
Cảm ơn các bạn đã theo dõi và hẹn gặp lại trong video tiếp theo
