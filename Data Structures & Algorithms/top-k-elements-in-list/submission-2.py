from typing import List
from typing import DefaultDict
from sortedcontainers import SortedSet


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_to_count = {}
        count_to_number = {}
        max_counts = SortedSet([], key=lambda x: -x)
        result = []
        for i in nums:
            if i not in number_to_count:
                number_to_count[i] = 1
            else:
                number_to_count[i] += 1

        for i in number_to_count:
            count_v = number_to_count[i]
            max_counts.add(count_v)
            if count_v not in count_to_number:
                count_to_number[count_v] = [i]
            else:
                count_to_number[count_v] = [*count_to_number[count_v], i]

        j = 1
        while j <= k:
            for i in max_counts:
                for c in count_to_number[i]:
                    result.append(c)
                    j += 1
                    if (j > k):
                        break
                if (j > k):
                    break

        return result