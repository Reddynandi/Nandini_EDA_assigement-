Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name='naveen'
>>> name+bhanu
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    name+bhanu
NameError: name 'bhanu' is not defined
>>> name='bhanu'
>>> name+'navi'
'bhanunavi'
>>> 5*name+navi
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    5*name+navi
NameError: name 'navi' is not defined
>>> 5*name+'navi'
'bhanubhanubhanubhanubhanunavi'
>>> _+'nagini'
'bhanubhanubhanubhanubhanunavinagini'
>>> 2*3
6
>>> 2**3
8
>>> 2//3
0
>>> 2/3
0.6666666666666666
>>> name=("bhanu\nnavi")
>>> print("name")
name
>>> bhanu\nnavi
SyntaxError: unexpected character after line continuation character
>>> name=('bhanu','navi')
>>> name
('bhanu', 'navi')
>>> values=(8.2,'bhanu',4)
>>> values
(8.2, 'bhanu', 4)
>>> mil=(name,values)
>>> mil
(('bhanu', 'navi'), (8.2, 'bhanu', 4))
>>> vinnu=(name,values)
>>> vinnu
(('bhanu', 'navi'), (8.2, 'bhanu', 4))
>>> nums=[2,32,54,65,67,68]
>>> nums
[2, 32, 54, 65, 67, 68]
>>> nums.append(45)
>>> nums.append(67)
>>> nums
[2, 32, 54, 65, 67, 68, 45, 67]
>>> nums.insert(22,24)
>>> nums
[2, 32, 54, 65, 67, 68, 45, 67, 24]
>>> nums.delete(67)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    nums.delete(67)
AttributeError: 'list' object has no attribute 'delete'
>>> nums.remove(67)
>>> nums
[2, 32, 54, 65, 68, 45, 67, 24]
>>> nums.pop(32)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    nums.pop(32)
IndexError: pop index out of range
>>> nums.pop(2)
54
>>> nums
[2, 32, 65, 68, 45, 67, 24]
>>> nums.pop(1,2)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    nums.pop(1,2)
TypeError: pop expected at most 1 argument, got 2
>>> nums.pop()
24
>>> del nums(4:)
SyntaxError: invalid syntax
>>> del nums (4: )
SyntaxError: invalid syntax
>>> del nums(4;)
SyntaxError: invalid syntax
>>> del nums[4:]
>>> nums
[2, 32, 65, 68]
>>> del nums[:2]
>>> nums
[65, 68]
>>> nums.extend[25,34,56]
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    nums.extend[25,34,56]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> nums.extend([23,24,34,45])
>>> nums
[65, 68, 23, 24, 34, 45]
>>> min(nums)
23
>>> max(nums)
68
>>> sum(nums)
259
>>> nums.sort()
>>> nums
[23, 24, 34, 45, 65, 68]
>>> 