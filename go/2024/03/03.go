package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	file, _ := os.Open("../../in.txt")
	scanner := bufio.NewScanner(file)

	var input []string
	for scanner.Scan() {
		input = append(input, scanner.Text())
	}
	s := strings.Join(input, "")

	part1(s)
	part2(s)
}

func part1(s string) {
	res := 0
	re := regexp.MustCompile(`mul\(([0-9]{1,3}),([0-9]{1,3})\)`)
	matches := re.FindAllStringSubmatch(s, -1)
	for _, match := range matches {
		x, _ := strconv.Atoi(match[1])
		y, _ := strconv.Atoi(match[2])
		res += x * y
	}
	fmt.Println(res)
}

func part2(s string) {
	var matches []string
	strs := strings.Split(s, "do()")
	for _, str := range strs {
		matches = append(matches, strings.Split(str, "don't()")[0])
	}
	part1(strings.Join(matches, ""))
}
