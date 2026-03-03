n = int(input())

arr = list(map(int, input().split()))

max_total = -1

for i in range(n):

    for j in range(i + 1, n):

        for k in range(j + 1, n):

            a = arr[i]

            b = arr[j]

            c = arr[k]

            

            S = a*b + b*c + a*c

            

            if S % 2 == 1:

                total = a + b + c

                if total > max_total:

                    max_total = total

print(max_total)