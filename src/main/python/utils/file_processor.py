import os
from math import ceil


def encrypt(data, e, n):
    return pow(int(data), e, n)


def decrypt(data, d, n):
    return pow(int(data), int(d), int(n))


def conduct_file_processed(source_file_path, target_file_path, e_or_d, n, read_bit_width, does_encrypt, signal):
    byte_width = int(read_bit_width / 8)

    file_size = os.path.getsize(source_file_path)

    with open(source_file_path, "rb") as fin:
        with open(target_file_path, "wb+") as fout:
            duration = ceil(file_size / 10)
            count = 0
            sub_count = 0
            while True:

                count += byte_width
                sub_count += byte_width
                if sub_count >= duration:
                    sub_count = 0
                    print("{:.1f}%".format(count / file_size * 100))
                    signal.emit(count / file_size)

                b = fin.read(byte_width)
                if b == b'':
                    break
                else:
                    data_int = int().from_bytes(b, "big")
                if does_encrypt:
                    data_encoded_int = encrypt(data_int, e_or_d, n)
                    fout.write(data_encoded_int.to_bytes(byte_width * 2, "big"))
                else:
                    data_decoded_int = decrypt(data_int, e_or_d, n)
                    fout.write(data_decoded_int.to_bytes(byte_width // 2, "big"))

    signal.emit(-1)


def read_write_byte(source_file_path, target_file_path, bit_width, n, e, d):

    byte_width = int(bit_width / 8)
    with open(source_file_path, "rb") as fin:
        with open(target_file_path, "wb+") as fout:
            while True:
                b = fin.read(byte_width)
                data_int = int().from_bytes(b, "big")
                data_encoded_int = encrypt(data_int, e, n)
                data_decoded_int = decrypt(data_encoded_int, d, n)
                print("raw: {:x}, encoded: {:x}, decoded: {:x}".format(data_int, data_encoded_int, data_decoded_int))
                if b == b'':
                    break
                fout.write(data_decoded_int.to_bytes(byte_width, "big"))


if __name__ == "__main__":
    # conduct_file_processed("D:/test.txt", "D:/test.txt.tjl", 35317, 35621, 8, True)
    # conduct_file_processed("D:/test.txt.tjl", "D:/final.txt", 18829, 35621, 16, False)

    conduct_file_processed("D:/test.png", "D:/test.png.tjl", 35317, 35621, 8, True)
    conduct_file_processed("D:/test.png.tjl", "D:/final.png", 18829, 35621, 16, False)

    # conduct_file_encoded("D:/test.txt", "D:/test.txt.tjl", 193, 143, 8)
    # conduct_file_decoded("D:/test.txt.tjl", "D:/final.txt", 97, 143, 8)

    # conduct_file_encoded("D:/test.txt", "D:/test.txt.tjl", 15317789, 8873957, 24)
    # conduct_file_decoded("D:/test.txt.tjl", "D:/final.txt", 2473109, 8873957, 24)

    # conduct_file_encoded("D:/test.txt", "D:/test.txt.tjl", 65537, 2532047633, 32)
    # conduct_file_decoded("D:/test.txt.tjl", "D:/final.txt", 1580616305, 2532047633, 32)

    # read_write_byte("D:/test.txt", "D:/final.txt", 32, 2532047633, 65537, 1580616305)
    # read_write_byte("D:/test.txt", "D:/final.txt", 8, 35621, 35317, 18829)
