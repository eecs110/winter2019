def get_hypotenuse(side1, side2):
    return (side1 ** 2 + side2 ** 2) ** 0.5

def get_area(side1, side2):
    area = (side1 * side2) / 2
    return area

def get_perimeter(side1, side2):
    perimeter = 2 * side1 + 2 * side2
    return perimeter

def write_to_file(side1, side2, file_destination):
    print(
        get_hypotenuse(side1, side2),
        get_area(side1, side2),
        get_perimeter(side1, side2),
        sep=', ',
        file=file_destination
    )