import random
import time

students = []
number = 0

print("추첨을 해보아요오")



def print_list(i):
    global students
    print(f"{i+1}번 [ ", end = '')

    n = len(students[i])

    if n == 0:
        print("]")

    else:
        for j in range(n-1):
            print(f"{j+1}.{students[i][j]},", end = ' ')
        print(f"{n}.{students[i][-1]} ]")
    print()



n = 1
def input_list():
    global n
    try:
        if n == number + 1:
            return

        print()
        print(f"{n}번째 추첨")
        student = input("입력: ")

        if student == '':
            input_list()

        students[n-1] = list(student.split())
        print_list(n-1)
        n += 1
        input_list()

    except:
        input_list()


def input_num():
    try:
        global number, students
        n = int(input("추첨 횟수 입력: "))
        number = n
        students = [[] for _ in range(n)]
        input_list()
        draw_num()
        
        print()

    except:
        input_num()



def print_list_all():
    global students

    for i in range(len(students)):
        print(f"{i+1}번", end = ' ')

        for j in range(len(students[i])):
            print(f"{j+1}.", students[i][j], end = ' ')

        print()

    print()



def add_list(num):
    global students

    try:
        student = input("입력: ")

        if student == '':
            add_list(num)

        students[num] = students[num] + student.split()
        print_list(num)

    except:
        add_list(num)



def modify_num(num):
    try:
        mod_n = int(input("수정할 학생 번호 입력: "))

        if mod_n < 1 or mod_n > len(students[num]):
            modify_num(num)

        else:
            modify_list(num, mod_n)

    except:
        modify_num(num)


def modify_list(num, mod_n):
    try:
        mod = input("수정사항 입력: ")

        if mod == '':
            modify_list(num)

        students[num][mod_n-1] = mod
        print_list(num)

    except:
        modify_list(num, mod_n)



def remove_list(num):
    try:
        mod_n = int(input("삭제할 번호 입력: "))
        del students[num][mod_n - 1]
        
        print_list(num)

    except:
        remove_list(num)



def except_win(num, winner):
    global number

    for i in range(number):
        if i == num:
            pass
        else:
            if winner in students[i]:
                students[i].remove(winner)



def draw(num):
    winner = random.choice(students[num])

    print()
    print()
    print(f"           {num+1}번 추첨을 시작합니다")
    time.sleep(1)
    for _ in range(10):
        print()
        time.sleep(0.1)
    for _ in range(3):
        print("                      두구")
        time.sleep(0.3)
    print()
    print()
    print("                 과연.", end = '')
    for _ in range(6):
        print(".", end = '')
        time.sleep(0.3)
    print()
    print()
    time.sleep(0.3)
    print("                 당첨자는...")
    time.sleep(0.4)
    for _ in range(10):
        print()
        time.sleep(0.1)
    time.sleep(0.2)
    print(f"            ---->  {winner} !!!! <----")
    time.sleep(0.3)
    for _ in range(5):
        print()
    time.sleep(0.3)
    print("                 축하합니다~!")
    time.sleep(0.3)
    for _ in range(2):
        print()

    except_win(num, winner)


def draw_num():
    try:
        print()
        print_list_all()
    
        num = int(input("편집할 추첨 번호 입력: "))

        if num < 1 or num > len(students):
            draw_num()
        num = num-1

        edit(num)

    except:
        draw_num()



def edit(num):
    try:    
        print("추가하려면 1, 수정하려면 2, 삭제하려면 3, 추첨을 시작하려면 4 입력")
        chk_n = int(input())

        if chk_n == 1:
            add_list(num)
            draw_num()

        elif chk_n == 2:
            modify_num(num)
            draw_num()

        elif chk_n == 3:
            remove_list(num)
            draw_num()

        elif chk_n == 4:
            draw(num)
            draw_num()

        else:
            draw_num()

    except:
        edit(num)
        


# main ------------------------------------------------------

input_num()