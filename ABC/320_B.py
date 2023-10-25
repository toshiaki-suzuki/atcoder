def is_palindrome(s):
    n = len(s)
    for i in range(n):
        if s[i] != s[n - i - 1]:
            return False
    return True


def main():
    s = input()
    n = len(s)
    ans = 1
    for i in range(n):
        for j in range(i + 1, n + 1):
            t = s[i:j]
            if is_palindrome(t):
                ans = max(ans, j - i)
    print(ans)


if __name__ == "__main__":
    main()
