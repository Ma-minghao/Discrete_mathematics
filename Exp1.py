import unittest


# 从键盘输入命题常元的真值
p = input("请输入命题常元 p 的真值 (True 或 False): ").lower() == 'true'
q = input("请输入命题常元 q 的真值 (True 或 False): ").lower() == 'true'

# 计算逻辑运算
conjunction = p and q  # 合取
disjunction = p or q  # 析取
negation_p = not p  # 求非 p
negation_q = not q  # 求非 q
exclusive_or = p != q  # 异或
conditional = (not p) or q  # 单条件
biconditional = (p and q) or ((not p) and (not q))  # 双条件

# 输出结果
print(f"合取 (p ∧ q): {conjunction}")
print(f"析取 (p ∨ q): {disjunction}")
print(f"求非 p (¬p): {negation_p}")
print(f"求非 q (¬q): {negation_q}")
print(f"异或 (p ⊕ q): {exclusive_or}")
print(f"单条件 (p → q): {conditional}")
print(f"双条件 (p ↔ q): {biconditional}")
