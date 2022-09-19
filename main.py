def lcs_length():
    from collections import Counter

    s = input('Введите 1 строку:')
    t = input('Введите 2 строку:')

    dp = Counter()

    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[i, j] = dp[i - 1, j] + 1
    return max(dp.values()) if dp else 1

print(lcs_length())