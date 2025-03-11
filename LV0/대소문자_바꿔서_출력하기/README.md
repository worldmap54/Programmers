# 대소문자 바꿔서 출력하기

## 문제 설명
영어 알파벳으로 이루어진 문자열 str이 주어집니다. 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.

## 제한사항
- 1 ≤ str의 길이 ≤ 20
- str은 알파벳으로 이루어진 문자열입니다.

## 입출력 예
```
입력 #1
aBcDeFg

출력 #1
AbCdEfG
```

## 알고리즘 순서도
```mermaid
graph LR
    A[시작] --> B[문자열 입력]
    B --> C[대소문자 변환]
    C --> D[출력]
    D --> E[종료]
```

## 실행 방법
```bash
python solution.py
```

## 테스트 방법
```python
def test_solution():
    assert solution('aBcDeFg') == 'AbCdEfG'
    assert solution('a') == 'A'
    assert solution('Z') == 'z'
```

## 성능 분석
- 시간 복잡도: O(n)
- 공간 복잡도: O(n)

## 개선 사항
- 현재 구현이 최적화되어 있어 추가 개선이 필요하지 않음
- swapcase() 메서드를 사용하여 간결한 코드 작성 