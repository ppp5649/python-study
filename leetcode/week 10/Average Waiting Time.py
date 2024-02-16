class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        ready = sum(customers[0])
        wait = customers[0][1]
        n = len(customers)

        for i in range(1, n):
            arrival = customers[i][0]
            time = customers[i][1]

            if ready > arrival:
                ready += time
                wait += ready - arrival
            else:
                ready = sum(customers[i])
                wait += time

        return wait / n
