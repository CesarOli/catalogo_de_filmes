from filme import Filme
from time import sleep

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
def adicionaFilmes(titulo, diretor, genero, anoLancamento):
    filme = Filme(titulo, diretor, genero, anoLancamento)
    catalogoDeFilmes[titulo] = filme

adicionaFilmes('Space Jam', 'Joe Pytka', 'Animação/Comédia', '1996')
print(catalogoDeFilmes)

def criarFilme(catalogo, titulo, diretor, genero, anoLancamento):
    filmeNovo = { 
        'titulo': titulo,
        'diretor': diretor,
        'genero': genero,
        'anoLancamento': anoLancamento
    }
    catalogo[titulo] = filmeNovo
    sleep(3)
    print('Salvando o Filme no catálogo...')
    sleep(1.5)
    print('O filme novo foi adicionado com sucesso!!')
