import json

#name = input("Введите имя: ")


class GuestBook:

    def __init__(self):
        self.guests = list()

    def add(self, name):
        name = input("Введите имя: ")
        assert (name != ''), "Имя не введено"
        self.guests.append({"Guest_name": name})

    def remove(self, name):
        for guest in self.guests:
            if guest.get("Guest_name") == name:
                self.guests.remove(guest)

    def write_file(self):
        with open("guest_book.json", 'a', encoding="utf-8") as f:
            json_data = {"Guests": self.guests}
            f.write(json.dumps(json_data, ensure_ascii=False))


if __name__ == "__main__":
    guestBook = GuestBook()
    guestBook.add("User1")
    guestBook.add("User2")
    guestBook.add("User3")
    guestBook.remove("User1")
    guestBook.write_file()

print(guestBook.guests)
