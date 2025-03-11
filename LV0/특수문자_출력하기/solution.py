def solution() -> str:
    """
    특수문자를 출력하는 함수
    
    Returns:
        str: 특수문자 문자열
        
    Examples:
        >>> solution()
        '!@#$%^&*(\'"<>?:;'
    """
    return "!@#$%^&*(\'\"<>?:;"


def test_solution():
    """solution 함수의 테스트 케이스"""
    assert solution() == "!@#$%^&*(\'\"<>?:;"
    print("테스트 통과!")


if __name__ == "__main__":
    print(solution())
    test_solution() 