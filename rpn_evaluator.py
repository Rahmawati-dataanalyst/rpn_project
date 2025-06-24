#rpn_evaluator.py
def evaluate_rpn(tokens):
    
    stack = []

    operators = {
        '+': lambda a, b: a+b,
        '-': lambda a, b: a-b,
        '*': lambda a, b: a*b,
        '/': lambda a, b: int(a/b)
    }

    for token in tokens:
        if token not in operators:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            result = operators[token](a,b)
            stack.append(result)

    return stack[0]

#pengujian

if __name__ == "__main__":

    #contoh 1
    tokens1 = ["2", "1", "+", "3", "*"]
    print(f"input: {tokens1} Output: {evaluate_rpn(tokens1)}")

    #contoh 2
    tokens2 = ["4", "13", "5", "/", "+"]
    print(f"input: {tokens2} Output: {evaluate_rpn(tokens2)}")

    #contoh 3
    tokens3 = ["25", "3", "/", "6", "-"]
    print(f"input: {tokens3} Output: {evaluate_rpn(tokens3)}")


