from multiprocessing import Pool


def square_number(x):
    return x ** 2

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]

    with Pool(processes=3) as pool:
        results = pool.map(square_number, data)
    
    print("Results: ", results)