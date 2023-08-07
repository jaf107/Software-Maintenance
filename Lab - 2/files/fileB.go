func factorial(n int) int {
	if n == 0 {
		return 1
	}
	return factorial(n-1) * n
}

func fibonacci(n int) int {
	if n <= 0 {
		return 0
	} else if n == 1 {
		return 1
	} else {
		return fibonacci(n-1) + fibonacci(n-2)
	}
}