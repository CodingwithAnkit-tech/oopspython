from abc import ABC, abstractmethod


class clg(ABC):

    @abstractmethod
    def msg():
        pass

    @abstractmethod
    def msg1():
        pass


class demo(clg):

    def msg():
        print("go to qspiders")

    def msg1():
        print("go to deepak sir...")


ob = demo()
print(demo.msg())