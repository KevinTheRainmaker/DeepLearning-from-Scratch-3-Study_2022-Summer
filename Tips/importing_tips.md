## 다른 주피터 노트북을 import 해서 사용하는 법

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