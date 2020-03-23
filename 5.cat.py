# $ man cat을 통해 
# cat 명령어에 대해 알아보자

# $ cat a.txt
# a.txt 파일의 내용을 출력한다

# $ cat a.txt b.txt c.txt
# a.txt + b.txt + c.txt의 내용을 출력한다

# $ cat a.txt b.txt > c.txt
# c.txt에 a.txt + b.txt를 입력한다

# 이제부터 45분간 파이썬으로 위의 기능을 구현하자

import argparse


