package main

import (
	"bufio"   // для буферизованного ввода/вывода
	"fmt"     // для форматированного ввода/вывода
	"math"    // для математических функций
	"os"      // для взаимодействия с операционной системой
	"strconv" // для преобразования строк
	"strings" // для работы со строками
)

type Coefficients struct {
	A, B, C float64
}

// Метод для получения коэффициентов
func (c *Coefficients) get_roots() {
	for i := 0; i < 3; i++ {
		switch i {
		case 0:
			c.A = check_coefficient(i + 1)
		case 1:
			c.B = check_coefficient(i + 1)
		case 2:
			c.C = check_coefficient(i + 1)
		}
	}
}

// Метод для вычисления корней уравнения
func (c *Coefficients) calculate() []float64 {
	D := math.Pow(c.B, 2) - 4*c.A*c.C
	root_list := make([]float64, 0)
	all_roots := make([]float64, 0)
	if D >= 0.0 {
		root_list = append(root_list, (-c.B+math.Sqrt(D))/(2.0*c.A))
		root_list = append(root_list, (-c.B-math.Sqrt(D))/(2.0*c.A))
	}
	for _, r := range root_list {
		if r >= 0 {
			all_roots = append(all_roots, math.Sqrt(r))
			all_roots = append(all_roots, -math.Sqrt(r))
		}
	}
	return all_roots
}

func main() {
	var coef Coefficients
	coef.get_roots()               // Получаем коэффициенты
	print_answer(coef.calculate()) // Выводим корни уравнения
}

// Функция для вывода корней уравнения
func print_answer(root_list []float64) {
	if len(root_list) == 0 {
		fmt.Println("Нет корней, дискриминант меньше нуля :(")
	} else {
		fmt.Println("Корни:")
		for _, e := range root_list {
			fmt.Println(e, " ")
		}
	}
}

// Функция для проверки корректности введенных коэффициентов
func check_coefficient(ind int) float64 {
	reader := bufio.NewReader(os.Stdin)
	for {
		fmt.Printf("Введите коэффициент %d: ", ind)
		input, _ := reader.ReadString('\n')
		coef, err := strconv.ParseFloat(strings.TrimSpace(input), 64)
		if err != nil {
			fmt.Println("Ошибка. Попробуйте еще раз")
			continue
		}
		if coef == 0.0 && ind == 1 {
			fmt.Println("Коэффициент 1 равен 0. Так не пойдет")
			continue
		}
		return coef
	}
}
