data = [list(line) for line in open('18.txt').read().split('\n')]

def get_number_of_lit_neighbours(state, x, y):
    n = 0
    for dx, dy in [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]:
        cx, cy = x + dx, y + dy
        if 0 <= cx < len(state[0]) and 0 <= cy < len(state) and state[cy][cx] == '#':
            n += 1
    return n

def turn_on_corners_lennyface(state):
    state[0][0] = '#'
    state[0][len(state[0]) - 1] = '#'
    state[len(state) - 1][0] = '#'
    state[len(state) - 1][len(state[0]) - 1] = '#'
    return state

def next_state(previous_state):
    width = len(previous_state[0])
    height = len(previous_state)
    state = []
    for y, line in enumerate(previous_state):
        for x, cell in enumerate(line):
            if previous_state[y][x] == '#' and get_number_of_lit_neighbours(previous_state, x, y) in [2, 3]:
                state.append('#')
            elif previous_state[y][x] == '.' and get_number_of_lit_neighbours(previous_state, x, y) == 3:
                state.append('#')
            else:
                state.append('.')
    state = [state[i:i + width] for i in xrange(0, len(state), width)]
    return state

def count_on(state):
    return ''.join([''.join(line) for line in state]).count('#')

state = turn_on_corners_lennyface(data)

for _ in xrange(100):
    state = next_state(state)
    state = turn_on_corners_lennyface(state)

print count_on(state)
