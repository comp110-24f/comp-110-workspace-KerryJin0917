"""Examples of dictionary syntax with Ice cream Shop order tallies."""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

print(len(ice_cream))

ice_cream["mint"] = 10

mint_orders: int = ice_cream["mint"]
print(mint_orders)


# Re-assign values in a dictionary
ice_cream["mint"] = ice_cream["mint"] + 1
ice_cream["mint"] += 1

# Remove items by key using the pop method
ice_cream.pop("strawberry")

# Test if a key is in th dictionary
print("strawberry" in ice_cream)
print("vanilla" in ice_cream)

# Loop through items using for-in loops
for flavor in ice_cream:
    tally: int = ice_cream[flavor]
    print(f"{flavor}: {tally}")
