# rpn_evaluator.py
# Fungsi utama untuk evaluasi RPN

def evaluate_rpn(tokens):
    # Langkah 1: Inisialisasi stack kosong

    stack = []

    # Langkah 2: Definisikan operasi menggunakan dictionary dengan lambda

    operators = {
        '+': lambda a, b: a+b,
        '-': lambda a, b: a-b,
        '*': lambda a, b: a*b,
        '/': lambda a, b: int(a/b)  # Pembagian dengan pembulatan ke nol

    }

    # Langkah 3: Iterasi melalui token

    for token in tokens:
        if token not in operators:  # Jika token adalah angka
            stack.append(int(token))    # Masukkan ke stack

        else:   # Jika token adalah operator
            b = stack.pop() # Operand kedua
            a = stack.pop() # Operand pertama
            result = operators[token](a,b)  # Hitung hasil menggunakan lambda
            stack.append(result)    # Masukkan hasil ke stack


    # Langkah 4: Hasil akhir adalah elemen terakhir di stack

    return stack[0]

#pengujian

if __name__ == "__main__":

    #contoh 1
    tokens1 = ["2", "1", "+", "3", "*"] # Sama dengan (2 + 1)*3
    print(f"input: {tokens1} Output: {evaluate_rpn(tokens1)}")

    #contoh 2
    tokens2 = ["4", "13", "5", "/", "+"]
    print(f"input: {tokens2} Output: {evaluate_rpn(tokens2)}")

    #contoh 3
    tokens3 = ["25", "3", "/", "6", "-"]
    print(f"input: {tokens3} Output: {evaluate_rpn(tokens3)}")

    #contoh 4
    tokens4 = ["3", "-4", "+"]  # Sama dengan 3 + (-4)
    print(f"input: {tokens4} Output: {evaluate_rpn(tokens4)}")

