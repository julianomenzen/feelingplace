from configparser import ConfigParser
import psycopg2 

 
def config(filename='conexaodb.cfg', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
 
    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return db

def testarConexao():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
        conn = psycopg2.connect(**params)
  
        # create a cursor
        cur = conn.cursor()

        cur.execute('SELECT version()')
 
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
     # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def executarComando(comando):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
  
        # create a cursor
        cur = conn.cursor()
        
        # execute a statement
        cur.execute(comando)

        conn.commit()
  
        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def RegistroExite(comando):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
  
        # create a cursor
        cur = conn.cursor()
        
        # execute a statement
        cur.execute(comando)
        existe = True

        try:
            x = cur.fetchone()[0]
        except :
            existe = False
        
        return existe
        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return False
    finally:
        if conn is not None:
            conn.close()
        
def criarTabelaMunicipio():
    comando = "create table if not exists municipio (id serial primary key, uf varchar(2), regiao varchar(512), municipio varchar(512), categoria varchar(1));"
    comando = comando + "delete from municipio;"
    executarComando(comando)

def criarTabelaHospedagens():
    comando = " create table if not exists hospedagens (id serial primary key, razaosocial varchar(512), nomefantasia varchar(512), cnpj varchar(512), naturezajuridica varchar(512), datainicio varchar(512), porte varchar(512), situacao varchar(512), tipoatividade varchar(512), "
    comando = comando + " subtipo varchar(512), cep varchar(512), uf varchar(2), localidade varchar(512), bairro varchar(512), logradouro varchar(512), telefone varchar(512), fax varchar(512), email2 varchar(512), email3 varchar(512), site varchar(512), "
    comando = comando + " codigocertificado varchar(512), codigodescricaocnae varchar(512), uh varchar(512), uhacessiveis varchar(512), uhscaoguia varchar(512), uhstps varchar(512), totalleitos varchar(512), linguas varchar(512), segmentos varchar(512), servicos varchar(512), equipamentos varchar(512), latitude decimal(15,6), longitude decimal(15,6));"
    comando = comando + "delete from hospedagens;"
    executarComando(comando)

def criarTabelaRestaurantes():
    comando = "create table if not exists restaurantes (id serial primary key, razaosocial varchar(512) ,nomefantasia varchar(512) ,cnpj varchar(512) ,naturezajuridica varchar(512) ,datainicio varchar(512) ,porte varchar(512) ,situacao varchar(512) ,tipoatividade varchar(512) ,subtipo varchar(512) ,cep varchar(512) ,uf varchar(512) ,localidade varchar(512) ,bairro varchar(512) ,logradouro varchar(512) ,telefone varchar(512) ,fax varchar(512) ,email2 varchar(512) ,email3 varchar(512) ,site varchar(512) ,codigocertificado varchar(512) ,codigodescricaocnae varchar(512) ,capacidade varchar(512) , linguas varchar(512), latitude decimal(15,6), longitude decimal(15,6));"
    comando = comando + "delete from restaurantes;"
    executarComando(comando)

def criarTabelaEspabelecimentosEspecializados():
    comando = "create table if not exists especializados ( id serial primary key, razaosocial varchar(512) , nomefantasia varchar(512) ,cnpj varchar(512) , natureza varchar(512) ,datainicio varchar(512) , porte varchar(512) , situacao varchar(512) , tipoatividade varchar(512) , subtipo varchar(512) , cep varchar(512) , uf varchar(512) , localidade varchar(512) , bairro varchar(512) , logradouro varchar(512) , telefone varchar(512) , fax varchar(512) , email2 varchar(512) , email3 varchar(512) , site varchar(512) , certificado varchar(512) , codigodescricaocnae varchar(512) , servicos  varchar(512), segmento varchar(512) ,linguas varchar(512), latitude decimal(15,6), longitude decimal(15,6));"
    comando = comando + "delete from especializados;"
    executarComando(comando)