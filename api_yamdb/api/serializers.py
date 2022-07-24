from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User

SERIALIZERS_FIELDS = {
    "ReviewSerializer": (
        "id",
        "text",
        "author",
        "score",
        "pub_date",
        "title",
    ),
    "CommentSerializer": (
        "id",
        "text",
        "author",
        "pub_date",
        "review"
    ),
    "TitleSerializer": (
        "id",
        "name",
        "year",
        "rating",
        "category",
        "genre",
        "description",
    ),
    "GenreSerializer": (
        "name",
        "slug",
    ),
    "CategorySerializer": (
        "name",
        "slug",
    ),
    "UserSerializer": (
        "username",
        "email",
        "first_name",
        "last_name",
        "bio",
        "role",
    ),
}


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = SERIALIZERS_FIELDS["UserSerializer"]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = SERIALIZERS_FIELDS["GenreSerializer"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = SERIALIZERS_FIELDS["CategorySerializer"]


class TitleReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(many=True, read_only=True)
    rating = serializers.IntegerField(
        read_only=True,
        allow_null=True
    )

    class Meta:
        model = Title
        fields = SERIALIZERS_FIELDS["TitleSerializer"]


class TitleWriteSerializer(TitleReadSerializer):
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(), slug_field="slug", many=True
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field="slug"
    )

    class Meta:
        model = Title
        fields = SERIALIZERS_FIELDS["TitleSerializer"]


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        slug_field="username",
        read_only=True,
    )
    title = serializers.SlugRelatedField(
        slug_field="name",
        read_only=True,
    )
    score = serializers.IntegerField()

    class Meta:
        fields = SERIALIZERS_FIELDS["ReviewSerializer"]
        model = Review

    def validate(self, data):
        request = self.context["request"]
        if request.method != "POST":
            return data
        author = request.user
        title_id = self.context["view"].kwargs.get("title_id")
        title = get_object_or_404(Title, pk=title_id)
        if Review.objects.filter(title=title, author=author).exists():
            raise serializers.ValidationError(
                "Вы уже оставили свой отзыв" "к этому произведению!"
            )
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
    )
    review = serializers.HiddenField(default=Review)

    class Meta:
        fields = SERIALIZERS_FIELDS["CommentSerializer"]
        model = Comment


class UserSignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("username", "email")

    def validate_username(self, value):
        if value == "me":
            raise serializers.ValidationError(
                "me нельзя использовать в качестве username"
            )
        return value


class UserSignupConfirmSerializer(serializers.ModelSerializer):
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "confirmation_code")


class UserEditingSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()
    email = serializers.ReadOnlyField()
    role = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = SERIALIZERS_FIELDS["UserSerializer"]
