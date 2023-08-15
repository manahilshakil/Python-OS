import sys

if len(sys.argv) > 1:
    # Accessing the first command line argument (index 1)
    value1 = sys.argv[1]
    print("Value 1:", value1)

    # Accessing the second command line argument (index 2)
    value2 = sys.argv[2]
    print("Value 2:", value2)
else:
    print("No command line arguments provided.")
