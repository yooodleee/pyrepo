# 1차원 배열(리스트)
data = [1, 2, 3, 4, 5]
string1 = 'Hello World'
print(data[3])              # 4
print(string1[3])           # l

# 2차원 배열
data2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(data2[1][0])          # 4


# for 문을 두 번 반복하고 있습니다. -> 시간 복잡도는 어떻게 될까요? (O(n^2))
def find_alp(dataset, alphabet):
    count = 0
    for data in dataset:
        for i in range(len(data)):
            if data[i] == alphabet:
                count += i
    print(count)