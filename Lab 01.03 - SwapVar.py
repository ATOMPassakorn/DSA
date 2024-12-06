"""Lab 01.03 - SwapVar"""
def convert_string_to_tuples(text_in):
  """convert_string_to_tuples"""
  values = text_in.strip('()').split(', ')
  return tuple(map(float, values[::-1]))
def swapvar():
    """Lab 01.03 - SwapVar"""
    text_in=str(input())
    laongdao_data = convert_string_to_tuples(text_in)
    print(laongdao_data)
swapvar()
