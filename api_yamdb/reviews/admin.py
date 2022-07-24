from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title

# Литеральные константы
EMPTY = "-пусто-"


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Источник конфигурации модели Review, регистрируемой в админке, позволяет:
    - отображать в админке первичный ключ, текст, дату публикации, автора и
    оценку каждого обзора;
    - редактировать оценку и привязку к произведению;
    - проводить поиск по тексту и произведению;
    - фильттровать по дате публицкации;
    - выводить "-пусто-" в полях со значением None."""

    list_display = (
        "pk",
        "title",
        "text",
        "pub_date",
        "author",
        "score",
    )
    list_editable = (
        "title",
        "score",
    )
    search_fields = (
        "text",
        "title",
    )
    list_filter = ("pub_date",)
    empty_value_display = EMPTY


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Источник конфигурации модели Comment, регистрируемой в админке, позволяет:
    - отображать в админке первичный ключ, текст комментария, дату создания,
    автора комментария и первые символы комментируемого обзора;
    - проводить поиск по тексту комментария и обзору;
    - выводить "-пусто-" в полях со значением None."""

    list_display = (
        "pk",
        "text",
        "pub_date",
        "author",
        "review",
    )
    search_fields = (
        "text",
        "review",
    )
    list_filter = (
        "pub_date",
        "review",
    )
    empty_value_display = EMPTY


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    """Источник конфигурации модели Title, регистрируемой в админке, позволяет:
    - отображать в админке первичный ключ, название, дату публикации, автора и
    рейтинг произведения;
    - редактировать название;
    - проводить поиск по названию;
    - фильттровать по дате публицкации, названию и рейтингу;
    - выводить "-пусто-" в полях со значением None."""

    list_display = (
        "pk",
        "name",
    )
    list_editable = ("name",)
    search_fields = ("name",)
    list_filter = (
        "name",
    )
    empty_value_display = EMPTY


@admin.register(Genre)
class GroupAdmin(admin.ModelAdmin):
    """Источник конфигурации модели Genre, регистрируемой в админке, позволяет:
    - отображать в админке первичный ключ, название жанра и ссылку;
    - редактировать название жанра;
    - проводить поиск по названию жанра;
    - выводить "-пусто-" в полях со значением None."""

    list_display = (
        "pk",
        "name",
        "slug",
    )
    list_editable = ("name",)
    search_fields = ("name",)
    empty_value_display = EMPTY


@admin.register(Category)
class GroupAdmin(admin.ModelAdmin):
    """Источник конфигурации модели Category, регистрируемой в админке,
    позволяет:
    - отображать в админке первичный ключ, название категории и ссылку;
    - редактировать название категории;
    - проводить поиск по названию категории;
    - выводить "-пусто-" в полях со значением None."""

    list_display = (
        "pk",
        "name",
        "slug",
    )
    list_editable = ("name",)
    search_fields = ("name",)
    empty_value_display = EMPTY
