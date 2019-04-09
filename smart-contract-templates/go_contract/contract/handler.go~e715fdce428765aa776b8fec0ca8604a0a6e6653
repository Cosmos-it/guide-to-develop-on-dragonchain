package contract

import (
	"fmt"
	"os"
)

// Handle actual smart contract logic
func Handle(req []byte) string {
	fmt.Fprintf(os.Stderr, "This is a log\n")
	return fmt.Sprintf("Hello from golang smart contract: %s", string(req))
}
