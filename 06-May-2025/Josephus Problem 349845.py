# Problem: Josephus Problem - https://www.geeksforgeeks.org/josephus-problem/

def Josh(person: List[int], n: int, k: int, start_idx: int) -> None:
  
  if n == 1:
    print(person[0])
    return
  
  new_idx = (start_idx + k) % n
  
  person.pop(new_idx)
  
  Josh(person, n - 1, k, new_idx)