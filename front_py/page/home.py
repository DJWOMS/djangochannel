from pyoms.core.base import Base
from pyoms.core.show import Show

class BlockCourses(Base):
    """Блоки курсов"""

    def created(self):
        # Свернуть блоки курсов
        for i in [1, 2, 3, 4]:
            Show('#block-{}'.format(i)).hide()

    def click(self, tag):
        # Свернуть\развернуть
        Show(tag).toggle("blind")
