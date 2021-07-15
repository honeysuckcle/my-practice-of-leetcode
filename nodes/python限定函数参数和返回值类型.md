本文内容从下面的网址中复制

[python限定方法参数类型、返回值类型、变量类型等](https://www.cnblogs.com/linkenpark/p/11676297.html)

## typing模块的作用

自python3.5开始，PEP484为python引入了类型注解(type hints)

- 类型检查，防止运行时出现参数和返回值类型、变量类型不符合。
- 作为开发文档附加说明，方便使用者调用时传入和返回参数类型。
- 该模块加入后并不会影响程序的运行，不会报正式的错误，只有提醒pycharm目前支持typing检查，参数类型错误会黄色提示

**官网typing详细说明**
[typing类型标注](https://docs.python.org/zh-cn/3/library/typing.html#module-typing)

## 常用类型

- int,long,float: 整型,长整形,浮点型
- bool,str: 布尔型，字符串类型
- List, Tuple, Dict, Set:列表，元组，字典, 集合
- Iterable,Iterator:可迭代类型，迭代器类型
- Generator：生成器类型

## 基本类型指定

- 示例

```python
def test(a:int, b:str) -> str:
    print(a, b)
    return 1000

if __name__ == '__main__':
    test('test', 'abc')
函数test，
a:int  指定了输入参数a为int类型，
b:str  b为str类型，
-> str  返回值为srt类型。

可以看到，
在方法中，我们最终返回了一个int，此时pycharm就会有警告；
当我们在调用这个方法时，参数a我们输入的是字符串，此时也会有警告；
但非常重要的一点是，pycharm只是提出了警告，但实际上运行是不会报错，毕竟python的本质还是动态语言
```

## 复杂的类型标注

- 示例1

```python
from typing import List
Vector = List[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

# typechecks; a list of floats qualifies as a Vector.
new_vector = scale(2.0, [1.0, -4.2, 5.4])
```

- 示例2

```python
from typing import Dict, Tuple, Sequence

ConnectionOptions = Dict[str, str]
Address = Tuple[str, int]
Server = Tuple[Address, ConnectionOptions]

def broadcast_message(message: str, servers: Sequence[Server]) -> None:
    ...

# The static type checker will treat the previous type signature as
# being exactly equivalent to this one.
def broadcast_message(
    message: str,
    servers: Sequence[Tuple[Tuple[str, int], Dict[str, str]]]) -> None:
    ...
):
    ...
这里需要注意，元组这个类型是比较特殊的，因为它是不可变的。
所以，当我们指定Tuple[str, str]时，就只能传入长度为2，
并且元组中的所有元素都是str类型
```

## 泛型指定

- 示例

```python
from typing import Sequence, TypeVar, Union

T = TypeVar('T')      # Declare type variable

def first(l: Sequence[T]) -> T:   # Generic function
    return l[0]

T = TypeVar('T')  # Can be anything
A = TypeVar('A', str, bytes)  # Must be str or bytes
A = Union[str, None] # Must be str or None
```

## 创建变量时的类型指定

```python
from typing import NamedTuple

class Employee(NamedTuple):
    name: str
    id: int = 3

employee = Employee('Guido')
assert employee.id == 3
```

## 不足之处

- 示例

```python
from typing import List

def test(b: List[int]) -> str:
    print(b)
    return 'test'


if __name__ == '__main__':
    test([1, 'a'])
从这个例子可以看出来，虽然我们指定了List[int]即由int组成的列表，
但是，实际中，只要这个列表中存在nt（其他的可以为任何类型），就不会出现警告
```