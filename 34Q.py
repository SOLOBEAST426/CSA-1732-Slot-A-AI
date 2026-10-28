def monkey_banana():
    monkey = "door"
    box = "window"
    banana = "window"
    on_box = False
    has_banana = False

    print("Initial state: Monkey is at the door.")

    monkey = "window"
    print("1. Monkey walks to the window.")

    if monkey == box:
        box = "under banana"
        print("2. Monkey pushes the box under the banana.")

    if monkey == "window":
        on_box = True
        print("3. Monkey climbs onto the box.")

    if on_box and monkey == banana:
        has_banana = True
        print("4. Monkey grasps the banana.")

    if has_banana:
        print("Goal achieved: Monkey has the banana.")
    else:
        print("Goal not achieved.")


monkey_banana()