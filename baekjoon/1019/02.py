import datetime
import collections


if __name__ == "__main__":
    question = input()

    val = collections.defaultdict(int)
    for idx in range(0, 10):
        val[idx] = 0

    start_time = datetime.datetime.now()

    val[0] = str(list(range(1, int(question) + 1))).count('0')
    val[1] = str(list(range(1, int(question) + 1))).count('1')
    val[2] = str(list(range(1, int(question) + 1))).count('2')
    val[3] = str(list(range(1, int(question) + 1))).count('3')
    val[4] = str(list(range(1, int(question) + 1))).count('4')
    val[5] = str(list(range(1, int(question) + 1))).count('5')
    val[6] = str(list(range(1, int(question) + 1))).count('6')
    val[7] = str(list(range(1, int(question) + 1))).count('7')
    val[8] = str(list(range(1, int(question) + 1))).count('8')
    val[9] = str(list(range(1, int(question) + 1))).count('9')

    end_time = datetime.datetime.now()
    print(f"time lapse: loop ... \t\t{end_time - start_time}")  # noqa

    for v in val.values():
        print(v, end=" ")
