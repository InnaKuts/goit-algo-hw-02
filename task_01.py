from random import randrange, randint
from queue import Queue

queue = Queue()
_request_id = 0


def generate_request():
    global _request_id
    _request_id += 1
    request = _request_id
    queue.put(request)


def process_requests():
    if queue.empty():
        print("Queue is empty")
        return
    while not queue.empty():
        request = queue.get()
        print(f"Request processed: {request}")


def main():
    while True:
        requests = randrange(10)
        for _ in range(requests):
            generate_request()
        print(f"Generated {requests} new requests")
        process_requests()


if __name__ == '__main__':
    main()
