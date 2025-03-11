def solution(s: str) -> str:
    """
    문자열의 대소문자를 변환하여 반환하는 함수
    
    Args:
        s (str): 변환할 문자열 (1 ≤ len(s) ≤ 20)
        
    Returns:
        str: 대소문자가 변환된 문자열
        
    Examples:
        >>> solution('aBcDeFg')
        'AbCdEfG'
    """
    
    return s.swapcase()


def test_solution():
    """solution 함수의 테스트 케이스"""
    # 정상 케이스
    assert solution('aBcDeFg') == 'AbCdEfG'
    
    # 경계값 테스트
    assert solution('a') == 'A'
    assert solution('Z') == 'z'
    
    # 추가 테스트
    assert solution('HelloWorld') == 'hELLOwORLD'
    
    print("모든 테스트 케이스 통과!")


if __name__ == "__main__":
    # 입력 받기
    s = input().strip()
    print(solution(s)) 