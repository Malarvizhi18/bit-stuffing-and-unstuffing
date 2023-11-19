def bit_stuffing(data):
    stuffed_data = []
    count = 0

    for bit in data:
        if bit == '1':
            count += 1
        else:
            count = 0

        stuffed_data.append(bit)

        if count == 5:
            # After 5 consecutive '1's, add an extra '0' to stuff
            stuffed_data.append('0')
            count = 0

    return ''.join(stuffed_data)

def bit_destuffing(data):
    destuffed_data = []
    count = 0
    skip_next_zero = False

    for bit in data:
        if bit == '1':
            count += 1
        else:
            count = 0

        if skip_next_zero:
            skip_next_zero = False
        else:
            destuffed_data.append(bit)

        if count == 5 and bit != '0':
            # Skip the next '0' which was used for stuffing
            skip_next_zero = True
            count = 0

    return ''.join(destuffed_data)

if __name__ == '__main__':
    original_data = input("enter the data:")  # Example data
    stuffed_data = bit_stuffing(original_data)
    print("Stuffed Data:", stuffed_data)

    destuffed_data = bit_destuffing(stuffed_data)
    print("Destuffed Data:", destuffed_data)
