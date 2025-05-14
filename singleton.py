class Singleton:
    _instance = None
    # __new__ 是在物件「還沒被建立」時呼叫的方法
    # 第一次建立時，呼叫父類別的 __new__ 來分配記憶體
    # override父類別的__new__
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        # 在第一次初始化時設定屬性
        # hasattr(obj, name) 是 Python 的內建函式，用來判斷物件 obj 是否擁有屬性（attribute）name。
        if not hasattr(self, "_initialized"):
            self.value = value
            self._initialized = True

# 測試
s1 = Singleton(10)
s2 = Singleton(20)
print(s1 is s2)       # True
print(s1.value, s2.value)  # 10 10

#補充
#在 Python 中，* 並不是「指標」的意思，而是一種「打散（unpacking）」或「收集（packing）」引數的語法糖；而 __new__ 則是在物件「還沒被建立」時呼叫的方法。以下分別說明：
#* 的用法
#在函式定義時：收集多餘的定位引數
def foo(a, *args, **kwargs):
    print(a)        # 第一個定位引數
    print(args)     # 其餘所有定位引數會被打包成 tuple
    print(kwargs)   # 所有關鍵字引數會被打包成 dict

foo(1, 2, 3, x=10, y=20)
# 輸出：
#   1
#   (2, 3)
#   {'x': 10, 'y': 20}

#在函式呼叫時：打散序列／映射到參數
def bar(x, y, z):
    print(x, y, z)

nums = [1, 2, 3]
bar(*nums)        # 等同於 bar(1, 2, 3)

opts = {'x': 4, 'y': 5, 'z': 6}
bar(**opts)       # 等同於 bar(x=4, y=5, z=6)
#*nums 會把 nums 中的每個元素依序對應到 bar 的定位參數
#**opts 則把字典的鍵值對映射到對應的參數
#重點：* 與 C/C++ 的指標（pointer）沒有任何關聯，它只是用來操作函式引數的「打包／打散」機制。


