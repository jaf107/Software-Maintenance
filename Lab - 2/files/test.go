package main

import "fmt"

// Function to calculate the factorial of a number
func factorial(n int) int {
	if n == 0 {
		return 1
	}
	return n * factorial(n-1)
}

/*
This is a multi-line comment.
It spans multiple lines.
*/

func main() {
	fmt.Println("Hello, World!") // Print "Hello, World!"

	// Calculate factorial of 5 and print the result
	result := factorial(5)
	fmt.Println("Factorial of 5:", result)

	// This is a single-line comment.

	/*
		This function calculates the square of a number.
		It takes an integer as input and returns the square.
	*/
	square := func(x int) int {
		return x * x
	}

	// Calculate square of 10 and print the result
	squareResult := square(10)
	fmt.Println("Square of 10:", squareResult)
}
