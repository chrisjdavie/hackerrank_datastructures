
def left_rotation(arr_in, d):

    n = len(arr_in)

    arr_out = [ 0 ]*n

    for i, a_i in enumerate(arr_in):
        i_rotated = (i - d)%n
        arr_out[i_rotated] = a_i

    return arr_out

