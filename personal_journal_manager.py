import os
from datetime import datetime


class JournalManager:

    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self):
        entry = input("Enter your journal entry: ")

        if entry == "":
            print("Entry cannot be empty.")
            return

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file = open(self.filename, "a")
        file.write("[" + date + "]\n")
        file.write(entry + "\n\n")
        file.close()

        print("Entry added.")

    def view_entries(self):
        if not os.path.exists(self.filename):
            print("No journal entries found.")
            return

        file = open(self.filename, "r")
        data = file.read()
        file.close()

        if data == "":
            print("No journal entries found.")
        else:
            print("\nYour Journal Entries:")
            print(data)

    def search_entry(self):
        keyword = input("Enter keyword to search: ")

        if keyword == "":
            print("Please enter something to search.")
            return

        if not os.path.exists(self.filename):
            print("No journal entries found.")
            return

        file = open(self.filename, "r")
        data = file.read()
        file.close()

        entries = data.split("\n\n")
        found = False

        for entry in entries:
            if keyword.lower() in entry.lower():
                print("\n" + entry)
                found = True

        if found == False:
            print("No matching entry found.")

    def delete_entries(self):
        if not os.path.exists(self.filename):
            print("No journal entries found.")
            return

        choice = input("Delete all entries? (yes/no): ")

        if choice.lower() == "yes":
            os.remove(self.filename)
            print("All entries deleted.")
        else:
            print("Delete cancelled.")


def main():

    journal = JournalManager()

    while True:
        print("\n===== Personal Journal =====")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Search Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            journal.add_entry()

        elif choice == "2":
            journal.view_entries()

        elif choice == "3":
            journal.search_entry()

        elif choice == "4":
            journal.delete_entries()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()