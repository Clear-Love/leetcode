package utils

func Counter[T comparable](elements []T) map[T]int {
	counter := make(map[T]int)
	for _, element := range elements {
		counter[element]++
	}
	return counter
}