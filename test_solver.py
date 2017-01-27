import unittest
import time
from solver import *


class TestProcess(unittest.TestCase):
    def test_can_get_success_rate(self):
        test = [1] * 9 + [False]

        self.assertEqual(get_success_rate(test), 0.9) 

        test = [1, 3, 5, False] # Success 3/4 Fail 1/4

        self.assertEqual(1 - get_success_rate(test), 1/4)



class TestTime(unittest.TestCase):
    def test_time_it_function_returns_execution_time(self):
        sleep_seconds = 2
        self.assertAlmostEqual(time_it(time.sleep, sleep_seconds)[0], sleep_seconds, places=1)
        sleep_seconds = 1
        self.assertAlmostEqual(time_it(time.sleep, sleep_seconds)[0], sleep_seconds, places=1)
        sleep_seconds = 0
        self.assertAlmostEqual(time_it(time.sleep, sleep_seconds)[0], sleep_seconds, places=1)

class TestIO(unittest.TestCase):
    def test_read_data_can_read_file(self):
        easy_file = "data/easy1011.txt"
        data = read_data(easy_file)
        self.assertTrue(all([len(d) == 81 for d in data]))

        hard_file = "data/hard2365.txt"
        data = read_data(hard_file)
        self.assertTrue(all([len(d) == 81 for d in data]))

    def test_can_solve_actually_solve(self):
        easy_file = "data/easy1011.txt"
        data = read_data(easy_file)
        result = solve(data[0])
        self.assertTrue(result)

    def test_one_example_return_time_or_False(self):
        easy_file = "data/easy1011.txt"
        data = read_data(easy_file)
        result = analyze_one(data[0])
        self.assertEqual(type(result[0]), float)
        self.assertTrue(result[1])

        result = analyze_one("1"*81)
        self.assertEqual(type(result[0]), float)
        self.assertFalse(result[1])


def job(x):
    return x**2

class TestMultiProcess(unittest.TestCase):
    def test_multithread(self):
        result = multi_process(job, [1, 2, 4], cores=4)
        self.assertEqual(result, [1, 4, 16])


    def test_analyze_all(self):
        easy_file = "data/easy1011.txt"
        data = read_data(easy_file)
        result = analyze_all(data[:5])
        self.assertEqual(type(result), dict)

        min_time = result["min_time"]
        max_time = result["max_time"]
        avg_time = result['avg_time']
        success_rate = result['solve_rate']

        for k in result:
            self.assertEqual(type(result[k]), float)






if __name__ == '__main__':
    unittest.main()
