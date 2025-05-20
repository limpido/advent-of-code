package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	input, _ := os.ReadFile("in.txt")
	split := strings.Split(strings.TrimSpace(string(input)), "\n\n")
	patterns := strings.Split(split[0], ", ")
	targets := strings.Split(split[1], "\n")
	fmt.Println(patterns)
	fmt.Println(targets)

	p1 := 0
	p2 := 0
	cache := map[string]int{}
	var ways func(string, []string) int

	ways = func(target string, patterns []string) int {
		if n, ok := cache[target]; ok {
			return n
		}
		n := 0
		if len(target) == 0 {
			n = 1
		}
		for _, p := range patterns {
			if strings.HasPrefix(target, p) {
				n += ways(target[len(p):], patterns)
			}
		}
		cache[target] = n
		return n
	}

	for _, t := range targets {
		n := ways(t, patterns)
		if n > 0 {
			p1++
		}
		p2 += n
	}
	fmt.Println(p1, p2)
}
