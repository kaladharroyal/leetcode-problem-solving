class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        result = []

        for interval in intervals:
            start = interval[0]
            end = interval[1]

            if not result:
                result.append(interval)
            else:
                last_end = result[-1][1]

                if start <= last_end:
                    result[-1][1] = max(last_end, end)
                else:
                    result.append(interval)

        return result