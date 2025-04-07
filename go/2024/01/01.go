package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	file, _ := os.Open("../../in.txt")
	scanner := bufio.NewScanner(file)

	var left []int
	var right []int

	for scanner.Scan() {
		s := strings.Fields(scanner.Text())
		l, _ := strconv.Atoi(s[0])
		r, _ := strconv.Atoi(s[1])

		left = append(left, l)
		right = append(right, r)
	}

	part1(left, right)
	part2(left, right)
}

func part1(left []int, right []int) {
	var res int
	sort.Ints(left)
	sort.Ints(right)
	for i := 0; i < len(left); i++ {
		res += max(left[i]-right[i], right[i]-left[i])
	}
	fmt.Println(res)
}

func part2(left []int, right []int) {
	right_count := map[int]int{}
	for _, v := range right {
		right_count[v]++
	}

	var res int
	for _, v := range left {
		res += v * right_count[v]
	}
	fmt.Println(res)
}
