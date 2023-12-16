package main

import (
	"bufio"   // для буферизованного ввода/вывода
	"fmt"     // для форматированного ввода/вывода
	"math"    // для математических функций
	"os"      // для взаимодействия с операционной системой
	"strconv" // для преобразования строк
	"strings" // для работы со строками
)

func main() {
	coef_list := get_roots() // Получаем коэффициенты
	all_process(coef_list)   // Обрабатываем коэффициенты
}

func all_process(coef_list []float64) {
	print_ans(calculation(coef_list)) // Вычисляем корни и выводим их
}

func print_ans(root_list []float64) {
	// Если корней нет, выводим сообщение
	if len(root_list) == 0 {
		fmt.Println("Нет корней, дискриминант меньше нуля :(")
	} else {
		fmt.Println("Корни:")
		// Выводим каждый корень
		for _, e := range root_list {
			fmt.Println(e, " ")
		}
	}
}

func calculation(coef_list []float64) []float64 {
	A := coef_list[0]
	B := coef_list[1]
	C := coef_list[2]
	D := math.Pow(B, 2) - 4*A*C // Вычисляем дискриминант
	root_list := make([]float64, 0)
	all_roots := make([]float64, 0)
	// Вычисляем корни, если дискриминант неотрицательный
	if D >= 0.0 {
		root_list = append(root_list, (-B+math.Sqrt(D))/(2.0*A))
		root_list = append(root_list, (-B-math.Sqrt(D))/(2.0*A))
	}
	// Добавляем корни в список
	for _, r := range root_list {
		if r >= 0 {
			all_roots = append(all_roots, math.Sqrt(r))
			all_roots = append(all_roots, -math.Sqrt(r))
		}
	}
	// Выводим коэффициенты и дискриминант
	for _, e := range coef_list {
		fmt.Println(e, " ", D)
	}
	return all_roots // Возвращаем список корней
}

func get_roots() []float64 {
	coef_list := make([]float64, 3) // Создаем список для коэффициентов
	for i := 0; i < 3; i++ {
		coef_list[i] = check_root(i + 1) // Проверяем каждый коэффициент
	}
	return coef_list
}

func check_root(ind int) float64 {
	reader := bufio.NewReader(os.Stdin)
	for {
		fmt.Printf("Введите коэффициент %d: ", ind)
		input, _ := reader.ReadString('\n')
		coef, err := strconv.ParseFloat(strings.TrimSpace(input), 64)
		// Если введенное значение не является числом, выводим сообщение об ошибке
		if err != nil {
			fmt.Println("Ошибка. Попробуйте еще раз")
			continue
		}
		// Если первый коэффициент равен нулю, выводим сообщение об ошибке
		if coef == 0.0 && ind == 1 {
			fmt.Println("Коэффициент 1 равен 0. Так не пойдет")
			continue
		}
		return coef
	}
}
