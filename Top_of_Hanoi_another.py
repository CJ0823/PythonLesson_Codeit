def move_disk(disk_num, start_peg, end_peg):

  print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))



def hanoi(num_disks, start_peg, end_peg):



  if num_disks ==1:

    move_disk(1, start_peg, end_peg)

    return None

  num_list = [1,2,3]

  num_list.remove(start_peg)

  num_list.remove(end_peg)

  a = num_list[0]

  hanoi(num_disks-1, start_peg ,a)

  move_disk(num_disks, start_peg, end_peg)

  return hanoi(num_disks-1,a,end_peg)

hanoi(4,1,)