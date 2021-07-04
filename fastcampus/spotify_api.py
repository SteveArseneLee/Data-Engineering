import sys

def main():
    print('fastcampus')
    
if __name__=='__main__':
    main()
else: # 현 파일이 직접 실행이 안되고 어떤 모듈 패키지화되서 import되면 출력
    print('this script is being imported')