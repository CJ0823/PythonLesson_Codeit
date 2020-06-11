"""현재 index를 중심으로 좌, 우측을 탐색한 다음
현재 index의 건물의 높이와 좌, 우측 최대의 높이를 갖는 건물의 높이 중 최소값과 현재 index의 건물의 높이차를 빼준다"""


def trapping_rain(buildings):
    # 총 담기는 빗물의 양을 변수에 저장
    total_height = 0

    # 리스트의 각 인덱스을 돌면서 해당 칸에 담기는 빗물의 양을 구한다
    # 0번 인덱스와 마지막 인덱스는 볼 필요 없다
    for i in range(1, len(buildings) - 1):
        # 현재 인덱스를 기준으로 양쪽에 가장 높은 건물의 위치를 구한다
        max_left = max(buildings[:i])
        max_right = max(buildings[i:])

        # 현재 인덱스에 빗물이 담길 수 있는 높이
        upper_bound = min(max_left, max_right)

        # 현재 인덱스에 담기는 빗물의 양을 계산
        # 만약 upper_bound가 현재 인덱스 건물보다 높지 않다면, 현재 인덱스에 담기는 빗물은 0
        total_height += max(0, upper_bound - buildings[i])

    return total_height

# 테스트
print(trapping_rain([0, 3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

# 보통 결과값이 출력되는데 결과값이 잘못 출력되는 경우, 머릿속으로 생각한 앞쪽 TC의 논리는 맞지만,
# 뒤쪽 TC의 논리는 맞지 않을 경우가 있는 것 같음.
# print문으로 각 변수값들을 순차 출력하여 TC 중 어떤 부분에서 에러가 있는지 확인해야함.