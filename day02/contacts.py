import textwrap, time

contacts = []

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"This operation took {end_time - start_time} seconds to complete.")
        return result
    return wrapper

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}() with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper

def get_valid_input(prompt: str, allow_empty: bool = False) -> str:
    """Keep asking until the user provides non-empty input."""
    while True:
        value = input(prompt).strip()
        if value or allow_empty:
            return value
        print("This field cannot be empty.")

@logger
@timer
def add_contact(contacts: list) -> None:
    """Add a new contact to the list."""
    name = get_valid_input("Name: ")
    phone = get_valid_input("Phone: ")
    email = get_valid_input("Email: ")
    tags = set(get_valid_input("Tags (comma-separated): ").split(","))
    # Strip whitespace from tags
    tags = {tag.strip().lower() for tag in tags}
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "tags": tags
    }
    contacts.append(contact)
    print(f"Added {name}!")

@logger
@timer
def search_contacts(contacts: list, query: str) -> list:
    """Search contacts by name (partial, case-insensitive match)."""
    results = [contact for contact in contacts if query.lower() in contact['name'].lower()]
    return results

@timer
def view_contacts(contacts: list) -> None:
    """Print a list of all contacts (name, phone, email)"""
    if contacts:
        print('All contacts:')
        for contact in contacts:
            print(f"{contact['name']} ({contact['phone']}, {contact['email']})")
    else:
        print("No contacts yet.")

@timer
def filter_by_tag(contacts: list) -> list[dict]:
    """Returns results with requested tag"""
    tag = input("Enter tag: ")
    results = [contact for contact in contacts if tag.lower() in contact['tags']]
    return results

@logger
@timer
def delete_contact(contacts: list) -> str:
    """Remove contact from contacts by name (partial, case-insensitive match)"""
    delete = input("Enter name to delete: ")
    for contact in contacts:
        if delete.lower() in contact['name'].lower():
            confirmation = input(f"Are you sure you want to delete {contact['name']}? y/n: ").lower()
            if confirmation == "y":
                contacts.remove(contact)
                return f"{contact['name']} has been removed."
            else:
                return f"Cancelled."
    return "Contact not found."

@timer
def get_stats(contacts: list) -> str:
    """Return current stats (total contacts, tag count)"""
    total_contacts = len(contacts)
    tag_count = {}
    try:
        for contact in contacts:
            for tag in contact['tags']:
                tag_count[tag] = tag_count.get(tag, 0) + 1
        most_common_tag = max(tag_count, key=tag_count.get)
        return textwrap.dedent(f"""Stats:
        Total Contacts: {total_contacts}
        Most Common Tag: {most_common_tag}""")
    except ValueError:
        return f'Total Contacts: {total_contacts}\nNo Tags'


def main():
    while True:
        print("\n--- Contacts Manager ---")
        print("1. Add contact")
        print("2. Search")
        print("3. List all")
        print("4. Filter by tag")
        print("5. Delete")
        print("6. Stats")
        print("7. Quit")
        
        choice = input("\nChoice: ")
        
        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            query = input("Search query: ")
            results = search_contacts(contacts, query)
            if results:
                print('Results:')
                for contact in results:
                    print(f"- {contact['name']} ({contact['phone']}, {contact['email']})")
                    
            else:
                print("No contacts found.")
        
        elif choice == "3":
            view_contacts(contacts)
        
        elif choice == "4":
            results = filter_by_tag(contacts)
            if results:
                print("Results:")
                for contact in results:
                        print(f"- {contact['name']} ({contact['phone']}, {contact['email']})")
            else:
                print("No contacts found with tag.")

        elif choice == "5":
            print(delete_contact(contacts))

        elif choice == "6":
            print(get_stats(contacts))

        elif choice == "7":
            print("Bye!")
            break
        else:
            print("Not implemented yet!")

if __name__ == "__main__":
    main()