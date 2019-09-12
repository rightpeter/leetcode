#!/usr/bin/env python3

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """


class Solution:

    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        WORD_LIST_LEN = len(wordlist)
        WORD_LEN = len(wordlist[0])

        def count_match(w1, w2: str) -> int:
            res = 0
            for i in range(WORD_LEN):
                if w1[i] == w2[i]:
                    res += 1

            return res

        H = [[0 for _ in range(WORD_LIST_LEN)] for _ in range(WORD_LIST_LEN)]

        for i in range(WORD_LIST_LEN):
            for j in range(WORD_LIST_LEN):
                H[i][j] = count_match(wordlist[i], wordlist[j])

        candidates = [i for i in range(WORD_LIST_LEN)]
        for _ in range(10):
            # print(f'candidates: {candidates}')

            guess = candidates[0]
            max_match = float('inf')
            for i in candidates:
                tmp = [0] * (WORD_LEN + 1)

                for j in candidates:
                    tmp[H[i][j]] += 1

                tmp = max(tmp)
                if tmp < max_match:
                    guess = i
                    max_match = tmp

            x = master.guess(wordlist[guess])
            # print(f'guess: {wordlist[guess]}, match: {x}')
            # print(f'H[guess]: {H[guess]}')

            if x == WORD_LEN:
                break

            next_candidates = []
            for i in candidates:
                if H[guess][i] == x:
                    next_candidates.append(i)
            candidates = next_candidates
