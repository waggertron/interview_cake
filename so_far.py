# import requests
# from bs4 import BeautifulSoup as bs

# page = requests.get(
#     "https://www.dataquest.io/blog/web-scraping-tutorial-python/")
# print(page.status_code)
# print(page.content[:20])
# soup = bs(page.content, 'html.parser')
# h1s = soup.find_all('h1')
# for title in h1s:
#     print(title.get_text())
# print(len(soup.get_text()))
# print(soup.get_text()[:20])
words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'zooologist',
    'asymptote',
    # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]


def find_rotaion(words):
    print(len(words))

    def binary_search(start=0, end=len(words) - 1):
        print(start, end)
        if (end - start) <= 1:
            print(start, end)
            return start if words[start] < words[end] else end
        first = words[start]
        last = words[end]
        mid_i = (start + end) // 2
        mid = words[mid_i]
        if first > mid or (first < mid and mid < last):  # grab firsthalf
            return binary_search(start, mid_i)
        if mid > last:
            return binary_search(mid_i, end)
    return binary_search()


def find_rotation_2(words):
    floor_index = 0
    ceiling_index = len(words) - 1
    first_word = words[0]
    while floor_index < ceiling_index:
        guess_index = (floor_index + ceiling_index) // 2
        print(floor_index, guess_index, ceiling_index)
        if words[guess_index] >= first_word:
            floor_index = guess_index
        else:
            ceiling_index = guess_index
        print("before if", floor_index, guess_index, ceiling_index)
        if floor_index + 1 == ceiling_index:
            return ceiling_index


# print(find_rotation_2(words))

def select_movies(flight_length, movie_lengths):
    remaining_times = set()
    for time in movie_lengths:
        if time in remaining_times:
            return True
        remaining_times.add(flight_length - time)
    return False


def knapsack_dynamic(treasures, capacity):
    max_values_at_capacity = [0] * (capacity + 1)
    for cur_capacity in range(capacity + 1):
        current_max = 0
        for val, weight in treasures:
            if weight <= cur_capacity:
                max_value_using_cake = val + \
                    max_values_at_capacity[cur_capacity - weight]
                current_max = max(current_max, max_value_using_cake)
                max_values_at_capacity[cur_capacity] = current_max
    return max_values_at_capacity[capacity]


print(knapsack_dynamic([(3, 1), (4, 2)], 2))


class Stack:
    def __init__(self, *args):
        self._items = [] + list(args)

    def __len__(self):
        return len(self._items)

    def push(self, *args):
        self._items = self._items + list(args)

    def pop(self):
        try:
            last = self._items[-1]
            self._items = self._items[:-1]
            return last
        except IndexError:
            return None

    @property
    def items(self):
        return self._items[:]


class Q:
    def __init__(self, *args):
        self._in = Stack()
        self._out = Stack()
        if args:
            self._in.push(*args)

    def __len__(self):
        return len(self._in) + len(self._out)

    @property
    def items(self):
        print("in: {}\nout: {}".format(self._in.items, self._out.items))
        return (list(reversed(self._out.items)) + self._in.items)[:]

    def enqueue(self, *args):
        self._in.push(*args)

    def dequeue(self):
        if len(self._out):
            return self._out.pop()
        cur = self._in.pop()
        while(len(self._in)):
            self._out.push(cur)
            cur = self._in.pop()
        return cur
