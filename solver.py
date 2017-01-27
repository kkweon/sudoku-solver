import time
import random
from multiprocessing import Pool
from solution import solve, display, grid_values

def read_data(file):
    with open(file, 'r') as f:
        data = f.readlines()
    return [line.strip() for line in data if len(line) > 80]


def time_it(fn, *args):
    toc = time.time()
    result = fn(*args)
    tic = time.time()

    return tic-toc, result

def multi_process(fn, args_list, cores=4):
    pool = Pool(processes=cores)
    result = pool.map_async(fn, args_list)
    return result.get()


def get_success_rate(list_):
    return sum([1 for x in list_ if x != False ] )/len(list_)


def analyze_one(data):
    return time_it(solve, data)


def analyze_all(data, cores=4):
    outcome = multi_process(analyze_one, data, cores)
    time_list = [item[0] for item in outcome]
    success_rate_list = [item[1] for item in outcome]

    result = {
        'min_time': min(time_list),
        'max_time': max(time_list),
        'avg_time': sum(time_list) / len(time_list),
        'solve_rate': get_success_rate(success_rate_list)
    }

    return result 

def main(path, sample=False, label="Hard"):
    data = read_data(path)
    if sample:
        data = random.sample(data, sample)
    else:
        sample = len(data)
    result = analyze_all(data)

    print(f"Solving [{label}] Puzzles of {sample}")
    for k, v in result.items():
        if k == "solve_rate":
            print(f"{k}\t: {v:.2%}")
        else:
            print(f"{k}\t: {v:.3f}")

if __name__ == '__main__':
    easy_trial = 100
    hard_trial = 100

    easy_path = "data/easy1011.txt"
    hard_path = "data/hard2365.txt"
    norvig_path = "data/top95.txt"
    norvig_hardest_path = "data/hardest11.txt"

    main(easy_path, easy_trial, "Easy")
    main(hard_path, hard_trial, "Hard")

    main(norvig_path, label="Norvig 95")
    main(norvig_hardest_path, label="Norvig Hardest 11")

    


