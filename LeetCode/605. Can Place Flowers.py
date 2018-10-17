class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        poss_flowers = 0
        start = -2
        flowerbed.extend([0,1])
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                if i > start + 1:
                    poss_flowers += (i - start - 2) // 2
                start = i
        return poss_flowers >= n
