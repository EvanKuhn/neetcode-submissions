from dataclasses import dataclass
import heapq

@dataclass
class Task:
    name: str
    runs_needed: int       # number of times this task must be run
    last_run: int = -1000  # last cpu cycle count (integer) this was run
    

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Get counts of each task
        counts: List[int] = [0] * 26
        for t in tasks:
            i = ord(t) - ord('A')
            counts[i] += 1

        # Create Task objects
        workloads: List[Task] = []
        for i, c in enumerate(counts):
            if c > 0:
                name = chr(ord('A') + i)
                workloads.append(Task(name=name, runs_needed=c))

        # Put tasks into max-heap (by count of runs needed)
        task_heap = [(t.runs_needed, i) for i, t in enumerate(workloads)]
        heapq.heapify_max(task_heap)

        # Min-heap for tasks to be cooled down (ordered by last_run)
        cooldown = []

        # CPU cycle counter, as an integer counting up from 0
        cycle = 0

        while task_heap or cooldown:
            # print()
            # print(f"cycle: {cycle}")
            # print(f"- workloads: {workloads}")
            # print(f"- task_heap: {task_heap}")
            # print(f"- cooldown: {cooldown}")

            # Take tasks off the cooldown heap
            while cooldown and cycle - cooldown[0][0] > n:
                _, i = heapq.heappop(cooldown)
                task = workloads[i]
                heapq.heappush_max(task_heap, (task.runs_needed, i))

            # Choose the next task from the task heap, by max runs_needed
            if task_heap:
                _, i = heapq.heappop_max(task_heap)
                task = workloads[i]
                task.runs_needed -= 1
                task.last_run = cycle
                # print(f"- CHOSE: {task.name}")

                # Add the task to the cooldown heap
                if task.runs_needed > 0:
                    heapq.heappush(cooldown, (task.last_run, i))
            # else:
            #     print("- NO-OP")

            # Increment cycle count
            cycle += 1

        return cycle