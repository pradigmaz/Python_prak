class Film:
    def __init__(self, title, genre, director, year, duration, studio, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors

class FilmController:
    def __init__(self):
        self.films = []

    def add_film(self, film):
        self.films.append(film)

    def get_all(self):
        return self.films

    def get_by_title(self, title):
        for f in self.films:
            if f.title.lower() == title.lower():
                return f
        return None

    def remove_by_title(self, title):
        self.films = [f for f in self.films if f.title.lower() != title.lower()]

class FilmView:
    def show_menu(self):
        print("===== Редактирование данных каталога фильмов =====")
        print("Действия с фильмами:")
        print("1 - добавление фильма")
        print("2 - каталог фильмов")
        print("3 - просмотр определенного фильма")
        print("4 - удаление фильма")
        print("q - выход из программы")
        return input("Выберите вариант действия: ")

    def show_all(self, films):
        print("=== Каталог фильмов ===")
        for f in films:
            print(f"- {f.title} ({f.year}) [{f.genre}]")

    def show_film(self, film):
        if not film:
            print("Фильм не найден.")
            return
        print("=== Информация о фильме ===")
        print(f"Название: {film.title}")
        print(f"Жанр: {film.genre}")
        print(f"Режиссер: {film.director}")
        print(f"Год выпуска: {film.year}")
        print(f"Длительность: {film.duration}")
        print(f"Студия: {film.studio}")
        print(f"Актеры: {film.actors}")

    def add_film(self):
        title = input("Название фильма: ")
        genre = input("Жанр: ")
        director = input("Режиссер: ")
        year = input("Год выпуска: ")
        duration = input("Длительность: ")
        studio = input("Студия: ")
        actors = input("Актеры: ")
        return Film(title, genre, director, year, duration, studio, actors)

    def ask_title(self, text="Введите название фильма: "):
        return input(text)


def main():
    controller = FilmController()
    view = FilmView()

    while True:
        choice = view.show_menu()
        if choice == '1':
            film = view.add_film()
            controller.add_film(film)
        elif choice == '2':
            view.show_all(controller.get_all())
        elif choice == '3':
            title = view.ask_title()
            view.show_film(controller.get_by_title(title))
        elif choice == '4':
            title = view.ask_title("Название фильма для удаления: ")
            controller.remove_by_title(title)
            print("Готово.")
        elif choice == 'q':
            break
        else:
            print("Нет такого варианта.")

if __name__ == "__main__":
    main()
