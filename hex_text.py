# diegoHERNANDO 2023

hex_str = input("Introduce HEX:\n")
s = hex_str.replace(" ", "")
# loop para convertir HEX a INT y asignarle su valor ASCII 
texto = ''.join([chr(int(s[i:i+2], 16)) for i in range(0, len(s), 2)])
print('\n' + texto + '\n')
