class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        results = []

        # Get initial task counts
        task_counts = defaultdict(int)
        for t in tasks:
            task_counts[t] += 1

        # Maintain max-heap of tasks, ordered by count
        task_heap = []
        for task, count in task_counts.items():
            task_heap.append((count, task))
        heapq.heapify_max(task_heap)

        # Maintain a list of tasks in cooldown. 
        # - Entry = (task_id, count, timestamp)
        # - Timestamps can be a simple integer
        ts = 0
        tasks_in_cooldown = []

        # Choose the task with highest task count that is able to run
        while task_heap or tasks_in_cooldown:
            # Choose next available task
            if task_heap:
                # Select task, add to results, place in cooldown
                count, task = heapq.heappop_max(task_heap)
                results.append(task)
                count -= 1
                if count > 0:
                    if n > 0:
                        tasks_in_cooldown.append((task, count, ts))
                    else:
                        heapq.heappush_max(task_heap, (count, task))
            else:
                # Idle
                results.append("")

            # Increment timestamp and remove tasks from cooldown
            ts += 1

            for i, x in enumerate(tasks_in_cooldown):
                task, count, task_ts = x
                # If the task no longer needs to be in cooldown, then remove
                # it from cooldown and add it back to the task heap.
                if ts - task_ts > n:
                    tasks_in_cooldown.pop(i)
                    heapq.heappush_max(task_heap, (count, task))
                else:
                    break

        return len(results)













