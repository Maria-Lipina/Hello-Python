# TODO: распределить их потом корректнее по файлам: main, controller, view, tN
# TODO: мне нужен метод вроде request? Задача просит view показать пользователю инструкцию, какие именно данные от него нужны. Контроллер проверяет полученные входные данные на корректность. Но если проверять ввод на корректность, то так же нужно добавлять сюда обработку исключений

import view as v

def run (task):
     code_f = open(f't{task}.py', 'r')
     code_str = f'{code_f.read()}\nv.show_res(do())\n'
     code_f.close()
     code = compile(code_str, f't{task}.py', 'exec')
     exec(code)

t = v.menu()
v.t_text(t)
run(t)

