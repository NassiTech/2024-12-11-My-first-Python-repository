# how does a permutation function work!
# perm(abc) = a+PERM(bc), b+PERM(ac), c+PERM(ab) = a+b+PERM(c), a+c+PERM(b), .....


def permutation(s):
    if len(s) == 1:
        return [s]
    perms = []
    for i in range(len(s)):
        for p in permutation(s[:i] + s[i + 1 :]):
            perms.append(s[i] + p)
    return perms


# Beispiel
print(permutation("CBA"))  # Ausgabe: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
