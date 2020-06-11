#Rules
#한 번에 하나의 원판만 옮길 수 있다.
#큰 원판이 작은 원판 위에 있어서는 안된다.

def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    # 코드를 입력하세요.
    if num_disks == 0:
        return
    else:
        #hanoi(3,1,3)일 경우는 disk1이 peg3으로 가야하지만, hanoi(4,1,3)일 경우는 disk1dl peg2로 가야한다(최적화)
        #다른 경우들도 다 생각해보면, 처음에 disk1이 가야되는 위치가 disk의 숫자에 따라 바뀌게 됨을 알 수 있다.
        #따라서 hanoi함수에서 disk가 이동하는 목적지가 계속 바뀌어야 함을 알 수 있고, 실행 전 이전 실행에서 이동한 disk가
        #이동한 peg가 아닌 다른 peg를 가리키는 other_peg를 만든다.
        #other_peg는 peg 번호 1,2,3을 합친 것에서, start_peg, end_peg를 제하면 구할 수 있다.
        other_peg = 6 - start_peg - end_peg
        #재귀적으로 실행이 되며, hanoi(3,1,3) = hanoi(2,1,2) -> hanoi(1,1,3) -> hanoi(0,1,2)(None) 으로 만들어준다.
        #이것은 물리적으로 봤을 때, disk3을 3번 peg로 옮기기 위한 문제가
        #disk2를 2번 peg로 옮기기 위한 문제와 같음을 표현하는 것이다.
        #disk가 몇개이든, 최적화를 위해서는 num_disks - 1 까지의 disks가 2번 peg에 모이고, num_disks에 해당하는 disks가
        #3번 disk로 이동해야 함을 표현한 것이다.
        hanoi(num_disks-1, start_peg, other_peg)
        #hanoi(0,1,2) 이후에 hanoi(1,1,3)을 실행하면서, move_disk가 호출되도록 한다. (move_disk(1,1,3))
        move_disk(num_disks, start_peg, end_peg)
        #hanoi(2,1,2)가 실행된 상태에서 hanoi(1,1,3)이 종료되고, move(2,1,2)가 실행된다.
        #이후 2보다 1작은 1번 disk를 3번 peg에서 다시 2번 peg로 불러와야 하므로, 아래와 같이 작성한다. 즉, hanoi(1,3,2)가 된다.
        #hanoi(1,3,2) = hanoi(0,3,1) (None) + move_disk(1,3,2) + hanoi(0,3,1) (None)
        hanoi(num_disks-1, other_peg, end_peg)


# 테스트 코드 (포함하여 제출해주세요)

hanoi(3, 1, 3)