# Библиотека загружена отсюда: https://pypi.org/project/equation-solver/#description

from equation import quadratic_equation as qe
roots = qe.QuadraticEquation(5, 3, -1) #<equation.quadratic_equation.QuadraticEquation object at 0x000001DABB237D60> - почему не поддается конвертации в число?
print(roots)
