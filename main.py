def lcs_length(s, t):
    from collections import Counter
    dp = Counter()

    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[i, j] = dp[i, j - 1] + 1
            else:
                dp[i, j] = max(dp[i, j - 1], dp[i - 1, j])
    return max(dp.values()) if dp else 1


print(lcs_length("meow", "homeone"))
