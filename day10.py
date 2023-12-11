pipe_map = {                  
    '|': {( 0,  1), ( 0, -1)},
    '-': {( 1,  0), (-1,  0)},
    'L': {( 0, -1), ( 1,  0)},
    'J': {( 0, -1), (-1,  0)},
    '7': {(-1,  0), ( 0,  1)},
    'F': {( 0,  1), ( 1,  0)},
}

with open('input.txt') as f:
    grid = [list(line.strip()) for line in f.readlines()]
    distances = {}
    start = None

    for y, row in enumerate(grid):
        if 'S' in row:
            start = (row.index('S'), y)
            break

    grid[start[1]][start[0]] = 'F'
    dist = 0
    pipe = start
    
    while pipe not in distances:
        distances[pipe] = dist
        dist += 1

        x, y = pipe
        current = grid[y][x]

        for dx, dy in pipe_map[current]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in distances:
                pipe = (nx, ny)
                break

    tile_count = 0
    for y, row in enumerate(grid):
        parity = 0
        for x, c in enumerate(row):
            if (x, y) not in distances: 
                if parity % 2 == 1:
                    tile_count += 1
                continue

            if c in ['|', 'L', 'J']:  
                parity += 1            

    print("SUM", tile_count)
