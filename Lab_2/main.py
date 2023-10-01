from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import pyfiglet
import matplotlib.pyplot as plt


def main():
    r1 = Rectangle("синего", 3, 2)
    r2 = Rectangle("зеленого", 4, 3)
    r3 = Rectangle("красного", 5, 4)
    c1 = Circle("синего", 5)
    c2 = Circle("зеленого", 6)
    c3 = Circle("красного", 7)
    s1 = Square("синего", 5)
    s2 = Square("зеленого", 6)
    s3 = Square("красного", 7)


    #Первый способ
    result = pyfiglet.figlet_format("L a b a - 2", font="3-d")
    print(result)
    #Второй способ
    f = pyfiglet.Figlet(font='slant')
    ascii_art = f.renderText('programmers rule the world')
    print(ascii_art)

    #График
    squares = [r1.square(),r2.square(),r3.square(),
               c1.square(),c2.square(),c3.square(),
               s1.square(),s2.square(),s3.square()]

    fig, ax = plt.subplots()
    #заголовки
    ax.set_title("Squares", fontsize=14)
    x_value = [r1.FIGURE_TYPE[:2] + '1', r2.FIGURE_TYPE[:2] + '2', r3.FIGURE_TYPE[:2] + '3',
               c1.FIGURE_TYPE[:2] + '1', c2.FIGURE_TYPE[:2] + '2', c3.FIGURE_TYPE[:2] + '3',
               s1.FIGURE_TYPE[:2] + '1', s2.FIGURE_TYPE[:2] + '2', s3.FIGURE_TYPE[:2] + '3']

    plt.plot(x_value, sorted(squares))
    plt.xticks(rotation=90)
    plt.show()

if __name__ == "__main__":
    main()