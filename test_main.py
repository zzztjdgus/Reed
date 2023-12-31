# test_example.py

# 테스트 대상이 되는 함수입니다.
def add(a: int, b: int) -> int:
    return a + b

# add 함수에 대한 테스트 코드로 남게 된다.
def test_add():
    assert add(1, 1) == 2, "통과가 아닌데요?"  # add(1, 1)의 출력이 2면 테스트를 통과합니다.

def create_token(user_id: str) -> str:
    return user_id + "_verified"

def test_create_token():
    actual = create_token("grab")
    expected = "grab_verified"
    assert actual == expected

