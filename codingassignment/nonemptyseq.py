def countsequence(a: 'input sequence', b: 'size input'):
    a.sort()
    count = 0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if len(a) - j >= b-1:
                if a[i] + sum(a[j:j+b-1]) <= 1000:
                    count = count + 1
    res = count if count > 0 else "No Valid subsequence"
    return res


result = countsequence([1, 2, 8], 2)
print(result)












