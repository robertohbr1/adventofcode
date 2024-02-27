cal = open("input.txt", "r", encoding="utf-8").read().split("\n")

def ret(x):
    nums = "".join(i for i in x if i.isdigit())
    return int(nums[0]) * 10 + int(nums[-1])

def subs(x):
    for i, name in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        # It's necessary to concatenate the first and last letter of the name because some lines have, for example: "oneight" (2 names joined)
        x = x.replace(name, name[0] + str(i + 1) + name[-1:]) # the first letter of the name + number + the last letter of the name
    return ret(x)


print("Round 1:", sum(map(ret, cal))) # 55386

print("Round 2:", sum(map(subs, cal)))  # 54824