### nametuple ###

# 책의 제목과 가격을 저장하는 Book 클래스 생성 후 객체 생성


class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price


mybook = Book("파이썬을 이용한 비트코인 자동매매", 27000)
print(mybook.title, mybook.price)

# 단순 튜플 이용
mybook2 = ("파이썬을 이용한 비트코인 자동매매", 27000)
print(mybook2[0], mybook2[1])

# nametuple을 사용하여 객체 생성
from collections import namedtuple

Book = namedtuple("Book", ["title", "price"])
mybook3 = Book("파이썬을 이용한 비트코인 자동매매", 27000)
print(f"title = {mybook3.title}, price = {mybook3.price}")

# namedtuple을 통해 생성한 객체는 결국 튜플처럼 immutable하기 때문에 클래스와 달리 값을 수정 불가
# 그리고 튜플처럼 정수 값을 통해서 인덱싱할 수 있음

print(f"title = {mybook3[0]}, price = {mybook3[1]}")  # indexing
# mybook3.price = 25000  # AttributeError


### tuple unpacking ###
def print_book(title, price):
    print(title, price)


print_book(*mybook3)
