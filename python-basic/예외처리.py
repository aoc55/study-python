from typing import Any


# Custom 예외선언 1
class MyCustomException(Exception):
    pass


# Custom 예외선언2
class MyCustomNumberException(Exception):     # Exception 을 상속
    def __init__(self, value: Any) -> None:
        self.value = value
        super().__init__(f'My Cusotm Exception => {value}')     # Super 호출

    def get_value(self) -> Any:
        return self.value





# 예외처리
if __name__ == '__main__':
    try:
        if True:
            raise MyCustomNumberException('Test')       # 예외 발생 (raise)
    except MyCustomNumberException as ex:
        print(f'Except MyCustomNumberException =>{ex.get_value()}')
    else:
        print('Else 실행 ~')  # 실행안됨
    finally:
        print('Finally 실행 ~')