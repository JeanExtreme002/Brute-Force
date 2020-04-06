from src.app import App
import validator
import os


def try_password(password):

    """
    Função para mostrar a senha e verifica se ela é verdadeira.
    """

    if app.args.show == "true":
        print("\r Trying %s..." % password, end = "")

    return True if validator.main(app.args.command, password) == app.args.code else False


def err_callback(message = ""):

    """
    Função para imprimir erro e sair do programa.
    """

    print(" " + message)
    os._exit(1)


# Configurações do App.
description = "|Brute Force| by Jean Loui Bernard Silva de Jesus"
data_dir = "data"
key_to_stop = "q"

# Cria uma instância de App e obtém os argumentos passados na linha de comando.
app = App(try_password, err_callback, data_dir, description, key_to_stop)

# Mostra as informações que o usuário passou como argumento.
print("\n INFO:")
print(" -----------------------------------")
print(" Command:", app.args.command)
print(" Expected Exit Code:", app.args.code)
print(" Show:", app.args.show)
print(" Length:", app.args.min, "-", app.args.max)
print(" -----------------------------------")

print('\n Press "q" to finish.')

if app.args.show != "true": print(" Running...")

try:
    # Inicializa o Brute Force.
    app.run_brute_force()

except Exception as error:

    # Informa que houve um erro.
    print("\n\n Oops, it looks like there was an error during the process.")
    print(" Error:", error)

finally:

    # Obtém os dados do Brute Force e os imprime.
    pwd = app.bruteForce.found_password
    attempts = app.bruteForce.attempts

    print("\n -----------------------------------")
    print(" Password:", pwd if pwd else "Not Found")
    print(" Attempts:", attempts)
    print(" -----------------------------------")