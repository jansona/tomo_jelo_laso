def encrypt(data, e, n):
    return pow(int(data), int(e), int(n))


def decrypt(data, d, n):
    return pow(int(data), int(d), int(n))


def conduct_file_encoded(source_file_path, target_file_path, e, n, bit_width):
    byte_width = int(bit_width / 8)

    with open(source_file_path, "rb") as fin:
        with open(target_file_path, "wb+") as fout:
            while True:
                b = fin.read(byte_width)
                if b == b'':
                    break
                else:
                    data_int = int().from_bytes(b, "big")
                data_encoded_int = encrypt(data_int, e, n)
                fout.write(data_encoded_int.to_bytes(byte_width, "big"))


def conduct_file_decoded(source_file_path, target_file_path, d, n, bit_width):
    byte_width = int(bit_width / 8)

    with open(source_file_path, "rb") as fin:
        with open(target_file_path, "wb+") as fout:
            while True:
                b = fin.read(byte_width)
                if b == b'':
                    break
                else:
                    data_int = int().from_bytes(b, "big")
                data_encoded_int = decrypt(data_int, d, n)
                fout.write(data_encoded_int.to_bytes(byte_width, "big"))


if __name__ == "__main__":
    conduct_file_encoded("D:/code/TestPlace/tomo_jelo_laso/src/main/python/main.py", "D:/main.tjl", 227, 143, 8)
    conduct_file_encoded("D:/main.tjl", "D:/main.py", 83, 143, 8)
