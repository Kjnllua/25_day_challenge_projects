def display_menu():
    print("\nNote-Taking Application")
    print("1. Add a Note")
    print("2. View Notes")
    print("3. Delete a Note")
    print("4. Exit")


def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note added successfully.")


def view_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
        if notes:
            print("\nYour Notes:")
            for idx, note in enumerate(notes, start=1):
                print(f"{idx}. {note.strip()}")
        else:
            print("No notes found.")
    except FileNotFoundError:
        print("No notes found.")


def delete_note():
    view_notes()
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
        if notes:
            note_num = int(input("Enter the note number to delete: "))
            if 1 <= note_num <= len(notes):
                del notes[note_num - 1]
                with open("notes.txt", "w") as file:
                    file.writelines(notes)
                print("Note deleted successfully.")
            else:
                print("Invalid note number.")
    except FileNotFoundError:
        print("No notes found.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            delete_note()
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
