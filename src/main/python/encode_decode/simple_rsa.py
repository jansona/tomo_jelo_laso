# Inspired by https://github.com/keon/algorithms/blob/master/algorithms/maths/rsa.py
import random
import rsa


class RSA(object):

    def __init__(self):
        self.n, self.e, self.d = None, None, None

    def generate_key_with_rsa(self, width):

        p, s = rsa.newkeys(width)
        self.n = s.n
        self.e = s.e
        self.d = s.d
    
    def generate_key(self, width, seed=None):
        """
        the RSA key generating algorithm
        k is the number of bits in n
        """

        def modinv(a, m):
            """calculate the inverse of a mod m
            that is, find b such that (a * b) % m == 1"""
            b = 1
            while not (a * b) % m == 1:
                b += 1
            return b

        def gen_prime(k, seed=None):
            """generate a prime with k bits"""

            def is_prime(num):
                if num == 2:
                    return True
                for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0:
                        return False
                return True

            random.seed(seed)
            while True:
                key = random.randrange(int(2 ** (k - 1)), int(2 ** k))
                if is_prime(key):
                    return key

        # size in bits of p and q need to add up to the size of n
        p_size = width / 2
        q_size = width - p_size

        e = gen_prime(width, seed)  # in many cases, e is also chosen to be a small constant

        while True:
            p = gen_prime(p_size, seed)
            if p % e != 1:
                break

        while True:
            q = gen_prime(q_size, seed)
            if q % e != 1:
                break

        n = p * q
        l = (p - 1) * (q - 1)  # calculate totient function
        d = modinv(e, l)

        self.n, self.e, self.d = int(n), int(e), int(d)

        return self.n, self.e, self.d

    def encrypt(self, data):
        return pow(int(data), int(self.e), int(self.n))

    def decrypt(self, data):
        return pow(int(data), int(self.d), int(self.n))


if __name__ == "__main__":
    rsa = RSA()
    N, E, D = rsa.generate_key(16)
    test_data = 25
    encrypted = pow(test_data, E, N)
    decrypted = pow(encrypted, D, N)
    print("n:", N)
    print("e:", E)
    print("d:", D)
    print("data:", test_data)
    print("encrypted:", encrypted)
    print("decrypted:", decrypted)
    assert decrypted == test_data
