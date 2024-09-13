# hello.py
def saudacao():
    print("Olá, seja bem-vindo ao projeto de Python!")

if __name__ == "__main__":
    saudacao()
# hello.py
def saudacao():
    print("Olá, seja bem-vindo ao projeto de Python!")

def nova_funcionalidade():
    print("Esta é uma nova funcionalidade adicionada!")

if __name__ == "__main__":
    saudacao()
    nova_funcionalidade()
git add hello.py
git commit -m "Adiciona nova funcionalidade ao projeto"
git push origin nova-funcionalidade
# hello.py
def saudacao():
    print("Olá, seja bem-vindo ao projeto de Python!")

def nova_funcionalidade():
    print("Esta é uma nova funcionalidade adicionada para testar o CI e CD!")

if __name__ == "__main__":
    saudacao()
    nova_funcionalidade()
git add hello.py
git commit -m "Adiciona nova funcionalidade e configura workflows para CI e CD"
git push origin nova-feature
