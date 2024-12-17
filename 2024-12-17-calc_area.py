# calculate area rectangle ex: calc_area(width,height)
# write a function miles_kilometrs (m) and kilometrs_miles
# write a function conversion celcius_Farenheit and Farenheit_celcius
def area_rectangle(w, l):
    return w * l


# w = width and l = length
w = float(input(f"enter width (m) : "))
l = float(input(f"enter length (m): "))

# a = area_rectangle(w, l)
# print(f"area of rectangle {a} m2")
print(f"area of rectangle (m2): ", area_rectangle(w, l))
