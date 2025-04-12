def check_vowels():
    # Código a implementar utilizando input.
    name = input('Ingrese aquí el nombre: ')
    name = name.lower()
    print('Contiene a: ' + str('a' in name))
    print('Contiene e: ' + str('e' in name))
    print('Contiene i: ' + str('i' in name))
    print('Contiene o: ' + str('o' in name))
    print('Contiene u: ' + str('u' in name))

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
