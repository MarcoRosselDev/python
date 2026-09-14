from typing import Literal

status: Literal["draft", "published", "archived"] = "draft"

# Only these three values are valid
status = "draft"      # OK
status = "published"  # OK
status = "pending"    # Type checkers will warn about this
