def filtertest():
    print("INFO: filter test served as a test for developing a filter for this program. this is to avoid error ",
          "encounters when entering non integer or float type characters in supposed int variables..\n--------------------------------------------------------\n")
    hometime=input("enter num: ")
    bedtime = "5"
    hometime = int(hometime)

    print(hometime-int(bedtime))