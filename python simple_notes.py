# simple_notes.py
# text-based notes app

notes = []

def show_menu():
    print("\n===== Simple Notes App =====")
    print("1. Add a note")
    print("2. View all notes")
    print("3. Delete a note")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        note = input("Write your note: ")
        notes.append(note)
        print("Note added!")

    elif choice == "2":
        if not notes:
            print("No notes yet.")
        else:
            print("\n--- Your Notes ---")
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note}")

    elif choice == "3":
        if not notes:
            print("No notes to delete.")
        else:
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note}")
            num = int(input("Enter note number to delete: "))
            if 1 <= num <= len(notes):
                deleted = notes.pop(num - 1)
                print(f"Deleted note: {deleted}")
            else:
                print("Invalid number.")

    elif choice == "4":
        print("Goodbye")
        break

    else:
        print("Invalid choice. Try again.")
