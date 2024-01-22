def calculate_price_per_unit_weight(weights, prices, output):
    weights_data = []
    prices_data = []

    weights_file = open(weights, 'r')
    weights_data = weights_file.readlines()
    weights_file.close()

    prices_file = open(prices,'r')
    prices_data = prices_file.readlines()
    prices_file.close()

    if len(weights_data) != len(prices_data):
        print("Both file must have equal size")
        return

    output_file = open(output, 'w')

    for i in range(len(weights_data)):
        w = float(weights_data[i].strip())
        p = float(prices_data[i].strip())
        result = p / w
        output_file.write(f"{result:.2f}\n")

    print("Data Stored")

f1 = 'file1.txt'
f2 = 'file2.txt'
output = 'output.txt'
calculate_price_per_unit_weight(f1, f2, output)
