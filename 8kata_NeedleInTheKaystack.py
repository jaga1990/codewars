def find_needle(array_of_junk):
    for i in range(len(array_of_junk)):
        if array_of_junk[i] == "needle":
            #print("found the needle at position " + str(i))
            return "found the needle at position " + str(i)

find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"])