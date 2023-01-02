def print_segment(segment_size, total_width):

    for line_size in range(1, segment_size + 1, 2):
        print((line_size * "*").center(total_width))

def print_tree(size):
    for segment_size in range(3, size + 1, 2):
        print_segment(segment_size, size)



print_tree(12)


'''def y(i, total_width):

    for g in range(1, i + 1, 2):
        print((g * "*").center(total_width))

def print_tree(size):
    for i in range(3, x + 1, 2):
        y(i, x)



print_tree(12)'''