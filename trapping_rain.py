""" 강남역에 엄청난 폭우가 쏟아진다고 가정합시다. 정말 재난 영화에서나 나올 법한 양의 비가 내려서, 고층 건물이 비에 잠길 정도입니다.
그렇게 되었을 때, 건물과 건물 사이에 얼마큼의 빗물이 담길 수 있는지 알고 싶은데요. 그것을 계산해 주는 함수 trapping_rain을 작성해 보려고 합니다.
함수 trapping_rain은 건물 높이 정보를 보관하는 리스트 buildings를 파라미터로 받고, 담기는 빗물의 총량을 리턴해 줍니다.
예를 들어서 파라미터 buildings로 [3, 0, 0, 2, 0, 4]가 들어왔다고 합시다. 그러면 0번 인덱스에 높이 3의 건물이, 3번 인덱스에 높이 2의 건물이, 
5번 인덱스에 높이 4의 건물이 있다는 뜻입니다. 1번, 2번, 4번 인덱스에는 건물이 없습니다.
그러면 아래의 사진에 따라 총 10 만큼의 빗물이 담길 수 있습니다. 따라서 trapping_rain 함수는 10을 리턴하는 거죠. """

#물이 모이는 공간의 양 끝 건물을 dam1, dam2로 지정하고, 그 사이의 물값을 구하는 알고리즘을 만든다.
#dam1은 i, i+1 번째 건물의 높이를 비교하여 i번째가 높다면 i번쨰 건물을 dam1으로 지정하되,
#dam1과 dam2 사이 고여있는 물의 양을 water_amount로 구한뒤 새롭게 지정되는 dam1은 dam2 이후 위치에서부터 탐색되도록 한다.
#dam1과 dam2 사이에 다른 건물이 있다면 water_amount에서 해당 건물들의 값들을 합친 dam_inside 값을 빼주도록 한다.

def trapping_rain(buildings):
    # 코드를 작성하세요
    water_amount = 0
    dam_inside = 0
    dam2_index = 0
    for i in range(len(buildings)-1):
        if buildings[i] > buildings[i+1] and i >= dam2_index:
            dam1 = buildings[i]
            for j in range(i+1, len(buildings)):
                if buildings[j] >= buildings[i]:
                    dam2 = buildings[j]
                    for k in range(i+1, j):
                        if buildings[k] != 0:
                            dam_inside += buildings[k]
                    water_amount += (min(dam1,dam2)) * (j-i-1) - dam_inside
                    dam2_index = j
                    dam_inside = 0
                    break
    return water_amount
# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))