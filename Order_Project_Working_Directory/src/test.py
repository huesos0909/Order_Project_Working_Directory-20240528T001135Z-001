import os

file_path = "test_postal_orders.txt"
with open(file_path, "w") as f:
    f.write("Test entry\n")

with open(file_path, "r") as f:
    contents = f.readlines()
    print("Test file contents:", contents)