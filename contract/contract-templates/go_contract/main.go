package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
)

func main() {
	input, err := ioutil.ReadAll(os.Stdin)
	if err != nil {
		log.Fatalf("Unable to read standard input: %s", err.Error())
	}

	fmt.Println(Handle(input))
}

// Handle payload
func Handle(req []byte) string {
	return fmt.Sprintf("Hello from go smart contract: %s", string(req))

}
