package main

import (
	"fmt"
	"handler/contract"
	"io/ioutil"
	"os"
)

func main() {
	input, err := ioutil.ReadAll(os.Stdin)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Unable to read standard input: %s", err.Error())
		os.Exit(1)
	}
	fmt.Print(contract.Handle(input))
}
