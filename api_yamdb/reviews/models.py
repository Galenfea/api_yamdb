from django.db import models

from users.models import User
from .validators import validate_one_to_ten_range, validate_title_year

# Литеральные константы
CONSTATNTS = {
    "CATEGORY_NAME": "Категория",
    "CATEGORIES_NAME": "категории",
    "URL_NAME_СATEGORY": "Ссылка на категорию",
    "GENRE_NAME": "Жанр",
    "GENRES_NAME": "жанры",
    "URL_NAME_GENRE": "Ссылка на жанр",
    "TEXT_NAME": "Текст обзора",
    "AUTHOR_NAME": "Автор",
    "DATE_NAME": "Дата публикации",
    "REVIEW_NAME": "обзор",
    "REVIEWS_NAME": "обзоры",
    "SCORE_NAME": "оценка",
    "TITLE_NAME": "произведение",
    "TITLES_NAME": "произведения",
    "RATING_NAME": "Рейтинг",
    "COMMENT_NAME": "комментарий",
    "COMMENTS_NAME": "комментарии",
    "NAME": "Название",
    "DESCRIPTION": "Описание",
    "YEAR": "Год выпуска",
}


class Category(models.Model):
    name = models.CharField(CONSTATNTS["CATEGORY_NAME"], max_length=256)
    slug = models.SlugField(
        CONSTATNTS["URL_NAME_СATEGORY"], unique=True, max_length=256
    )

    class Meta:
        ordering = ("name",)
        verbose_name = CONSTATNTS["CATEGORY_NAME"]
        verbose_name_plural = CONSTATNTS["CATEGORIES_NAME"]

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(CONSTATNTS["GENRE_NAME"], max_length=256)
    slug = models.SlugField(
        CONSTATNTS["URL_NAME_GENRE"], unique=True, max_length=256
    )

    class Meta:
        ordering = ("name",)
        verbose_name = CONSTATNTS["GENRE_NAME"]
        verbose_name_plural = CONSTATNTS["GENRES_NAME"]

    def __str__(self):
        return self.name


class Title(models.Model):
    """Модель произведения содержит поля:
    - name - название произведение;
    - year - год публикации;
    - description - текстовое описание произведения;
    - genre - жанр произведения;
    - category - категория произведения (книга, музыка, фильм);
    - year - год выпуска произведения.
    """

    name = models.CharField(
        verbose_name=CONSTATNTS["NAME"], max_length=255, blank=False
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name="category",
        verbose_name=CONSTATNTS["CATEGORY_NAME"],
    )
    description = models.TextField(
        verbose_name=CONSTATNTS["DESCRIPTION"],
        blank=True,
    )
    genre = models.ManyToManyField(
        Genre, through="TitleGenre", verbose_name=CONSTATNTS["GENRE_NAME"]
    )
    year = models.SmallIntegerField(
        verbose_name=CONSTATNTS["YEAR"],
        validators=[validate_title_year],
    )

    class Meta:
        ordering = (
            "name",
        )
        verbose_name = CONSTATNTS["TITLE_NAME"]
        verbose_name_plural = CONSTATNTS["TITLES_NAME"]

    def __str__(self):
        name_limited_withdrawal = self.name[:15]
        return f"{name_limited_withdrawal}"


class TitleGenre(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.genre}"


class Review(models.Model):
    """Модель обзора содержит поля:
    - text - текст обзора;
    - pub_date - дата публикации, по-умолчанию текущая;
    - author - автор (при удалении автора удаляются все обзоры);
    - score - частная оценка произведения, тип int;
    - title - произведение, на которое сделан обзор.
    """

    text = models.TextField(CONSTATNTS["TEXT_NAME"])
    pub_date = models.DateTimeField(CONSTATNTS["DATE_NAME"], auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name=CONSTATNTS["AUTHOR_NAME"],
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name=CONSTATNTS["TITLE_NAME"],
    )
    score = models.PositiveSmallIntegerField(
        validators=[validate_one_to_ten_range],
        blank=False,
        null=False,
        verbose_name=CONSTATNTS["SCORE_NAME"],
    )

    class Meta:
        ordering = ("-pub_date",)
        verbose_name = CONSTATNTS["REVIEW_NAME"]
        verbose_name_plural = CONSTATNTS["REVIEWS_NAME"]
        constraints = [
            models.UniqueConstraint(
                fields=["title", "author"], name="unique_review"
            ),
        ]

    def __str__(self):
        text_limited_withdrawal = self.text[:15]
        return f"{text_limited_withdrawal}"


class Comment(models.Model):
    """Модель комментария содержит поля:
    - text - текст комментария;
    - pub_date - дата публикации, по-умолчанию текущая;
    - author - автор (при удалении автора удаляются все сообщения)
    - review - обзор для которого написаны комментарии.
    """

    text = models.TextField(CONSTATNTS["COMMENT_NAME"], blank=False)
    pub_date = models.DateTimeField(CONSTATNTS["DATE_NAME"], auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name=CONSTATNTS["AUTHOR_NAME"],
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name="comments",
        blank=False,
        verbose_name=CONSTATNTS["TEXT_NAME"],
    )

    class Meta:
        ordering = ("-pub_date",)
        verbose_name = CONSTATNTS["COMMENT_NAME"]
        verbose_name_plural = CONSTATNTS["COMMENTS_NAME"]

    def __str__(self):
        text_limited_withdrawal = self.text[:15]
        return f"{text_limited_withdrawal}"
