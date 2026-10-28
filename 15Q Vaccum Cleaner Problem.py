def vacuum_cleaner(room_a, room_b, position):
    rooms = {"A": room_a, "B": room_b}

    while "Dirty" in rooms.values():
        print("Vacuum is in room", position)

        if rooms[position] == "Dirty":
            rooms[position] = "Clean"
            print("Room", position, "cleaned")

        position = "B" if position == "A" else "A"

    print("All rooms are clean!")

vacuum_cleaner("Dirty", "Dirty", "A")