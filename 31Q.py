birds = {
    "sparrow": True,
    "parrot": True,
    "pigeon": True,
    "eagle": True,
    "penguin": False,
    "ostrich": False
}

bird = input("Enter bird name: ").lower()

if bird in birds:
    if birds[bird]:
        print(bird, "can fly.")
    else:
        print(bird, "cannot fly.")
else:
    print("Unknown bird.")