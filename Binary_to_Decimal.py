def convert_to_decimal(A,B):
    result=0
    n=len(A)

    for i in range(n):
        digit=int(A[i])
        result=result*B+digit

    return result

A=input()
B=int(input())
decimal_value=convert_to_decimal(A,B)
print(decimal_value)
