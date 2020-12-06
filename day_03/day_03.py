with open("day_3.txt", "r") as f:
	grid = [line.strip() for line in f.readlines()]


grid_length = len(grid)
grid_width = len(grid[0])

def trees_encountered(right_slope, down_slope):
	trees = 0	
	right = 0
	down = 0
	while True:
		right += right_slope
		down += down_slope
		if down > grid_length-1:
			break
		if right > grid_width-1:
			right -= grid_width
		if grid[down][right] == '#':
			trees += 1
	return trees

	
def part_one():
	print(trees_encountered(3,1))


def part_two():
	list_of_slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
	result = 1
	for slope in list_of_slopes:
		result *= trees_encountered(slope[0], slope[1])
	print(result)


part_one()
part_two()