# Problem: Python Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    
    name_grade_pair = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        name_grade_pair.append([name, score])
    
    second_lowest = sorted(set(
        [score for _, score in name_grade_pair]))[1]
        
    names = [
        name
        for name, grade in name_grade_pair
        if grade == second_lowest
    ]
    for name in sorted(names):
        print(name)
