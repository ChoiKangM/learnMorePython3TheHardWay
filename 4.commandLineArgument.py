# 파이썬이 스크립트를 처리하는 방식을 공부하자
# 1.sys.argv 이용
# 2.argparse 패키지 이용

# 코드 제작 프로세스
# 1. 구글링 - 남이 만들어둔 자료가 없으면 아무것도 못한다
# 2. python 라이브러리의 -help를 이용? - 한번도 해본적 없다

# 결과
# 구글링의 경우 인터넷이 안되거나 남이 만들어둔 자료가 없으면
# 아무것도 하지 못한다
# python 라이브러리의 help 함수를 이용해 확인하였지만 빈약하였다
# Module Reference는 docs.python.org의 라이브러리 문서가 원본이므로
# 인터넷에서 찾는게 나쁘지 않다는 결과를 보여줌

# 아래의 예시 코드는 구글링 후 제작하여
# 온전히 내 머리에서 나왔다고 할 수 없음

import sys
print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: " , str(sys.argv))

print("============================================")
import argparse
print("This is the name of the script: ", argparse.ArgumentParser.parse_args)
