from time import sleep

# Definição da Classe Filme
class Filme:
    def __init__(self, titulo, diretor, genero, anoLancamento):
        self.titulo = titulo
        self.diretor = diretor
        self.genero = genero
        self.ano_lancamento = anoLancamento

    def imprimirNomeFilme(self):
        return self.titulo

# Criação do Catálogo de Filmes
catalogoDeFilmes = { 
    
    #chave    classe e informações dos filmes       
    'Rocky': Filme('Rocky', 'John G. Avildsen', 'Drama', 1976),
    'Rocky II': Filme('Rocky II', 'Sylvester Stallone', 'Drama', 1979),
    'Rocky III': Filme('Rocky III', 'Sylvester Stallone', 'Drama', 1982),
    'Rocky IV': Filme('Rocky IV', 'Sylvester Stallone', 'Drama', 1985),
    'Rocky V': Filme('Rocky V', 'John G. Avildsen', 'Drama', 1990),
    'Rocky VI': Filme('Rocky Balboa', 'Sylvester Stallone', 'Drama', 2006),
    'Creed': Filme('Creed', 'Ryan Coogler', 'Drama', 2015),
    'Creed II': Filme('Creed II', 'Steven Caple Jr.', 'Drama', 2018),
}

# Função para adicionar filmes ao catálogo
def adicionarFilmes(catalogo):
    titulo = input('Informe o nome do filme que deseja adicionar: ')
    diretor = input('Informe o nome do diretor deste filme: ')
    genero = input('Informe o gênero deste filme que deseja incluir: ')
    anoLancamento = int(input('Informe em que ano este filme foi lançado: '))

    novoFilme = Filme(titulo, diretor, genero, anoLancamento)
    catalogo[titulo]  = novoFilme

# Função para visualizar catálogo de filmes
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
            print(f"Filme: {filme.titulo}")

# Função para atualizar informações de um filme no catálogo
def atualizarFilmes(catalogo, titulo):
    if titulo in catalogo:
        filme = catalogo[titulo]

        print(f'Informe as novas informações para o filme "{titulo}: ')
        novoTitulo = input('Informe o novo título deste filme: ')
        novoDiretor = input('Informe o novo diretor deste filme: ')
        novoGenero = input('Informe o novo gênero deste filme: ')
        novoAnoLancamento = int(input('Informe o novo ano de lançamento deste filme: '))

        # Atualiza as informações do filme no catálogo
        filme.titulo = novoTitulo
        filme.diretor = novoDiretor
        filme.genero = novoGenero
        filme.anoLancamento = novoAnoLancamento

        print(f'O filme "{titulo}" foi atualizado com sucesso ao Catalogo.')

    else:
        print(f'O filme "{titulo}" não consta na lista de filmes deste Catálogo. Obrigado!!')

# Função para remover filmes do catálogo
def removerFilme(catalogo, titulo):
    titulo = input('Informe o nome do filme que deseja remover: ')
    if titulo in catalogo:
        del catalogo[titulo]
        print(f'O filme "{titulo}" foi removido do catalogo com sucesso!!')

    else:
        print(f'O filme "{titulo}" não consta neste Catálogo de filmes. Obrigado!!')


# Chamando função de adicionar filmes

adicionarFilmes(catalogoDeFilmes)
sleep(2)
print('Aguarde, estamos adicionando o filme ao catálogo.')
sleep(1.5)
print('Filme adicionado com sucesso!')
sleep(2)

# Chamando a funçao de visualizar filmes
visualizarCatalogo(catalogoDeFilmes)

# Chamando a função de atualizar filmes
atualizarFilmes(catalogoDeFilmes, 'Rocky')
visualizarCatalogo(catalogoDeFilmes)

# Chamando a função remover filmes
removerFilme(catalogoDeFilmes, 'Rocky II')
print('Aguarde um momento, atualizando Catálogo...')
sleep(1.5)
print('Catálogo de Filmes Atualizado com Sucesso!!')
visualizarCatalogo(catalogoDeFilmes)

