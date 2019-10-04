from django.core.management.base import BaseCommand
from backend.blog.models import Post, BlogCategory


class Command(BaseCommand):
    help = 'Add post'

    def handle(self, *args, **options):
        category = BlogCategory.objects.create(name="Test3", slug="test3")
        i = 1
        mini_text = """В последнее время в русскоязычном сегменте интернета все реже и реже попадаются толковые статьи. 
        Особенно это касается статей на техническую тему. Многие из них лишь поверхностно касаются озвученных вопросов, 
        даже не предоставляя никаких ссылок на дополнительную информацию."""
        text = """Данное руководство посвящено процессу генерации документации с помощью связки reStructuredText, 
        Python Sphinx, GitHub и сервиса Read the Docs. Ключевую роль в этой связке играет генератор документации Python 
        Sphinx, разработанный для документирования языка программирования Python, но активно прижившегося и в других 
        проектах.
        Sphinx использует облегченный язык разметки reStructuredText, с помощью которого можно создавать текстовые 
        документы с четкой структурой. В дальнейшем, такие документы могут быть преобразованы в любой другой формат: 
        HTML, LaTeX, ODT, ePub, man и другие. Sphinx расширяет возможности reStructuredText и упрощает процесс 
        генерации в различные форматы.
        GitHub позволяет организовать совместную работу над документацией и значительно упрощает процесс отслеживания 
        изменений. Сервис Read the Docs предоставляет бесплатную площадку для публикации документации, сгенерированной 
        с помощью Sphinx. Он автоматизирует процесс создания и загрузки Sphinx-документации после каждой фиксации 
        изменений на GitHub. """
        while i <= 2:
            post = Post.objects.create(author_id=1,
                                       title="title-{}".format(post.id),
                                       mini_text=mini_text,
                                       text=text,
                                       # slug="title",
                                       category_id=category.id)
            i += 1
        self.stdout.write('Success add posts')
