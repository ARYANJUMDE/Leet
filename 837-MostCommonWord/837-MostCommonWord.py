# Last updated: 12/27/2025, 6:56:51 PM
import re
from collections import Counter

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        # 1. Normalize text (lowercase + remove punctuation)
        words = re.findall(r'\w+', paragraph.lower())

        # 2. Count words excluding banned ones
        counts = Counter(word for word in words if word not in banned)

        # 3. Return the most common word
        return counts.most_common(1)[0][0]

        