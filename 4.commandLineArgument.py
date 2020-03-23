# 커맨드 라인을 처리하는 두가지 작은 파이썬 스크립트 작성
# 1. 전통적인 방식인 sys.argv를 사용해 처리
# 2. 파이썬의 argparse 패키지를 사용한다. 좀 더 깔끔한 argument 처리 가능

# 테스트 스크립트의 조건
# 1. --help, -h argument를 이용해 도움말을 얻는다
# 2. 최소 세 개의 arguemnt를 플래그로 받는다. 플래그는 다른 argument를 추가적으로 필요하지 않아 커맨드라인에 이 플래그가 보이면 변수를 on시킨다
# 3. 옵션인 아규먼트를 최소 세 개를 처리한다. 옵션은 별도의 argument를 가진다. 여러분이 작성하는 스크립트에는 옵션에 주어진 값으로 변수를 설정한다.
# 4. 추가적으로 포지셔널 argument를 처리한다. 이 argument는 -로 시작하는 아규먼트 위에 와서 파일 목록들을 받을 수 있다. 그리고 이때 *.txt처럼 터미널 와일드카드를 처리할 수 있다.

# 이번 연습의 목표 : 프로젝트를 시작하는 나만의 방식을 알아보자

# 1. 구글링을 통해 자료 조사
# 2. 해체와 재조합을 통한 새로운 코드 창조

# sys.argv에 대한 이해
# https://www.pythonforbeginners.com/system/python-sys-argv
# import sys

# print("This is the name of the script: ", sys.argv[0])
# print("Number of arguments: ", len(sys.argv))
# print("The arguments are: " , str(sys.argv))

# sys.argv에 대한 심화
# https://www.tutorialspoint.com/python3/python_command_line_arguments.htm
# import sys, getopt

# def main(argv):
#    inputfile = ''
#    outputfile = ''
#    try:
#       opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
#    except getopt.GetoptError:
#       print ('test.py -i <inputfile> -o <outputfile>')
#       sys.exit(2)
#    for opt, arg in opts:
#       # 1. --help, -h argument를 이용해 도움말을 얻는다
#       # 3. 옵션인 아규먼트를 최소 세 개를 처리한다. 옵션은 별도의 argument를 가진다. 여러분이 작성하는 스크립트에는 옵션에 주어진 값으로 변수를 설정한다.
#       if opt == '-h':
#          print ('test.py -i <inputfile> -o <outputfile>')
#          sys.exit()
#       elif opt in ("-i", "--ifile"):
#          inputfile = arg
#       elif opt in ("-o", "--ofile"):
#          outputfile = arg
#    print ('Input file is "', inputfile)
#    print ('Output file is "', outputfile)

# if __name__ == "__main__":
#    main(sys.argv[1:])

# sys.argv가 어렵고, 진행하기 위한 문서가 부족한 상황
# argparse를 사용한다
# argparse에 대한 이해
# import argparse

# parser = argparse.ArgumentParser(prog='4.commandLineArgument.py', add_help=False)
# # 1. --help, -h argument를 이용해 도움말을 얻는다
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')
# parser.add_argument('--version', action='version', version='%(prog)s 2.0',
#                     help='version of this program')
# parser.add_argument('--count', '-c', action='count', default=0, help='count arguments')
# # parser.print_help()
# args = parser.parse_args()
# print(parser.print_help())
#print(args.accumulate(args.integers))


# 첫번째 45분을 다 썼지만 완성하지 못했다
# 실패한 이유는 sys.argv와 argparse에 대한 자료 수집 없이
# 바로 코드를 짜는 시간을 거쳐 그런 것으로 예상된다.
# 다음부턴 자료 수집을 통해 내가 사용할 수 있는 라이브러리를 확인해서 접근하자

# 해설
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('integers', metavar='N', type=int, nargs='+')
parser.add_argument('-f', '--foo', help='foo help')
parser.add_argument('-b', '--bar', help='bar help')
parser.add_argument('-z', '--baz', help='baz help')
parser.add_argument('-t', '--turn-on', action='store_true')
parser.add_argument('-x', '--exclude', action='store_false')
parser.add_argument('-s', '--start', action='store_true')
args = parser.parse_args()

print(args)