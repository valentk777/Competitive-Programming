# -------------------------------------------------------------------
# runs

def run():
    while True:
        try:
            print(solve())
        except:
            break


# -------------------------------------------------------------------

def rotate_90_degree_clckwise(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        li = list(map(lambda x: x[i], matrix))
        li.reverse()
        new_matrix.append(li)

    return new_matrix
