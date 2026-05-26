import json
import os
from datetime import datetime

DATA_FILE = "books.json"

def load_books():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, IOError):
        return []

def save_books(books):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)

def add_book(books):
    author = input("👤 Автор: ").strip()
    title = input("📖 Название: ").strip()

    for b in books:
        if b["author"].lower() == author.lower() and b["title"].lower() == title.lower():
            print("⚠️ Эта книга уже есть в библиотеке.")
            return

    while True:
        try:
            rating = int(input("⭐ Оценка (1-5): "))
            if 1 <= rating <= 5: break
            print("Оценка должна быть от 1 до 5.")
        except ValueError:
            print("Введите целое число.")

    date_input = input("📅 Дата прочтения (YYYY-MM-DD) [Enter - сегодня]: ").strip()
    if not date_input:
        date_input = datetime.now().strftime("%Y-%m-%d")
    else:
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
        except ValueError:
            print("⚠️ Неверный формат даты. Использована текущая дата.")
            date_input = datetime.now().strftime("%Y-%m-%d")

    books.append({"author": author, "title": title, "rating": rating, "date": date_input})
    save_books(books)
    print("✅ Книга успешно добавлена.")

def show_books(books):
    if not books:
        print("📚 Библиотека пуста.")
        return
    print(f"\n{'№':<3} | {'Название':<30} | {'Автор':<20} | {'Оценка':<6} | {'Дата':<10}")
    print("-" * 80)
    for i, b in enumerate(books, 1):
        print(f"{i:<3} | {b['title']:<30} | {b['author']:<20} | {b['rating']:<6} | {b['date']:<10}")
    print()

def show_avg_rating(books):
    if not books:
        print("📊 Нет данных для расчёта средней оценки.")
        return
    avg = sum(b["rating"] for b in books) / len(books)
    print(f"📊 Средняя оценка по всем книгам: {avg:.2f}\n")

def show_author_stats(books):
    if not books:
        print("👥 Нет данных для статистики по авторам.")
        return
    stats = {}
    for b in books:
        stats[b["author"]] = stats.get(b["author"], 0) + 1
    print("👥 Статистика по авторам:")
    for author, count in sorted(stats.items()):
        print(f"  • {author}: {count} кн.")
    print()

def delete_book(books):
    if not books:
        print("📚 Библиотека пуста.")
        return
    show_books(books)
    while True:
        try:
            idx = int(input("Введите номер книги для удаления: ")) - 1
            if 0 <= idx < len(books):
                removed = books.pop(idx)
                save_books(books)
                print(f"🗑️ Удалена: \"{removed['title']}\" ({removed['author']})\n")
                return
            else:
                print("❌ Неверный номер. Попробуйте снова.")
        except ValueError:
            print("❌ Введите целое число.")

def main():
    books = load_books()
    menu = (
        "\n📖 МЕНЮ ТРЕКЕРА КНИГ\n"
        "1. Добавить книгу\n"
        "2. Показать все книги\n"
        "3. Показать среднюю оценку\n"
        "4. Статистика по авторам\n"
        "5. Удалить книгу\n"
        "6. Выход\n"
    )
    while True:
        print(menu)
        choice = input("Выберите действие (1-6): ").strip()
        if choice == "1": add_book(books)
        elif choice == "2": show_books(books)
        elif choice == "3": show_avg_rating(books)
        elif choice == "4": show_author_stats(books)
        elif choice == "5": delete_book(books)
        elif choice == "6": print("👋 До свидания!"); break
        else: print("⚠️ Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()