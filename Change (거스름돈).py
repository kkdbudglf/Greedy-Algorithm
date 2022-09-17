n = int(input())  # 거슬러 주어야 할 돈

change_list = [500, 100, 50, 10]  # 거스름돈 목록

count = 0  # 동전의 최소 개수

for coin in change_list:
    count += n // coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)
