## 다른 주피터 노트북을 import 해서 사용하는 법

작성자: 김동우

셀에 아래와 같이 작성하면 다른 노트북을 셀에서 실행하고, 결과를 받을 수 있다.
%run NotebookName.ipynb

클래스나 함수를 가져오는 방법은 아래와 같다.

1. 터미널에서 import_ipynb 설치
   pip install import_ipynb

2. 셀에 해당 모듈을 import 해 옴.
   import import_ipynb

3. Codes 라는 폴더 내에 step11.ipynb의 Variable 클래스를 사용하고 싶다면?
   from Codes.step11 import Variable
   의 형식으로 가져올 수 있다!!

ref: https://stackoverflow.com/questions/20186344/importing-an-ipynb-file-from-another-ipynb-file

## 다른 파이썬 파일을 사용하는 법

작성자: 고강빈

위 방식을 파이썬 파일에서 하는 방법은 더욱 간단하다.

그냥 `from 파이썬_파일이름 import 원하는_함수(또는 *)`을 최상단에 삽입하면 된다!

해당 파이썬 파일 내 함수는 물론 클래스, 외부 라이브러리까지 모두 불러올 수 있다.

단, 실행부분은 `if __name__=='__main__'`과 같은 식으로 작성해서 이전 파일의 출력이 중첩되지 않도록 하자.
