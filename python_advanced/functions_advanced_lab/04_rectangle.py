def rectangle(width, height):
    if not isinstance(width, int) or not isinstance(height, int):
        return "Enter valid values!"

    def area():
        return width * height

    def perimeter():
        return 2 * (width + height)

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"