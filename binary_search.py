def search(input_list):
  number = 0
  left = 0
  right = len(input_list) - 1

  while left <= right:
      cur_ind = (left + right) // 2
      if number < input_list[cur_ind]:
          right = cur_ind - 1
      elif number > input_list[cur_ind]:
          left = cur_ind + 1
      else:
          return cur_ind - 1

print(search([1, 1, 1, 1, 0, 0, 0, 0, 0]))
