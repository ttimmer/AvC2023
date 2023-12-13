def find_symmetry_index(pattern,pattern_list,patternnumber):
    temp_pattern_list = []
    output =[]
    columns = len(pattern)
    for x in range(1,columns):
        left = list(pattern[0:x])
        right = list(pattern [x:columns])
        reversed_left = list(reversed(left))
        if len(right) > len(left):
            print(reversed_left,right[:len(left)])
            if reversed_left == right[:len(left)]:
                print(f'Found one right bigger{reversed_left}, {right[:len(left)]}, {x}')
                temp_pattern_list.append(x)
        elif len(right) < len(left):
            if reversed_left[:len(right)] == right:
                print(f'Found one left bigger {reversed_left[:len(right)]}, {right}, {x}')
                temp_pattern_list.append(x)
    if patternnumber>0:
        for x in pattern_list:
            if x in temp_pattern_list:
                output.append(x)
    else:
        output = temp_pattern_list
    return output

# Example usage:
input_test = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

input_actual = """#.######.#.
....##.#...
..######...
###....###.
#..####..##
.#.#..#.#.#
.#.#..#.#.#
##......###
..........#
.#.####.#.#
.#......#.#
.#......#.#
.#.####.#.#

.##...#.#...#
#######..#.#.
#..#.######.#
....###..##.#
......##.....
#..##..#...##
#..####.#....
###.#..##....
............#
#..#..#####.#
#..#..#####.#

##..#######..
.#.####.#.#..
.#.#..#..##.#
...#..#.##.#.
#.#..#....##.
#.#..#....##.
...#..#.##.#.
.#.#..#..##.#
.#.##.#.#.#..
##..#######..
#.#.##.#.....
#.....###..#.
###.....###.#
###.....###.#
#.....###..#.
#.#.##.#.....
##..#######..

#...#.##.
#...#.##.
..#.#....
...#.....
.##.##..#
##...####
#.#.#####
#.##.#...
.###.....
#.#.#####
###.##..#
.#..##..#
.#....##.

#..#.#.####
....#..#.#.
.##.#..####
.##...#..#.
####....#..
#####.##.#.
#####.##.#.
####....#..
.##...#..#.
.##.#..####
.......#.#.
#..#.#.####
....#...##.
.##.##.##.#
#..###.#..#
#..###.#.#.
....##.###.

##.##..##
.##.#..#.
#..##..#.
#.#.#..#.
....####.
##..#..#.
.#..####.
.##.####.
...#....#
...#....#
.##.####.

..#.#.##.
##..#.##.
##...#..#
##..##..#
##..##..#
##...#..#
.#..#.##.
..#.#.##.
..###....
.#.#.####
.#..#.##.
..##..##.
###..#..#
##.#.....
...#.....

######....#
##..###..##
#.####.##.#
.......##..
.####.#..#.
......####.
#....#.##.#
......#..#.
#....#....#

.#....###
#.#######
#.#######
.#....###
..##.#...
.###.#.##
.#...#.##
..####.##
...##..#.

##.#.#.#.####.#
####.#..#....#.
####.#..##..###
#...###..#..#..
#.#.#..#.####.#
###...#.##..##.
.#....#.##..##.
.#....#.##..##.
###...#.##..##.

######.##.#.##..#
..##..#.#..#..#.#
..##......#.#..##
.......##.##.#.##
..##..##....#...#
########..#####.#
#....#.###.#...#.
#########..#.#..#
######..#.#.###.#

####.#.###.#.##
...##.#..##.###
#.##.#..##.#.##
.##..##.######.
#.#...#.#..##.#
.......##..##.#
#.###......#.#.
#.###......#.#.
.......##..##.#
#.#...#.#..##.#
.##...#.######.
#.##.#..##.#.##
...##.#..##.###
####.#.###.#.##
####.#.###.#.##

..####.##
....#.#..
..#......
....#..#.
####..#..
###....#.
###..##.#
###...#..
###.#...#
###.#...#
###.#.#..
###..##.#
###....#.
####..#..
....#..#.

###...#...#
###..#..#.#
.#.##.#..##
.#.#..##.##
#...##.#..#
.##.....#..
..#..######
.....#.##.#
.#..#.###.#
#.#.#.#.#..
#.#.###.#..
#.#.###.#..
#.#.#.#.#..

.##.#..####.#.#..
###..#..###.#.###
##..###.....#..##
#........###..###
###.####..##.....
###.#.#....##.#..
###.#.#....##.#..
###.####..##.....
#........###..###
##..###.....#..##
###..#..###.#.###
.##.#..####.#.#..
......#..####.##.
##.#.#######.#...
#..#.#..#.#.#####
#....#.##.##..#..
.#....##..#......

...##..#.######.#
.######...#..#...
..#.#.#.##...###.
...#.#.#........#
##...#.#..####..#
.##.##.###....###
..#...###......##
###.#.#.#.#..#.#.
.#.#..#..#.##.#..
.##.#..###....###
#.#...##.#....#.#
####.#.##..##..##
####.#.##..##..##
#.#...##.#....#.#
.##.#..###....###
.#.#..#..#.##.#..
###.#.#.#.#..#.#.

........#######
#######.#######
#..###..#######
....#..#.#..##.
.##.#.#.#.#.##.
##.##..##.#....
#..#.#...######
.....#.#..##..#
##########.####
.##.#.##.#.####
#..#...####.##.
#..##.##..#.##.
.##.#.....##..#
#..##..##.#####
.....##..##....

#..####.##.##
.##.##.####.#
#######.##.##
####.........
#..##..####..
....##.#..#.#
.##..#.####.#
....#.#....#.
.....##....##
.##.##.#..#.#
#..##..#..#..
####.######.#
.....#.####.#
.##.##......#
#..##........

#.#..#.
.######
.######
#......
...##..
.######
...##..
###..##
.######

##.#..#.##...
.##.##.##.#..
...####.....#
##..##..###.#
.#......#.##.
..##..##...#.
....##.....#.
.##.##.##.#.#
#.#.##...#.#.
##.#..#.#####
###....###.#.
..######....#
###....####..
....##.....#.
...####...#.#
###.##.###...
###.##.###...

.##.######..#
.##.######..#
.#.###.####..
.####.##..###
...#..###.###
###.....#..#.
..##.#.##..#.
..#.##..##.#.
.#..#.#.....#
.#..#.#.....#
..#.##..##.#.
..##.#.##..#.
###.....#..#.
...#..###.###
.####.##..###
.#.###.####..
.##..#####..#

.##.##..#
.#..####.
.#..####.
.#####..#
#.##...#.
...###..#
..##.#...
#.#.....#
#...#.#..
#...#.#..
#.#.....#
..##.#...
...###..#
#.##...#.
.#####..#

##..###..#...#.
#...###..#...#.
.#.#...##..####
#..#.##....#.##
.##.##.....####
...###.###.#.#.
#..#.####...#.#
.#..###...#....
....#.#######..
.#.#.#.##...###
.#.#.#.##...###

.##...#..#...##..
##..########..###
##..#..##..#..###
...##.#..#.##....
.#...##..##...#..
..##........##...
##.###....###.###
..##...##...##...
######....##.####
...##.#..#.##....
.....#....#......
...##......##....
.......##........

.##.###.#..
####......#
.##.####.##
#...##....#
#.##.#.....
#.##.#.....
#...##....#
.##.####.##
####......#
.##.###.#..
#...#.#####
.....#.##.#
.....#.##.#
#...#.#####
.##.###.#..
####.#....#
.##.####.##

#.##......##.#.#.
..#.#....#.#.....
..#.#....#.#.....
#.##......##.#.#.
####.#..#.####.##
#.##.#..#.##.#...
##...####...###.#
###.#.#..#.#####.
..###.##.###...##
#.##.#..#.##.##.#
..#..####..#....#
#.##.#..#.##.#.#.
#..##.##.##..#.#.

#.####.#..###..
##....###.##...
..####..#.#####
#.####.#....#.#
#.####.#....#.#
..####..#.#####
##....###.##...
#.####.#..###..
.##..##....#.##
#......#.#...#.
##....#####.###
...##.....##.#.
.##..###.#.#.##
.######.#...###
.#....#....##..

#...#.##.###.
#...#.#.###.#
#...#.#.###.#
#...#.##.###.
##.#...##.#..
#.###..###.#.
###.#.#..#...
.##..###..#.#
.##..###..###
###.#.#..#...
#.###..###.#.

..#.#..####..##
....#.#.####...
..####..#.#....
#######..###...
...#..###.#..##
##.#..#.#...###
##..#..#.######
##.....#.#.#.##
##.###.###..###
#......#.#.....
..##.#.#####.##

#.#.#..
##.##..
..#####
..##.##
..##.##
..#####
##.###.
#.#.#..
#......
.#....#
.#....#
#......
#.#.#..

##.#..##..#.#
..#..####..#.
##...#..#...#
..#.##..##.#.
###..#..#..##
..###.##.###.
##.##....##.#
##.##.##.####
###.#.##.#.##
##..##..##..#
..#..#..#..#.

...#.#.
...#...
##.#...
..##.##
##..#.#
##..#..
###..##
##..#.#
###....
..#.##.
####..#

##...###.#.##
##...###.#.##
#..#..#..##..
.....#.###.#.
#.#.#..##.###
##...##.#..#.
##...##.#..#.
#.#.#..######
.....#.###.#.
#..#..#..##..
##...###.#.##

....#...######.
####.#.######.#
#..#####.#..#.#
####..#..#..#..
#..#.###.####.#
#..#.#..#.##.#.
#..#...#......#
#..#.#####..###
#####.##.#..#.#
####.##..####..
#..#.#..##..##.
#..#...##.##.##
.##..##########

.##..##..##..
.#.#.####.#..
.###....###..
..#.#..#.#...
###.#..#.####
##..####..###
.#..####..#..
##..####..###
.#...##...#..
.###....###..
##.#.##.#.###
##........###
..#..##..#...

..#..#....#..#..#
.....#....#......
..##........##...
#.#.#.#..#.#.#.#.
..#..#....#..#...
#..##..##..##..##
...##.####.##....
##............###
##............##.

.....#.#.##.#...#
#..#.#..#.##.##..
.#.#.##.#.#...#..
..##.###..#.##.##
..#.####.##.#.##.
###.....#..###..#
....#.##...###...
....#.##...###...
###.....#..###..#
..#..###.##.#.##.
..##.###..#.##.##
.#.#.##.#.#...#..
#..#.#..#.##.##..
.....#.#.##.#...#
.....#.#.##.#...#

#..#..#
##.##.#
#....#.
#....#.
##.##.#
#..#..#
.#...#.
##.###.
..#..#.
..##.#.
##.###.

.##...##.##
.##.#######
.##.###.##.
####.##..#.
#######.###
.##..#.##.#
....###.###
......#....
#..#.###.#.
#######..#.
#####.#.#.#
.##.##..##.
.##.##..##.
#####.#.#.#
######...#.

###..####.###
##.##.##.##..
##.##.##.##..
###..####.###
#.#..#.#.##.#
#.#..#...#.##
........#..#.

..#.####..##..#
.#..#.#........
.#..##.........
#....##........
...#.###..##..#
...##.#.##..##.
.##.#..........
..#..#.#..##..#
...#.##.##..##.
#...#..#..##..#
.#.....###..###
.#..#..........
#.####.........

..#.##....#
##.##..#.##
.#.#..#....
#####.#....
###.#...###
###.####.##
##.....####
..#.##.##..
..#.##.##..
##.....####
###.####.##
###.#...###
#####.#....
.#.#..#....
##.##..#.##

#.##.##.##.#...
#####..#####.##
..#..##..#..#..
.####..####.#..
#.#......#.#...
#.#.####.#.#.#.
.....##........
.##..##..##.#..
#.#..##..#.####
#..#.##.#..####
.#.##..##.#....
............###
.#.#....#.#.###
.##########....
..########..###

....#..#..#..
......#....#.
#####.##..##.
.....##..#.##
#..####.##.##
....#.#.##.#.
#..##.#.##.#.
....####..###
.##.#........
#..#...####..
......#....#.
#..##........
#######.##.##
........##...
.....###..###

...###..#..##..
########..####.
#..#..#..######
.##.#.###.#..#.
#.###.#########
..#....##.####.
....##.##.####.
..#............
...###.........
...#.##.#.#..#.
.#.##.##....#..
##.#.#.##.#..#.
###.##...#.##.#
..##....#..##..
#.##..#...#..#.
......####....#
......####....#

#.#..##.#
#.##...#.
#........
.......#.
.......#.
#........
#.##...#.
#.#..##.#
..#..##..
.#..#..#.
...#####.
...#####.
.#..#..#.
..#..##..
###..##.#
#.##...#.
#........

.####..#.
#.##.#.##
.####.###
#....###.
#....###.
.####.###
#.##.#.##
.####..#.
.#..#.#.#
.......##
#...##.##
##..###.#
#....###.
######.#.
##..###..

.#.###..#...###
.#.###......###
.#.###......###
.#.###..#...###
#....###..####.
..##########...
###.#..##.#.##.
....#.#.#.#...#
###....##...##.
##...#..#..##.#
.#.#.#.#.......

#.####.###.###.##
.#....#....##....
...##......#.#...
#####.##.....###.
..####...#.#...#.
.#.##.#...##..#.#
#......#####...##
..#..#....#.###..
..#..#....#.###..
#......#####...##
.#.##.#...##..#.#

######.#.#..##.
####...######..
....###.#.##.##
....#.#.#.##.##
####...######..
....#....######
#.#..#####...#.
#.#..#####...#.
....#....######
####...######..
....#.#.#.##.##
....###.#.##.##
####...######..

##....#.#.#..
###...#.#.#..
#..#...#....#
..#.###...###
#..#####.##.#
.#..#...#...#
##..##..#####
.#.#..####.#.
##..##.#.#.##
..####.#...##
..####.#...##

#.#.#..#..#
...#....##.
#.#.#..####
...####.##.
...####.##.
#.#.#..####
...#..#.##.
#.#.#..#..#
#.#..#..##.
###.#......
#..#.#.#..#
.####..#..#
#.#.####..#
#..##.#....
#.#..#.....
##.##.#....
..##..#####

..#.###
#..#...
.###.#.
..#....
#..###.
#..#.#.
..#....
.###.#.
#..#...
..#.###
..#.###

.........#...####
#######.#..#####.
##..##.#.....####
.......##.#####.#
......###.#....#.
......###.#....#.
#....#.##.#####.#
##..##.#.....####
#######.#..#####.
.........#...####
##..##..####.....

....#..#..#..
##.#..######.
##..##..##..#
...##.#.##...
####.#......#
...#..######.
....###.##.##
##..#.######.
...#.##....##
...#....##...
...##.##..##.
##.####.##.##
..###..####..

.###.####
##...##.#
..#.#.##.
#.#..#.##
#.#.#.##.
#.#...##.
####.###.
####.###.
#.#...##.
#.#.#.##.
#.#..#.##
..#.#.###
##...##.#
.###.####
.###.####

.####..#####.
#.....#..#...
#.....#..#...
.####.######.
..#.....#..#.
..##.###....#
####.#.#...##
..####.#.##..
.###...###.##
###..##....#.
###..##....#.

###.#...####...
.##...#####..##
.#..##....#....
.###...##....##
.#####.#...#...
....#.#...#.###
.####.###..#.##
....###..###...
....###..###...
.########..#.##
....#.#...#.###

.##.#.#.#.#
#..#..#...#
....#...#..
#..###.####
#..##.####.
.....##..#.
#..##.##..#
####.#...#.
#..#....#..
#..#....#..
######...#.

#..###...
.##.#####
.......#.
.......#.
.##.#####
#..###...
.##..#.##
...#.#.#.
.##..###.
.....###.
#..##.###
.##..###.
.##......
#..#..#.#
....###.#
#..##.#.#
.##.#.#.#

###.#.###........
.#.#..#.#........
.#...##..########
#.####.##...##...
.#.#..#.###....##
.###.#...##....##
#.#..#..#..#..#..
##.#.#.#...#..#..
#######...#....#.

##.#..##.####.##.
######....##....#
##.####..####..##
##...##.######.##
.....##...##...##
....###...##...##
..##.###..##..###
...######....####
##...#....##....#
..#######....####
...#.####....####
##.......#..#....
..#.##.#.#..#.#.#
##.#...########..
####..##.##.#.##.

.##.####...#.
.....#..#....
#..####.#.##.
.##..#...#...
####.##.#.#.#
###.#....#..#
#..#.##...#..
####....#####
.##.##....#.#
#..#..#..##..
#..#..#..##..
.##.##....#.#
####....#####

#..#.##.#
##.#.##.#
...#.##.#
..#######
.#.##..##
#..##..##
##.######
..###..##
.##..###.
####....#
...######
.....##..
.....##..
...######
####....#
.##..###.
..###..##

####...
####...
##.####
......#
#....#.
#.#...#
..#....
..#....
#.....#

#..#...#.
##.#...#.
##.#...#.
#..#...#.
..#.....#
..##.##..
.#......#
.#.##.###
###.....#

#.####.#..##..##.
########.##.##.##
###..###.#.#..#.#
##....####.####.#
#..##..##.#....#.
.#.##.#.##.#..#.#
...##....#.####.#
#..##..########.#
##....##..#....#.
##....##.###..###
........#..#..#..
.........#.####.#
.#.##.#..########
.#....#.#########
##....##..#.##.#.

##.#.....
#..#.....
.#....#..
.#..##.##
#...##..#
#..#..#.#
###.#....
..##.#..#
##..####.
######..#
######..#
##..####.
..##.#..#
###.#....
#..#..#.#
#...##..#
.#..##.##

#...###..####..
###..#..##..##.
.#.....##.##.#.
#.###.#.##...#.
###...###.#.###
###...###.#.###
#.###.#.##...#.
.#.....##.##.#.
###..#..##..##.
#...##...####..
###..##.#.####.
#....##...#.##.
#....##...#.##.

.####.####..###
#.##.###.#..#.#
..##...##.#..##
######....##...
..##.....#..#..
##..##....##...
#....###..##..#

.#.##.#..
#.####.##
#.####.##
.#.##.#..
#.....###
#.#..#.#.
#.####.#.

##.....##.#.#
#.#.####.....
..###......##
...#.....#.##
#.#..#.....#.
#.##....#.###
....#.##.#.#.
....#.##.#.#.
#.##....#.###
#.#..#.....#.
...#.....#.##
..###......##
#.#.####.....
##.....#..#.#
##.....#..#.#
#.#.####.....
..###......##

.#..#.#.##.#.##
.##.#####.#...#
.##.#####.#.#.#
.#..#.#.##.#.##
#..#.#..#.##...
....##.#.....##
#.##....####.#.
#..##...#.#...#
....##.#####...
##...#.###.....
.#...#..#..#.#.
.#...#..#..#.#.
##...#.###.....
....##.#####...
#..##...#.#...#

#......####.#.#.#
###..#######.##..
###..#######.##..
#......####.#.#.#
#.####.##.###.#.#
#..##..###...#...
...##...##...#...
.#.##.#..##.#.###
#########.###..#.
###..####.#####..
.##..#...##..##.#
###..####.#.##...
#.#..#.#.#.#..###
#.####.##..#.##.#
.######......####

..######...#..#
#.#....#.######
#.#....#.######
..######...#..#
..#....#...#...
#..####..#.####
...#..#.#.##...
.##.##.##.....#
#..#..#..#..##.
#.#.##.#.#...##
..#....#.....##
#.##..##.##..#.
.#.#..#.#..#..#

.#...##.###..#.
.#...##..##..#.
.#..#...#......
##...#.####.###
##.#.###.##.###
..#....####..##
.##..#####..#..
..###.#..#.###.
..###.#..#.###.

.########..
#..#..#..##
.###..###.#
##.#..#.##.
..#.##.#..#
..#.##.#..#
##.#..#.###
.###..###.#
#..#..#..##
.########..
.#.####.#..
#..#..#..##
##########.
...#..#...#
##.####.###

###.###
#.#####
.#.##..
#.#.#..
.....##
..#.#..
#..##..
...#.##
...#.##
#..##..
#.#.#..
.....##
#.#.#..
.#.##..
#.#####
###.###
..#.#..

...#.#...
##..#..##
###.#..#.
##...##.#
##...#...
...#.#...
...#.#...
##...#...
##...##.#
###.#.##.
##..#..##
...#.#...
##.###.#.

..#...####.
.#.##..##..
.###..####.
.#.###....#
##..#..##..
###..##..##
.....######
..#..##..##
.###...##..
###..#....#
#.####.##.#
#.####.##.#
##...#....#

####.#....##...
.##..#.###..###
#..###..##..##.
#..##.####..###
####...##....##
....#.#.#....#.
#...#####....##

####.#..#.#
.##..####..
#..#..##..#
####......#
######..###
#..###..###
....#....#.
...#..##..#
#####....##
#..#.#..#.#
######..###

.#..#..
#.#...#
.###..#
...##..
.#...#.
.#...#.
...##..
.###..#
#.#...#
....#..
#.....#
####.#.
.....##
.....##
####.#.

####.#..#....#..#
.#..#.....##.....
..###..#.####.#..
..##.###.#..#.###
...####........##
.######..####..##
.#..#..###..###..
.##.###...##...##
...#.###......###

####.####
##...#.##
##...#.##
####.####
##.#.####
####..###
..#.##...
####..#.#
.....#...
.....##..
.#.####..
...#.##..
#..######

.##..####..
.##..####..
#...#.##.#.
#...#....#.
#.....###..
....##..##.
.#####..###

####..#.#####
...######....
#..#.##.#..##
#####..######
#.###..###.##
##........###
..##....##...
###..##..####
##...##...###
##..#..#..###
.#.######.#..
..#......#...
..#.#..#.#...
####....#####
##.##..##.###

##.#....##.......
.#...#####.######
#....#..#..#.##.#
.###..##..#......
#####.#..#.......
.#....#.###.#..#.
..#.###.##.......
...#...#.#..####.
###.##...##......
.#.#...######..##
.#.##..######..##

.##..##..
.##..##..
#..###...
.#...#...
##.#..#..
#..#..###
....#....
.######..
.##.#.#..
##.#.##..
...##...#
###..#.##
#.###..##
##.####..
.####.###

..####...##
..##.#.#...
..##.#.#...
..####....#
...####.#..
....#.#...#
...#..#....
##...#.....
..#.###.###
...#####.#.
#####..#...

#####.#....#.
#####......#.
#.######.#.##
#.######.#.##
#####......#.
#####.#....#.
##..#.#...#.#
##..#.#....##
.#####.##.###
.#.#...#.##.#
#.#.#####..##

#...########.#.##
#...########.#.##
.....###.#.#...##
..##..#.#.##.###.
###.#.#.###.###.#
..#..#.....###...
##.#.#.#.....##..
.##.##.##.####.#.
#..##.#..#.####..
#..##.#..#.####..
.##.##.##.####.#.
##.#.#.#.....##..
..#..#.....###...
###.#.#.###.###.#
..##..#.#..#.###.
.....###.#.#...##
#...########.#.##

####..####.
####.#..#..
....#..###.
####..###..
...##.#####
..##..##..#
##...#..#..
####..##.##
###...##.##
##.####..##
####......#
...#.....#.
...#.....#.
####.#....#
##.####..##

...#....##..#
......#.#..##
....#..##...#
....##.###.#.
##...###...#.
###.###....#.
.....####..##
..####..#..#.
..##..##.#.##
..##.......#.
...####.....#
..######.##.#
...#####.##.#

.#.##.#...#..
...##...##.#.
#.####.##.#.#
#.####.##.###
...##...##.#.
.#.##.#...#..
..........#..

##.##..#..#
#.##.####..
..##....###
#....##..##
...#...##.#
#.#..#.#.#.
##....####.
..#..###.##
..#..###.##
##....####.
#.#..#.#.#.
...#...##.#
#.#..##..##
..##....###
#.##.####..
##.##..#..#
##.##..#..#

...#.##.#.....#..
...#.##.#.....#..
#....###.#.###.##
.#####.##.#.#..#.
##..###.##..###..
#.#####.##.#....#
...#....#..##.##.
...#....#..##.##.
#.#####.##.#....#
#...###.##..###..
.#####.##.#.#..#.

#.##.##.##.##
#...####...##
#.##....#####
###......####
.#.#.##.#.#..
###..##..####
#.###..###.##

##.#####.#####...
##.#.#####...####
..#..##.#.#.##.#.
###.#....##.#....
..##.#...........
####.#.##..#....#
.####..#..#...##.
###..####.#.##.#.
#######..#...#...
######..#....##..
..###.#.##.......
...#.####...###.#
...#.####...###.#

########.#.#..#
##.#..##..####.
#####..#.......
####.##..#.####
#..#.##.###.#..
.....#.#.#.####
#####....#...#.
#####.#.......#
.##...#..#.#...
.##...#..#.#...
#####.#.......#"""

patterns = input_actual.split("\n\n")
summed =0
for pattern in patterns:

    pattern = pattern.splitlines()
    print(pattern)
    i=0
    Horizontal = []
    for x in pattern:
        Horizontal = find_symmetry_index(x,Horizontal,i)

        i+=1

    print(Horizontal)

    vertical = []
    vertical = find_symmetry_index(pattern,vertical,0)
    horizontalindex = 0
    verticalindex =0
    if len(Horizontal)>0:
        horizontalindex = int(Horizontal[0])
    if len(vertical)>0:
        verticalindex = int(vertical[0])
    summed += horizontalindex + 100*verticalindex
print(summed)
