tasks = []
def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append(task_name)
    print(f"Đã thêm công việc: '{task_name}'")
# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")

def list_tasks():
    if not tasks:
        print("Hiện không có công việc nào.")
        return
    
    print("#--Danh sách công việc:#--")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def delete_task(task_index):
    """
    Xóa công việc (theo chỉ số 1-based) khỏi danh sách.
    Xử lý chỉ số không hợp lệ.
    """
    if task_index < 1 or task_index > len(tasks):
        print("Chỉ số công việc không hợp lệ.")
        return
    removed = tasks.pop(task_index - 1)
    print(f"Đã xóa công việc: '{removed['name']}'")

if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    list_tasks()
    complete_task(2)   # đánh dấu công việc số 2 hoàn thành
    list_tasks()
    delete_task(1)     # xóa công việc số 1
    list_tasks()