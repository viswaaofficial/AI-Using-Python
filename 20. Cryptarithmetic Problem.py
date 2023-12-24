import re

def solve(q):
    try:
        n = next(i for i in q if i.isalpha())  # Find the first alphabetic character in the query
    except StopIteration:
        # If no alphabetic characters found, evaluate the expression after performing some simplifications
        return q if eval(re.sub(r'(^|[^0-9])0+([1-9]+)', r'\1\2', q)) else False
    else:
        # Iterate over digits (0-9) and recursively replace the alphabetic character with each digit
        for i in (str(i) for i in range(10) if str(i) not in q):
            r = solve(q.replace(n, str(i)))  # Replace character with number
            if r:
                return r
        return False

# Driver code
if __name__ == "__main__":
    query = "TWO + TWO + THREE == SEVEN"
    result = solve(query)
    if result:
        print("Solution exists:")
        print(query)
        print(result)
    else:
        print("No solution found.")
