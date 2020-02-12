"""
Decimal - "человеческие" десятичные дроби
"""
from decimal import Decimal

# Decimal позволяет вести точные расчёты, которые не полагаются на двоичную природу float
assert 3.3 + 4.1 != 7.4
assert Decimal('3.3') + Decimal('4.1') == Decimal('7.4')

# для Decimal можно настроить точность дробной части (в отличие от float)
from decimal import getcontext
# контекст содержит и позволяет изменять настройки вычислений в рамках всей программы
getcontext().prec = 2
print(Decimal(2) / Decimal(3))  # выведет 0.67

getcontext().prec = 20
print(Decimal(2) / Decimal(3))  # выведет 0.66666666666666666667


# округление
import decimal
d = Decimal('0.515')

print(d, 'quantized up is', d.quantize(Decimal('.11'), decimal.ROUND_UP))    # 1.52
print(d, 'quantized down is', d.quantize(Decimal('.11'), decimal.ROUND_DOWN))  # 1.51


#
# рациональные дроби
#
from fractions import Fraction
assert Fraction('3/4') == Fraction(6, 8)
