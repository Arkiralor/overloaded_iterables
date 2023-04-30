from os import path, makedirs
from secrets import choice
from src.overloaded_iterables.classes import OverloadedList

def main():
    BASE_DIR = path.dirname(__file__)
    save_dir = path.join(BASE_DIR, "media", "graphs")
    if not path.exists(save_dir):
        makedirs(save_dir)
    elements = [i for i in range(1, 100)]
    arr = OverloadedList([choice(elements) for _ in range(1, 100)])

    _ = arr.hist(
        bins=arr.len, 
        title='test-figure', 
        # save_dir=save_dir, 
        show=True, 
        histtype='step'
    )

if __name__=="__main__":
    main()