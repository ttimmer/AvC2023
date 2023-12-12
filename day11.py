from collections import deque
import heapq
def dijkstra(grid, start,end):
    rows, cols = len(grid), len(grid[0])
    distances = {(i, j): float('inf') for i in range(rows) for j in range(cols)}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        current_dist, current = heapq.heappop(heap)

        if current_dist > distances[current]:
            continue

        row, col = current
        neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]

        for neighbor in neighbors:
            n_row, n_col = neighbor
            if 0 <= n_row < rows and 0 <= n_col < cols and (grid[n_row][n_col] == '.'):
                distance = distances[current] + 1
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))

    return distances

def shortest_path_length(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = deque([(start, 0)])
    while queue:
        current, length = queue.popleft()
        if current == end:
            return length+1

        if current in visited:
            continue

        visited.add(current)

        row, col = current
        neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]


        for neighbor in neighbors:
            n_row, n_col = neighbor
            # print(f"start{start}, length{length}, end {end} {grid[n_row][n_col]} and neighbors {neighbors} {end in visited}")
            if 0 <= n_row < rows and 0 <= n_col < cols and grid[n_row][n_col] == '.' and neighbor not in visited:
                queue.append(((n_row, n_col), length + 1))
            if n_row == end[0] and n_col == end[1]:
                return length

    return float('inf')  # Return infinity if no path is found


def perform_solution(input_test):
    lines = input_test.splitlines()
    length_line = len(lines[0])
    contains_galaxy = []
    galaxy_number = 1

    new_map = []
   # print(f"Start of length line and row numbers = {len(lines),length_line}")
    for row in lines:
        if not '#' in row:
            new_map.append(row)
            new_map.append(row)
        else:
            column_number = 0
            for x in row:
                if x == '#' and not column_number in contains_galaxy:
                    contains_galaxy.append(column_number)
                    galaxy_number+=1
                column_number+=1
            new_map.append(row)
   # print(f"extra rows of length line and row numbers = {len(new_map)},{len(new_map[0])}")
    for i in range(length_line):
        if i not in contains_galaxy:
            for j in range(len(new_map)):
                new_map[j] = new_map[j][:i] + '.' + new_map[j][i:]
    #print(f"extra rows of length line and row numbers = {len(new_map)},{len(new_map[0])}")
    print(new_map)
    galaxies = [(i, j) for i in range(len(new_map)) for j in range(len(new_map[0])) if new_map[i][j] == '#']
    total_length = 0
    summed =0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            start = galaxies[i]
            end = galaxies[j]
            length = shortest_path_length(new_map, start, end)
            print(f"Found path between {i+1} and {j+1} with a length of {length}")
            total_length += length

    print(total_length)
    print(summed)
    pass


if __name__ == '__main__':
    input_test = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""
    solution_test1 = 374
    answer_test_one =  perform_solution(input_test)
    if (solution_test1== answer_test_one):
        print(f"Test one succesfull {answer_test_one}")
