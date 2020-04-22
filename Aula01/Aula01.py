#Importando a biblioteca pandas
import pandas as pd

#Lendo os filmes do arquivo movies.csv
filmes = pd.read_csv('ml-latest-small/movies.csv')

#Exibe os primeiros itens dependendo do parâmetro, por default retorna 5
filmes.head()

#Lendo as avaliações do arquivo ratings.csv
avaliacoes = pd.read_csv('ml-latest-small/ratings.csv')

#Retorna o número de linhas e colunas do arquivo
avaliacoes.shape

#Retorna apenas o número de linhas
len(avaliacoes)

#Renomeando as colunas do Inglês para o Português (não é obrigatório fazer)
filmes.columns = ["filmeId", "titulo", "generos"]
avaliacoes.columns = ["usuarioID", "filmesId", "media", "momento"]

#Consultando valores passando paramêtros
avaliacoes_filme_1 = avaliacoes.query('filmesId == 1')

#Algumas informações referentes a base de dados como:
#quantidade, média, valores minimo e máximos, mediana entre outros
avaliacoes.describe()

#Saber a média da nota do filme um.
avaliacoes_filme_1['media'].mean()

#Recuperando apenas a média da coluna 'nota' de todos os filmes: 
notas_medias_por_filme = avaliacoes.groupby('filmesId')['media'].mean()

#Unindo o DataFrame filmes com as série média:
filmes_com_media = filmes.join(notas_medias_por_filme, on=['filmeId'])

#Ordenar filmes de acordo com sua média (os maiores em cima):
ordenacao_filmes_pela_media = filmes_com_media.sort_values('media', ascending=False)

#Realizando uma consulta de mais de um filme:
avaliacoes.query('filmesId in [1, 2, 102084]')

avaliacoes.query('filmesId == 1')['media'].plot(kind='hist', title='Avaliação do filme Toy Story')

avaliacoes.query('filmesId == 2')['media'].plot(kind='hist', title='Avaliação do filme Jumanji')

avaliacoes.query('filmesId == 102084')['media'].plot(kind='hist', title='Avaliação do filme Justice League: Doom')

#Desafio1
filmes_com_media['media'].isnull().sum()
filmes_sem_nota = filmes_com_media[filmes_com_media['media'].isnull()]

#Desafio2
filmes_com_media.rename(columns={"media":"nota_media"}, inplace=True)

#Desafio3
contador_notas_por_filme = avaliacoes.groupby('filmesId')["media"].count()
filmes_com_media = filmes_com_media.join(contador_notas_por_filme, on="filmeId")
filmes_com_media.rename(columns={"media":"quantidade_votos"}, inplace=True)
filmes_com_media.head()

#Desafio4
filmes_com_media = filmes_com_media.round({'nota_media':2})

#Desafio5
generos = filmes_com_media['generos']
generos = generos.str.split("|")
lista_generos = []
for g in generos:
    lista_generos.extend(g)
genero_com_repeticao = pd.DataFrame(lista_generos)
genero_com_repeticao.columns = ["genero"]
generos = genero_com_repeticao.drop_duplicates().reset_index().drop(['index'],axis=1)

#Desafio6
genero_qtd = genero_com_repeticao.stack().value_counts()

#Desafio7
genero_qtd.plot(kind="bar", title="Quantidade de filmes por gênero")
