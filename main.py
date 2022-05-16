# TODO: распределить их потом корректнее по файлам: main, controller, view, tN
# TODO: мне нужен метод вроде request? Задача просит view показать пользователю инструкцию, какие именно данные от него нужны. Контроллер проверяет полученные входные данные на корректность. Но если проверять ввод на корректность, то так же нужно добавлять сюда обработку исключений
# TODO: следующая подзадача: добавить аргумент-селектор для запуска задачи и связать с view
import view as v

task = v.menu()
v.t_text(task)
def foo ():
     code_f = open('t1.py', 'r')
     code_str = code_f.read()
     code_f.close()
     code = compile(code_str, 't1.py', 'exec') #сюда можно прикрутить портируемость (чтобы, скажем, t1 можно было бы успешно импортировать в другой файл как функцию и выполнить только там, а не в t1 и месте назначения
     exec(code)

foo() #10000000 loops, best of 5: 28.5 nsec per loop

import runpy
def foo1():
     runpy.run_module(mod_name='t1') #легче и проще, быстрее (скорее всего) но портируемость (я вообще правильно употребляю термин?) не прикрутишь

foo1() #10000000 loops, best of 5: 26.6 nsec per loop

import importlib
def foo2():
  importlib.import_module('t1')

foo2() #10000000 loops, best of 5: 26.6 nsec per loop
