# from uteis import fatorial, dobro # Não é recomendado quando se usa muitos módulos (Incompatibilidade)
import uteis


num = int(input("Digite um valor: "))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {uteis.dobro(num)}')
