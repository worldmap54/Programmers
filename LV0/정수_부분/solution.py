def solution(flo: float) -> int:
    """
    실수의 정수 부분을 반환하는 함수
    
    Args:
        flo (float): 변환할 실수 (0 ≤ flo ≤ 100)
        
    Returns:
        int: flo의 정수 부분
        
    Examples:
        >>> solution(1.42)
        1
        >>> solution(69.32)
        69
    """
    return int(flo)


def test_solution():
    """solution 함수의 테스트 케이스"""
    # 정상 케이스
    assert solution(1.42) == 1
    assert solution(69.32) == 69
    
    # 경계값 테스트
    assert solution(0.0) == 0
    assert solution(100.0) == 100
    
    # 소수점이 없는 경우
    assert solution(42.0) == 42
    
    print("모든 테스트 케이스 통과!")


if __name__ == "__main__":
    test_solution() 