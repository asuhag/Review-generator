import sys
import json

# Read input data from request body
input_data = json.loads(sys.stdin.read())

# Get user input from data
user_input = input_data["input"]

# Process input and generate output
output = "You entered: " + user_input

# Send output back to client
print(output)
