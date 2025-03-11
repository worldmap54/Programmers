def solution(a: int, b: int) -> str:
    """
    두 정수의 덧셈식을 문자열로 반환하는 함수
    
    Args:
        a (int): 첫 번째 정수 (1 ≤ a ≤ 100)
        b (int): 두 번째 정수 (1 ≤ b ≤ 100)
        
    Returns:
        str: "a + b = c" 형태의 덧셈식
        
    Examples:
        >>> solution(4, 5)
        '4 + 5 = 9'
    """
    return f"{a} + {b} = {a + b}"


def test_solution():
    """solution 함수의 테스트 케이스"""
    # 정상 케이스
    assert solution(4, 5) == "4 + 5 = 9"
    
    # 경계값 테스트
    assert solution(1, 1) == "1 + 1 = 2"
    assert solution(100, 100) == "100 + 100 = 200"
    
    # 추가 테스트
    assert solution(10, 20) == "10 + 20 = 30"
    
    print("모든 테스트 케이스 통과!")


if __name__ == "__main__":
    # 입력 받기
    a, b = map(int, input().split())
    print(solution(a, b)) 