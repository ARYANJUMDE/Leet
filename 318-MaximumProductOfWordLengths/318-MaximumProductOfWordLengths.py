# Last updated: 12/27/2025, 6:57:38 PM
# class Solution(object):
#     def maxProduct(self, words):
#         x=[]
#         for i in range(0,len(words)):
#             for j in range(i+1,len(words)):
#                 if not(set(words[i])&set(words[j])):
#                     x.append((words[i],words[j]))
#         if (len(x)==0):
#             return 0

#         y = max(x, key=lambda pair: len(pair[0])*len(pair[1]))
#         return len(y[0])*len(y[1])

class Solution(object):
    def maxProduct(self, words):
        # convert each word into a set of letters
        word_sets = [set(w) for w in words]
        
        max_product = 0  # answer
        
        # check every pair of words
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                # if the two sets have no common letters
                if word_sets[i].isdisjoint(word_sets[j]):
                    product = len(words[i]) * len(words[j])
                    # update answer
                    if product > max_product:
                        max_product = product
        
        return max_product


        