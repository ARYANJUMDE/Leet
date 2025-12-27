# Last updated: 12/27/2025, 6:57:07 PM
class Solution(object):
    def detectCapitalUse(self, word):
        return word.isupper() or word.islower() or word.istitle()

        