# 전민성
# https://school.programmers.co.kr/learn/courses/30/lessons/92335
# k진수에서 소수 개수 구하기
def solution(n, k):
    def prime(number):
        if number <= 1:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True
    answer = 0
    change = ""
    mul = 1
    while n>0:
        change=str(n%k)+change
        n=n//k
    potential_primes = change.split("0")
    for case in potential_primes:
        if case == "":
            continue
        elif prime(int(case)):
            answer+=1
    return answer if answer!=-1 else answer