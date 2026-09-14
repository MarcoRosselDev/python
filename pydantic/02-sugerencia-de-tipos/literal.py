from typing import Literal

# Required string
name: str

# Optional string (can be None)
nickname: str | None = None

# String with default
country: str = "USA"

# List of items
items: list[str] = []

# Dictionary
metadata: dict[str, str] = {}

# Specific allowed values
role: Literal["admin", "user", "guest"] = "user"
