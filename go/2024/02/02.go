package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, _ := os.Open("../../in.txt")
	scanner := bufio.NewScanner(file)

	var reports [][]int

	for scanner.Scan() {
		s := strings.Fields(scanner.Text())
		var report []int

		for _, c := range s {
			var n int
			n, _ = strconv.Atoi(c)
			report = append(report, n)
		}

		reports = append(reports, report)
	}
	part1(reports)
	part2(reports)
}

func isSafe(report []int) bool {
	var increasing bool
	if report[1] > report[0] {
		increasing = true
	}

	for i, _ := range report {
		if i == 0 {
			continue
		}
		if report[i] == report[i-1] {
			return false
		} else if increasing && (report[i] < report[i-1] || report[i]-report[i-1] > 3) {
			return false
		} else if !increasing && (report[i] > report[i-1] || report[i-1]-report[i] > 3) {
			return false
		}
	}
	return true
}

func part1(reports [][]int) {
	var res int
	for _, report := range reports {
		if isSafe(report) {
			res++
		}
	}
	fmt.Println(res)
}

func part2(reports [][]int) {
	var res int
	for _, report := range reports {
		if isSafe(report) {
			res++
			continue
		}
		for i, _ := range report {
			slice := []int{}
			slice = append(slice, report[:i]...)
			slice = append(slice, report[i+1:]...)
			if isSafe(slice) {
				res++
				break
			}
		}
	}
	fmt.Println(res)
}
