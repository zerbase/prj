class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bin_n = bin(n)[2:]
        while len(bin_n) < 32: 
            bin_n = '0' + bin_n
        return int(bin_n[::-1], 2)