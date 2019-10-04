from django.db.models.query import QuerySet

from rest_framework.views import APIView
from rest_framework.response import Response


class BlankGetAPIView(APIView):
    """Заготовка для GET-запросов"""

    # Обязательно указать один из них
    queryset = None
    model = None

    # Обязательный параметр
    serializer = None

    # Необязательные параметры
    many = True  # Опция для сериализера, скорее всего уберу
    pk_name = 'pk'  # Название параметра, который передается в GET
    filter_name = None  # Опция связана с pk_name, при фильтрации используется как ключ, pk_name как значение
    response_name = None  # Опция отвечает за название ключа в ответе
    filter_params = {}  # Параметры фильтрации, не работают при указании filter_name
    order_params = ''  # Сортировка запроса

    def __init__(self, *args, **kwargs):
        assert self.serializer is not None, (
            'Укажите serializer в {}'.format(self.__class__.__name__)
        )
        assert self.model is not None or self.queryset is not None, (
            'Укажите model или queryset в {}'.format(self.__class__.__name__)
        )
        assert isinstance(self.filter_params, dict), (
            'Укажите filter_params в {} как словарь'.format(self.__class__.__name__)
        )
        super().__init__(*args, **kwargs)

    def get(self, request):
        queryset = self.get_queryset(request)

        if self.order_params:
            queryset = queryset.order_by(self.order_params)

        if self.response_name:
            return Response(
                {self.response_name: self.serializer(queryset, many=self.many).data}
            )
        return Response(self.serializer(queryset, many=self.many).data)

    def get_queryset(self, request):
        if self.queryset is not None:
            queryset = self.queryset
            if isinstance(queryset, QuerySet):
                queryset = queryset.all()
            return queryset

        if self.filter_params:
            return self.model.objects.filter(**self.filter_params)

        if self.filter_name:
            pk = request.GET.get(self.pk_name)
            return self.model.objects.filter(**{self.filter_name: pk})

        return self.model.objects.all()
