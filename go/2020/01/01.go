package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func part1(nums []int) {
	for i, v1 := range nums {
		for _, v2 := range nums[i+1:] {
			if v1+v2 == 2020 {
				fmt.Println(v1 * v2)
				return
			}
		}
	}
}

func part2(nums []int) {
	for i, v1 := range nums {
		for j, v2 := range nums[i+1:] {
			for _, v3 := range nums[j+1:] {
				if v1+v2+v3 == 2020 {
					fmt.Println(v1 * v2 * v3)
					return
				}
			}
		}
	}
}

func main() {
	file, _ := os.Open("../../in.txt")
	scanner := bufio.NewScanner(file)

	var nums []int

	for scanner.Scan() {
		n, _ := strconv.Atoi(scanner.Text())
		nums = append(nums, n)
	}

	part1(nums)
	part2(nums)
}
