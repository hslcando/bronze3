# -*- coding: utf-8 -*-
"""럭비클럽24-02-21_이현지_.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UOhraYU5BbY4o4gPiC_IyCq7HUThcJXr
"""

while True: # 백준은,, 입력값을 연속으로 받나보다^^;;
    member = input().split() # 입력값 리스트 형태로 출력됨 -> ['Joe', '16', '34']
    name = member[0] # member의 0번째는 문자형 데이터 -> name 변수에 할당
    age = int(member[1]) # member의 1번째는 정수형 데이터 -> age 변수에 할당
    kg = int(member[2]) # member의 2번째는 정수형 데이터 -> kg 변수에 할당

    # 이름 조건 (알파벳 대소문자로 이루어져있으며, 길이 10을 넘기면 안됨)
    if (name.isalpha()) & (len(name)<=10): # isalpha() -> 알파벳으로 이루어져있는지 알 수 있는 함수
        if (age>17) | (kg>=80): # 성인부 조건
            print(name, 'Senior')
        else:
            print(name, 'Junior')
    else:
        break

