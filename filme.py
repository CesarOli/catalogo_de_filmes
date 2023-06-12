from time import sleep

class Filme:
    def __init__(self, titulo, diretor, genero, anoLancamento):
        self.titulo = titulo
        self.diretor = diretor
        self.genero = genero
        self.ano_lancamento = anoLancamento

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

'''def adicionarFilmes(catalogo):
    titulo = input('Informe o nome do filme que deseja adicionar: ')
    diretor = input('Informe o nome do diretor deste filme: ')
    genero = input('Informe o gênero deste filme que deseja incluir: ')
    anoLancamento = int(input('Informe em que ano este filme foi lançado: '))

    novoFilme = Filme(titulo, diretor, genero, anoLancamento)
    catalogo[titulo]  = novoFilme

adicionarFilmes(catalogoDeFilmes)
sleep(2)

print('Aguarde, estamos adicionando o filme ao catálogo.')
sleep(1.5)
print('Filme adicionado com sucesso!')
sleep(2)
print('Catálogo de Filmes: ')

for chave, filme in catalogoDeFilmes.items():
    sleep(0.5)
    print(filme.titulo)


def visualizarCatalogo(catalogo):
    print('------------------')
    print('CATÁLOGO DE FILMES')
    print('------------------')

    if len(catalogo) == 0:
        print('Nenhum filme encontrado neste catálogo.')
    else:
        for chave in catalogo:
            filme = catalogo[chave]
            sleep(0.5)
            print(f"Filme: {filme.titulo}")'''


def atualizarFilmes(catalogo, titulo):
    if titulo in catalogo:
        filme = catalogo[titulo]

        print(f'Informe as novas informações para o filme "{titulo}: ')
        novoTitulo = input('Informe o novo título deste filme: ')
        novoDiretor = input('Informe o novo diretor deste filme: ')
        novoGenero = input('Informe o novo gênero deste filme: ')
        novoAnoLancamento = int(input('Informe o novo ano de lançamento deste filme: '))

        #atualiza as informações do filme no catálogo
        filme.titulo = novoTitulo
        filme.diretor = novoDiretor
        filme.genero = novoGenero
        filme.anoLancamento = novoAnoLancamento

        print(f'O filme "{titulo}" foi atualizado com sucesso ao Catalogo.')

    else:
        print(f'O filme "{titulo}" não consta na lista de filmes deste Catálogo. Obrigado!!')

'''def removerFilme(catalogo, titulo):
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
    else:
        
        
visualizarCatalogo(catalogoDeFilmes)'''
atualizarFilmes(catalogoDeFilmes, 'filme1')


