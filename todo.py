import json
import os
from dataclasses import dataclass, asdict
from typing import List

DATA_FILE = "todos.json"


@dataclass
class Todo:
    id: int
    title: str
    done: bool = False


def load_todos() -> List[Todo]:
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        raw = json.load(f)
    return [Todo(**item) for item in raw]


def save_todos(todos: List[Todo]) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([asdict(t) for t in todos], f, ensure_ascii=False, indent=2)


def list_todos(todos: List[Todo]) -> None:
    if not todos:
        print("📭 등록된 할 일이 없습니다.")
        return
    print("\n=== TODO 리스트 ===")
    for t in todos:
        status = "✅" if t.done else "⬜"
        print(f"{t.id:3d} | {status} | {t.title}")
    print()


def add_todo(todos: List[Todo]) -> None:
    title = input("새 할 일 내용을 입력하세요: ").strip()
    if not title:
        print("내용이 비어 있습니다.")
        return
    next_id = max([t.id for t in todos], default=0) + 1
    todos.append(Todo(id=next_id, title=title))
    save_todos(todos)
    print("✅ 추가 완료!")


def toggle_todo(todos: List[Todo]) -> None:
    try:
        tid = int(input("완료/취소할 TODO id 입력: "))
    except ValueError:
        print("숫자를 입력해주세요.")
        return
    for t in todos:
        if t.id == tid:
            t.done = not t.done
            save_todos(todos)
            print("상태가 변경되었습니다.")
            return
    print("해당 id를 찾을 수 없습니다.")


def delete_todo(todos: List[Todo]) -> None:
    try:
        tid = int(input("삭제할 TODO id 입력: "))
    except ValueError:
        print("숫자를 입력해주세요.")
        return
    before = len(todos)
    todos[:] = [t for t in todos if t.id != tid]
    if len(todos) < before:
        save_todos(todos)
        print("🗑 삭제 완료.")
    else:
        print("해당 id를 찾을 수 없습니다.")


def main():
    print("==== 간단 TODO CLI ====")
    todos = load_todos()

    while True:
        print("\n[메뉴]")
        print("1. 목록 보기")
        print("2. 할 일 추가")
        print("3. 완료/취소 전환")
        print("4. 삭제")
        print("0. 종료")
        choice = input("선택: ").strip()

        if choice == "1":
            list_todos(todos)
        elif choice == "2":
            add_todo(todos)
        elif choice == "3":
            toggle_todo(todos)
        elif choice == "4":
            delete_todo(todos)
        elif choice == "0":
            print("안녕히 가세요 👋")
            break
        else:
            print("올바른 번호를 선택하세요.")


if __name__ == "__main__":
    main()
