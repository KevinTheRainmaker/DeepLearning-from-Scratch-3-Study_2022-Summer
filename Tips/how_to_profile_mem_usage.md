> pip install memory_profiler

위 커맨드를 터미널에서 실행시켜서 memory_profiler 패키지를 install 한다.

이후 아래와 같이 사용하면 된다.

```python
from memory_profiler import profile

@profile
def function():
    ...
```

더 자세한 사용법은 <a href='https://data-newbie.tistory.com/701'>링크</a>를 참조하자.
