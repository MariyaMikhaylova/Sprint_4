import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books_in_books_genre_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_name_more_40_book_not_add(self):
        collector = BooksCollector()

        collector.add_new_book('Книга с названием,состоящим из 41 символа')
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_add_book_twice_book_add_once(self):
        collector = BooksCollector()

        collector.add_new_book('Добавляю книгу дважды')
        collector.add_new_book('Добавляю книгу дважды')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_genre_in_list_true(self, genre):
        collector = BooksCollector()

        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', genre)
        assert collector.get_book_genre('Книга') == genre

    def test_set_book_genre_genre_not_in_list_genre_not_add(self):
        collector = BooksCollector()

        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Историческая')
        assert collector.get_book_genre('Книга') == ''

    def test_get_books_with_specific_genre_books_different_genre_return_chosen(self):
        collector = BooksCollector()

        collector.add_new_book('Книга-Ужас')
        collector.set_book_genre('Книга-Ужас', 'Ужасы')
        collector.add_new_book('Книга-Комедия')
        collector.set_book_genre('Книга-Комедия', 'Комедии')
        assert len(collector.get_books_with_specific_genre('Комедии')) == 1

    def test_get_books_genre_books_different_genre_return_books_name_and_genre_in_dictionary(self):
        collector = BooksCollector()

        collector.add_new_book('Книга-Ужас')
        collector.set_book_genre('Книга-Ужас', 'Ужасы')
        collector.add_new_book('Книга-Комедия')
        collector.set_book_genre('Книга-Комедия', 'Комедии')
        assert collector.get_books_genre() == {'Книга-Комедия': 'Комедии', 'Книга-Ужас': 'Ужасы'}

    def test_get_books_for_children_different_genre_return_filtered(self):
        collector = BooksCollector()

        collector.add_new_book('Книга-Ужас')
        collector.set_book_genre('Книга-Ужас', 'Ужасы')
        collector.add_new_book('Книга-Комедия')
        collector.set_book_genre('Книга-Комедия', 'Комедии')
        assert len(collector.get_books_for_children()) == 1

    def test_add_book_in_favorites_different_book_add_all_books(self):
        collector = BooksCollector()

        collector.add_new_book('Книга-Ужас')
        collector.add_new_book('Книга-Комедия')
        collector.add_book_in_favorites('Книга-Ужас')
        collector.add_book_in_favorites('Книга-Комедия')
        assert len(collector.get_list_of_favorites_books()) == 2

    def test_add_book_in_favorites_one_book_twice_add_once(self):
        collector = BooksCollector()

        collector.add_new_book('Добавляю книгу в избранное дважды')
        collector.add_book_in_favorites('Добавляю книгу в избранное дважды')
        collector.add_book_in_favorites('Добавляю книгу в избранное дважды')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_delete_one_of_two_stay_one(self):
        collector = BooksCollector()

        collector.add_new_book('Книга-Ужас')
        collector.add_new_book('Книга-Комедия')
        collector.add_book_in_favorites('Книга-Ужас')
        collector.add_book_in_favorites('Книга-Комедия')
        collector.delete_book_from_favorites('Книга-Комедия')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_get_list_of_favorites_books_different_book_return_books_name_in_list(self):
        collector = BooksCollector()

        collector.add_new_book('Книга-Ужас')
        collector.add_new_book('Книга-Комедия')
        collector.add_book_in_favorites('Книга-Ужас')
        collector.add_book_in_favorites('Книга-Комедия')
        assert collector.get_list_of_favorites_books() == ['Книга-Ужас', 'Книга-Комедия']
