#  tuples --->
immutable_var = 12, "string", 1.325, 'f', -1, False
#  вывод кортежа:
print(immutable_var)
#  вывод результата сложения кортежа:
print(immutable_var + immutable_var)
#  вывод результата умножения кортежа:
print(immutable_var * 3)
#  ниже - попытка изменить значение элемента кортежа.
#  Pycharm уже при вводе предупреждает, что это недопустимая операция
#  при выполнении - выдаёт ошибку. Поэтому строку закомментарил.
#  immutable_var[0] = 10
#  <--- tuples
#  lists --->
mutable_list = [10.5, "new_string", 13, 'A', -500, True]
#  вывод списка:
print(mutable_list)
#  меняем элементы списка:
mutable_list[1] = 'new_new_string'
mutable_list[-1] = False
#  добавляем элементы к списку:
mutable_list.append("dop_element")
mutable_list.extend(["dop2_element"])
#  удаляем элемент из списка:
mutable_list.remove(10.5)
#  вывод изменённого списка:
print(mutable_list)
#  <--- lists

