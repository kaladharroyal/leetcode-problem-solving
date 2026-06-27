class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1                    # Minimum possible eating speed
        right = max(piles)          # Maximum possible eating speed
        answer = right              # Initialize answer to worst case
        
        while left <= right:
            mid = (left + right) // 2   # Candidate eating speed
            
            hours = 0
            for pile in piles:
                hours += ceil(pile / mid)   # Hours to eat this pile at speed mid
            
            if hours <= h:              # Can finish in time with this speed
                answer = mid            # Update answer (valid speed found)
                right = mid - 1         # Try to find smaller speed
            else:                       # Too slow, need faster speed
                left = mid + 1          # Search right half
        
        return answer