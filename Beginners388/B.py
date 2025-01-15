def readSnakeDimensions(NumberOfSnakes: int) -> list[list[int,int]]:
    snakeDimensions = []
    for _ in range(NumberOfSnakes):
        thickness, length = map(int, input().split())
        snakeDimensions.append([thickness, length])
    return snakeDimensions

def calculateSnakeSize(snakeDimensions: list[list[int,int]], snakeID: int, lengthIncrement: int) -> int:
    return snakeDimensions[snakeID][0] * (snakeDimensions[snakeID][1] + lengthIncrement)

def printLargestSnakeForEachIncrement(NumberOfSnakes: int, snakeDimensions: list[list[int,int]], maxLengthIncrement: int) -> None:
    for lengthIncrement in range(1, maxLengthIncrement+1):
        largestSize = 0
        for j in range(NumberOfSnakes):
            currentSize = calculateSnakeSize(snakeDimensions, j, lengthIncrement)
            if currentSize > largestSize:
                largestSize = currentSize
        print(largestSize)
        
def main():
    # Read inputs
    N, D = map(int, input().split())
    
    snakeDimensions = readSnakeDimensions(N)
    
    printLargestSnakeForEachIncrement(N, snakeDimensions, D)
    
main()