
class Color:
    """
    Класс «Цвет фигуры»
    """
    def __init__(self):
        self._color = None
    @property
    def colorproperty(self):
        """
        Get-аксессор
        """
        return self._color
    @colorproperty.setter
    def colorproperty(self, value):
        """
        Set-аксессор
        """
        self._color = value

class FigureColor1:
    """
    Класс «Цвет фигуры»
    """
    def init(self):
        self._color = None
    def get_color(self):
        """
        Get-аксессор
        """
        return self._color

    def set_color(self, value):
        """
        Set-аксессор
        """
        self._color = value
'''
a = FigureColor()
b = FigureColor1()
a.colorproperty = 2
b.set_color(2)
print(a.colorproperty, b.get_color())
'''

