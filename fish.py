A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]


# f1 eats f2 and then f3
# f4 each f1

def solution(A, B):
    """
    fishy thing
    """
    # comblist = zip(A, B)

    fishlist = [(s, d) for (s, d) in zip(A, B)]

    for index in range(len(fishlist)):
        if index+1 <= len(fishlist)-1:
            curr_fish = fishlist[index]
            next_fish = fishlist[index+1]

            # check directions
            if curr_fish[1] == 1: # fish is going upsteeam
                if curr_fish[1] != next_fish[1]: # and next fish is going opposite way
                    print(fishlist)
                    print("")
                    print(f"curr fish dir {curr_fish[1]}, next fish dir {next_fish[1]} ")
                    # if currfish is bigger and meaner
                    if curr_fish[0] > next_fish[0]:
                        print("")
                        print(f"currfish size {curr_fish[0]},nxtfish size {next_fish[0]} ")
                        print(f"fish {index} ate fish {index+1}")
                        fishlist.pop(index+1)  # kill nextfish
                        fishlist.insert(index+1, curr_fish)
                        fishlist.pop(index)
                        print(fishlist)
                        new_A, new_B = zip(*fishlist)
                        fishlist = solution(new_A, new_B)
                    else:
                        fishlist.pop(index)  # kill nextfish
                        fishlist.insert(index, curr_fish)
                        fishlist.pop(index+1)
                        new_A, new_B = zip(*fishlist)
                        fishlist = solution(new_A, new_B)

    return fishlist


lst = solution(A, B)

print("==========")
print(lst)
print(len(lst))


# print(len(f))
