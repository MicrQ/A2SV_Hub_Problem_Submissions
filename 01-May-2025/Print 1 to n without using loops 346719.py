# Problem: Print 1 to n without using loops - https://www.geeksforgeeks.org/print-1-to-n-without-using-loops/

def printer(n: int) -> None:
    if n <= 0:
        return
    printer(n - 1)
    print(n, end=' ')