"""
간단한 콘솔 프로그램 예시

기능:
1. 할 일(To-do) 추가
2. 할 일 목록 보기
3. 할 일 삭제
4. 프로그램 종료
"""

def print_menu():
    print("===== 간단 To-Do 리스트 =====")
    print("1. 할 일 추가")
    print("2. 할 일 목록 보기")
    print("3. 할 일 삭제")
    print("4. 종료")
    print("============================")

def add_todo(todo_list):
    item = input("추가할 할 일을 입력하세요: ").strip()
    if item:
        todo_list.append(item)
        print(f"✅ '{item}' 추가됨")
    else:
        print("⚠ 빈 문자열은 추가할 수 없습니다.")

def show_todos(todo_list):
    if not todo_list:
        print("현재 등록된 할 일이 없습니다.")
        return

    print("📌 현재 할 일 목록:")
    for idx, item in enumerate(todo_list, start=1):
        print(f"{idx}. {item}")

def delete_todo(todo_list):
    if not todo_list:
        print("삭제할 할 일이 없습니다.")
        return

    show_todos(todo_list)
    try:
        num = int(input("삭제할 번호를 입력하세요: "))
        if 1 <= num <= len(todo_list):
            removed = todo_list.pop(num - 1)
            print(f"🗑 '{removed}' 삭제됨")
        else:
            print("⚠ 유효하지 않은 번호입니다.")
    except ValueError:
        print("⚠ 숫자를 입력해주세요.")

def main():
    todo_list = []

    while True:
        print_menu()
        choice = input("메뉴 선택 (1-4): ").strip()

        if choice == "1":
            add_todo(todo_list)
        elif choice == "2":
            show_todos(todo_list)
        elif choice == "3":
            delete_todo(todo_list)
        elif choice == "4":
            print("프로그램을 종료합니다.")
            break
        else:
            print("⚠ 1~4 중에서 선택해주세요.")

        print()  # 한 줄 띄우기

if __name__ == "__main__":
    main()
