from time import sleep

class Filme:
    def __init__(self, titulo, diretor, genero, ano_lancamento):
        self.titulo = titulo
        self.diretor = diretor
        self.genero = genero
        self.ano_lancamento = ano_lancamento

    def imprimirNomeFilme(self):
        return self.titulo

catalogoDeFilmes = { 
    
    #chave    classe e informações dos filmes       
    'filme1': Filme('Rocky', 'John G. Avildsen', 'Drama', 1976),
    'filme2': Filme('Rocky II', 'Sylvester Stallone', 'Drama', 1979),
    'filme3': Filme('Rocky III', 'Sylvester Stallone', 'Drama', 1982),
    'filme4': Filme('Rocky IV', 'Sylvester Stallone', 'Drama', 1985),
    'filme5': Filme('Rocky V', 'John G. Avildsen', 'Drama', 1990),
    'filme6': Filme('Rocky Balboa', 'Sylvester Stallone', 'Drama', 2006),
    'filme7': Filme('Creed', 'Ryan Coogler', 'Drama', 2015),
    'filme8': Filme('Creed II', 'Steven Caple Jr.', 'Drama', 2018),
}

def adicionarFilmes(catalogo):
    titulo = input('Informe o nome do filme que deseja adicionar: ')
    diretor = input('Informe o nome do diretor deste filme: ')
    genero = input('Informe o gênero deste filme que deseja incluir: ')
    ano_lancamento = int(input('Informe em que ano este filme foi lançado: '))

    novoFilme = Filme(titulo, diretor, genero, ano_lancamento)
    catalogo[titulo]  = novoFilme

adicionarFilmes(catalogoDeFilmes)
sleep(2)

'''def editarFilmes(catalogo, titulo):
    if:
    else:

def removerFilme(catalogo, titulo):
    if
        del
    else:


def menu()):
    print()
    print()
    print()
    print()
    print()
    print()
    
    return

while True:

    if:
    elif:
    elif:
    elif:
    elif:
    else:'''