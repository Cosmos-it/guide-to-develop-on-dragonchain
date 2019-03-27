package function

import (
	"fmt"
)

// Handle payload
func Handle(req []byte) string {
	return fmt.Sprintf("Hello from go smart contract: %s", string(req))

}
