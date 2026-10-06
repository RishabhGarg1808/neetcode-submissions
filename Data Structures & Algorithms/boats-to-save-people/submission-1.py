class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)

        i,j = 0,n-1

        res = 0

        while i<= j:
            sum = people[i] + people[j]

            if sum <= limit:
                i+= 1
            j -= 1
            res += 1
        return res

