from django.db import models
from stdimage.models import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.urls import reverse

class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)
    class Meta:
        abstract = True


class Categoria(Base):
    nome = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField('Slug', max_length=250, unique=True, blank=True, editable=False)


    class Meta:
        ordering = ('nome',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'


    def __str__(self):
        return self.nome


    def __str__(self):
        return self.nome


    def get_absolute_url(self):
        return reverse(
            'usuarios:listar_usuarios_por_categoria',
            kwargs={
                'slug_categoria': self.slug
            }
        )





class Cadastro(Base):
    '''INFORMAÇOES BASICAS'''
    nome = models.CharField('Nome ', max_length=200)
    genero = models.CharField('Gênero ', max_length=30)
    etnia = models.CharField('Etnia ', max_length=200)
    deficiencia = models.CharField('Deficiência ', max_length=200)
    estado = models.CharField('Estado ', max_length=200)
    cidade = models.CharField('Cidade ', max_length=200)
    curso = models.CharField('Curso ', max_length=200)
    periodo = models.CharField('Periodo', max_length=200)


    '''CONTATO'''
    email = models.EmailField('Email ', max_length=200, blank=True)
    linkedIn = models.CharField('LinkedIn', max_length=200, blank=True)
    site = models.CharField("Site pessoal ", max_length=200, blank=True)

    '''TELEFONE'''
    pessoal = models.CharField('Telefone Pessoal ', max_length=50, blank=True)
    residencial = models.CharField('Telefone Residencial ', max_length=50, blank=True)
    outro_tel = models.CharField('Algum outro', max_length=50, blank=True)

    '''EXPERIENCIA'''
    exp = models.TextField('Experiência Profissional ', blank=True)
    atv = models.TextField('Atividades Filantrópicas ', blank=True)


    '''QUALIFICAÇOES'''
    var1 = models.CharField('Habilidade 1 ', max_length=50, blank=True)
    porc1 = models.IntegerField('Porcentagem 1', blank=True, default=1)
    var2 = models.CharField('Habilidade 2 ', max_length=50, blank=True)
    porc2 = models.IntegerField('Porcentagem 2',  blank=True, default=1)
    var3 = models.CharField('Habilidade 3 ', max_length=50, blank=True)
    porc3 = models.IntegerField('Porcentagem 3',  blank=True, default=1)
    var4 = models.CharField('Habilidade 4 ', max_length=50, blank=True)
    porc4 = models.IntegerField('Porcentagem 4',  blank=True, default=1)

    '''IDIOMA'''
    idi1 = models.CharField('Idioma 1 ', max_length=50, blank=True)
    porc5 = models.IntegerField('Porcentagem 1',  blank=True, default=1)
    idi2 = models.CharField('Idioma 2 ', max_length=50, blank=True)
    porc6 = models.IntegerField('Porcentagem 2',  blank=True, default=1)
    idi3 = models.CharField('Idioma 3 ', max_length=50, blank=True)
    porc7 = models.IntegerField('Porcentagem 3',  blank=True, default=1)
    idi4 = models.CharField('Idioma 4 ', max_length=50, blank=True)
    porc8 = models.IntegerField('Porcentagem 4',  blank=True, default=1)

    '''ESCOLARIDADE'''
    enfu = models.CharField('Ensino fundamental ', max_length=50, blank=True)
    enme = models.CharField('Ensino médio ', max_length=50, blank=True)
    bach = models.CharField('Bacharelado ', max_length=50, blank=True)
    mes = models.CharField('Mestrado  ', max_length=50, blank=True)
    dout = models.CharField('Doutorado  ', max_length=50, blank=True)

    '''OBJETIVOS'''
    arint = models.TextField('Áreas de interesse ', blank=True)
    salario = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    objpe = models.TextField('Objetivos Pessoais ', blank=True)
    objpro = models.TextField('Objetivos Profissionais ', blank=True)


    imagem_banner = StdImageField('Imagem Banner', upload_to='usuario', variations={'thumb': (1920, 1080)})
    imagem_perfil = StdImageField('Imagem Perfil', upload_to='usuario', variations={'thumb': (500, 500)})
    slug = models.SlugField('Slug', max_length=250, unique=True, blank=True, editable=False)
    categoria = models.ForeignKey('usuario.Categoria', verbose_name='Categoria', on_delete=models.CASCADE)


    class Meta:
        ordering = ('nome',)
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'


    def __str__(self):
        return self.nome

    def __str__(self):
        return self.nome


    def get_absolute_url(self):
        return reverse(
            'usuarios:detalhes_usuarios',
            kwargs={
                'id_usuario': self.id,
                'slug_usuario': self.slug
            }
        )


def usuario_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)



def categoria_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(usuario_pre_save, sender= Cadastro)
signals.pre_save.connect(categoria_pre_save, sender=Categoria)