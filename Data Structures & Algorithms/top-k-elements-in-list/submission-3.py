class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        number_to_count = {}
        for i in nums:
            number_to_count[i] = number_to_count.get(i, 0)+1

        num_count = []
        for num, cnt in number_to_count.items():
            num_count.append((num, cnt))
        num_count = sorted(num_count, key=lambda item: item[1])
        while len(result) < k:
            result.append(num_count.pop()[0])
        return result