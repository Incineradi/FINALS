def act():
    print("INFO: this program showcases the list feature.\n")
    fruits = ["apple","banana","rtx3060"]

    print(fruits)

    print(f"i love {fruits[2]}")
    fruits.append("bloat")
    print(fruits)
    fruits.remove("bloat")
    fruits.insert(0,"gulaman")
    print(fruits)