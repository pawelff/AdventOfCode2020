f = open("day_6.txt").read().split('\n\n')
print(sum(len(set(group.replace('\n', ''))) for group in f))
print(sum(len(set.intersection(*[set(p) for p in group.split('\n')])) for group in f))