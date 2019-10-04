from pyoms.core.base import Base
from pyoms.core.show import Show

class SideBar(Base):
    """Левое меню"""
    def click(self, tag):
        # Свернуть\развернуть
        Show(tag).toggle("blind")