def solution(phone_book):
    answer = True
    phone_book.sort()
    for n in range(0,len(phone_book)-1):
            if phone_book[n+1].startswith(phone_book[n]):
                answer = False
                break
    return answer
