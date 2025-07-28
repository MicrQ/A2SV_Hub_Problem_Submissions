# Problem: A - Verifying Access Keys - https://codeforces.com/gym/625306/problem/A

tests = int(input())
 
for _ in range(tests):
    n = int(input())
    key = input()
 
    prev_char = 'a'
    prev_num = '0'
    letter_seen= False
    valid = True
 
    for char in key:
        if char.isdigit():
            if letter_seen:
                valid = False
                break
            if char < prev_num:
                valid = False
                break
            prev_num = char
        else:
            letter_seen = True
            if char < prev_char:
                valid = False
                break
            prev_char = char
 
    print("YES" if valid else "NO")