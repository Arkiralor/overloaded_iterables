from os import path, makedirs
from secrets import choice
from src.overloaded_iterables.classes import OverloadedList, Queue, Stack

from src.overloaded_iterables.utils import write_env_to_file

def main():
    # BASE_DIR = path.dirname(__file__)
    # save_dir = path.join(BASE_DIR, "media", "graphs")
    # if not path.exists(save_dir):
    #     makedirs(save_dir)
    # elements = [i for i in range(1, 100)]
    # arr = OverloadedList([choice(elements) for _ in range(1, 100)])

    # _ = arr.hist(
    #     bins=arr.len, 
    #     title='test-figure', 
    #     # save_dir=save_dir, 
    #     show=True, 
    #     histtype='step'
    # )

    # _ = write_env_to_file(file_path='new.env')

    q = Queue([1,2,3,4,5,6])
    print(f"Q (original):\t\t{q}")
    q.insert(7)
    print(f"Q (1 inserted):\t\t{q}")
    q.pop()
    print(f"Q (1 popped):\t\t{q}")

    s = Stack([1,2,3,4,5,6])
    print(f"S (original):\t\t{s}")
    s.insert(7)
    print(f"S (1 inserted):\t\t{s}")
    s.pop()
    print(f"S (1 popped):\t\t{s}")


if __name__=="__main__":
    main()