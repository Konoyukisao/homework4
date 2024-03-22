immutable_var = (123, True, '123', 1.23)
print(immutable_var)
#immutable_var[0] = 12 - Невозможно изменить элемент потому как, тип "tuple" не поддерживает изменение элементов.
mutable_list = [123, True, '123', 1.23]
mutable_list[0] = mutable_list[3]; mutable_list[3] = 123
print(mutable_list)
