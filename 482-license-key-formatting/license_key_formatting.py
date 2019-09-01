#!/usr/bin/env python3


class Solution:

    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace('-', '')
        n = len(S)

        if n == 0:
            return ''

        res = S[:n - n // K * K]

        for i in range(n - n // K * K, n - K + 1, K):
            res += '-' + S[i:i + K]

        res = res.upper()

        return res[1:] if res[0] == '-' else res
