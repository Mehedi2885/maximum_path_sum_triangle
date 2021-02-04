import copy


def maximum_path(triangle):
    """Return the maximum triangle path sum(bottom up)"""
    # deep copy of last row in triangle
    dp = copy.deepcopy(triangle[-1])

    # starting from second last row
    for row in range(len(triangle) - 2, -1, -1):
        # Going through each row and up
        for col in range(0, row + 1):
            dp[col] = triangle[row][col] + max(dp[col], dp[col + 1])
    # return very first value of deep copy as total sum
    return dp[0]


def get_triangle(triangle_filename):
    """Return a list of lists containing rows of the triangle."""
    triangle = [[int(number) for number in row.split()]
                for row in open(triangle_filename)]

    return triangle


# Please provide file path here
file = "triangle.txt"

triangle = get_triangle(file)

maximum_path(triangle)
