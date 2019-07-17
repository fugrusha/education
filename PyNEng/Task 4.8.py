# Задание 4.8

IP = '192.168.3.1'

nums = list(map(int, IP.split('.')))

print(
  '''
  {0:<8} {1:<8} {2:<8} {3:<8}
  {0:08b} {1:08b} {2:08b} {3:08b}
  '''.format(nums[0], nums[1], nums[2], nums[3])
)

print(nums)