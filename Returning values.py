def Calculate_area_perimeter(length,width):
    area  = length*width
    perimeter = 2*(length+width)
    return area,perimeter
length = 15
width = 13
area,perimeter = Calculate_area_perimeter(length,width)
print("The Area is:",area)
print("The Perimeter is:",perimeter)



