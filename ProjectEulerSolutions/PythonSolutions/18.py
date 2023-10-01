# PROJECT-EULER: PROBLEM #18 - 'Maximum Path Sum I'
# ------------------------------------------------------------------------------

TRIANGLE_STR = """          
                            75
                          95  64
                        17  47  82
                      18  35  87  10
                    20  04  82  47  65
                  19  01  23  75  03  34
                88  02  77  73  07  63  67
              99  65  04  28  06  16  70  92
            41  41  26  56  83  40  80  70  33
          41  48  72  33  47  32  37  16  94  29
        53  71  44  65  25  43  91  52  97  51  14
      70  11  33  28  77  73  17  78  39  68  17  57
    91  71  52  38  17  14  91  43  58  50  27  29  48
  63  66  04  68  89  53  67  30  73  16  69  87  40  31
04  62  98  27  23  09  70  98  73  93  38  53  60  04  23
"""
TRIANGLE_ARRAY = [line.split() for line in TRIANGLE_STR.split('\n')]
TRIANGLE_ARRAY = [list(map(int, line)) for line in TRIANGLE_ARRAY if line]

# ------------------------------------------------------------------------------

def get_max_neighbor(current_node):
    n1_val, n2_val = -1, -1
    next_row = current_node[0]+1
    next_col = current_node[1]+1
    if next_row < len(TRIANGLE_ARRAY):
        n1_val = TRIANGLE_ARRAY[next_row][current_node[1]]
        if next_col < len(TRIANGLE_ARRAY[next_row]): # This probably isn't needed as data is guaranteed triangular format.
            n2_val = TRIANGLE_ARRAY[next_row][next_col]
    else:
        return False
    if n1_val > n2_val:
        return (next_row, current_node[1])
    else:
        return (next_row, next_col)


def get_path_section(starting_node, depth):
    # Rewrite to brute-force entire section, or perform lookahead sum calculation.
    path_section = [starting_node]
    prev_node = starting_node
    for _ in range(depth):
        next_node = get_max_neighbor(prev_node)
        prev_node = next_node
        path_section.append(next_node)
        if not next_node:
            return path_section
    return path_section


def get_path(step_depth):
    path = get_path_section((0,0), step_depth)
    while path[-1]:
        path += get_path_section(path[-1], step_depth)[1:]
    return path
        

# ------------------------------------------------------------------------------

print(TRIANGLE_STR)
[print(l) for l in TRIANGLE_ARRAY]

print(get_path(4))
sum = 0
for node in get_path(4):
    if node:
        sum += TRIANGLE_ARRAY[node[0]][node[1]]
print(sum)
