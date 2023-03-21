import datetime
import collections


if __name__ == "__main__":
    question = input()

    val = collections.defaultdict(int)
    for idx in range(0, 10):
        val[idx] = 0

    start_time = datetime.datetime.now()

    for idx in range(1, int(question) + 1):
        while idx >= 10:
            val[idx % 10] += 1
            idx = idx // 10

        val[idx % 10] += 1

    end_time = datetime.datetime.now()
    print(f"time lapse: loop ... \t\t{end_time - start_time}")  # noqa

    for v in val.values():
        print(v, end=" ")
