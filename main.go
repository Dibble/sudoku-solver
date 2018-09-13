package main

import (
	"fmt"
	"strconv"
)

type cell struct {
	value int
}

type sudoku struct {
	cells [][]cell
}

func main() {
	fmt.Println("hello world")

	puzzle := sudoku{
		cells: [][]cell{
			{{1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}},
			{{1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}},
			{{1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}},
			{{1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}},
			{{1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}},
			{{1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}},
			{{1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}},
			{{1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}},
			{{1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}},
		},
	}

	puzzle.Print()
}

func (s *sudoku) Print() {
	fmt.Println("-------------------------------------")
	for _, row := range s.cells {
		rowString := "|"

		for _, column := range row {
			rowString += " " + strconv.Itoa(column.value) + " |"
		}

		fmt.Println(rowString)
		fmt.Println("-------------------------------------")
	}
}
