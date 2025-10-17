def solution(phone_book):
    phone_book.sort()
    for a, b in zip(phone_book, phone_book[1:]):
        if b.startswith(a):   # 인접 단 한 쌍만 체크
            return False
    return True