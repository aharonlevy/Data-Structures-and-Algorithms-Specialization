# python3
import copy
from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


class Worker:
    def __init__(self, worker_id, when_start):
        self.worker_id = worker_id
        self.when_start = when_start


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result


def assign_jobs_fast(n_workers, jobs):
    results = []

    # initialize workers heap
    min_work_heap = [Worker(i, 0) for i in range(n_workers)]

    # iterate through job time array and update the min heap accordingly
    for job in jobs:
        results.append(copy.deepcopy(min_work_heap[0]))
        update_top_worker(min_work_heap, job)
    return results


def update_top_worker(min_work_heap, time_to_add):
    min_work_heap[0].when_start += time_to_add
    sift_down(min_work_heap, 0)


def sift_down(min_work_heap, index):
    while index < len(min_work_heap):
        left_child = (index * 2) + 1
        right_child = left_child + 1
        min_child = -1

        # find minimal child index
        if right_child >= len(min_work_heap):
            if left_child >= len(min_work_heap):
                break
            min_child = left_child
        else:
            if (
                min_work_heap[left_child].when_start
                < min_work_heap[right_child].when_start
            ):
                min_child = left_child
            elif (
                min_work_heap[left_child].when_start
                == min_work_heap[right_child].when_start
            ):
                if (
                    min_work_heap[left_child].worker_id
                    <= min_work_heap[right_child].worker_id
                ):
                    min_child = left_child
                else:
                    min_child = right_child
            else:
                min_child = right_child

        # if needed sift down else break
        if min_work_heap[index].when_start > min_work_heap[min_child].when_start:
            min_work_heap[index], min_work_heap[min_child] = (
                min_work_heap[min_child],
                min_work_heap[index],
            )
            index = min_child
        elif min_work_heap[index].when_start == min_work_heap[min_child].when_start:
            if min_work_heap[index].worker_id <= min_work_heap[min_child].worker_id:
                break
            else:
                min_work_heap[index], min_work_heap[min_child] = (
                    min_work_heap[min_child],
                    min_work_heap[index],
                )
                index = min_child
        else:
            break


def build_heap(min_work_heap):
    index = (len(min_work_heap) - 2) // 2
    while index >= 0:
        sift_down(min_work_heap, index)
        index -= 1


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs_fast(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker_id, job.when_start)


if __name__ == "__main__":
    main()
