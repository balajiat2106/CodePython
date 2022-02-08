def solution(A):
    c=max(filter(lambda a:(len(str(a))==2), A))
    return c

print(solution([-6, -91, 1011, -100, 84, -22, 0, 1, 473]))
