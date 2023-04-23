# Convert the list [1, 2, 3, 4, 5] to [2, 4, 6, 8, 10] with list comprehension
import time

print(list([i * 2 for i in [1, 2, 3, 4, 5]]))


# Build a retry decorator with retry time and retry interval to run a function 3 time with interval of 3 sec
def retry(opr, ps):
    def retry_time(max_tries):
        for i in range(max_tries):
            opr()
            ps()

    return retry_time


def pause():
    time.sleep(1)


def operation():
    print("Operation called")


retry(operation, pause)(3)

# Build a counter generator
print(list(map(lambda count: count + 1, range(10))))
