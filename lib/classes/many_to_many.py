class Article:
    # Class-level attribute to store all Article instances
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class.")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be an instance of the Magazine class.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be a string between 5 and 50 characters.")
        
        self._author = author
        self._magazine = magazine
        self._title = title

        # Add the new instance to the class-level list
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise Exception("Author must be an instance of the Author class.")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise Exception("Magazine must be an instance of the Magazine class.")
        self._magazine = new_magazine


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string.")
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        # Return all articles written by this author
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        # Return a unique list of magazines the author has contributed to
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        # Create and return a new Article instance
        return Article(self, magazine, title)

    def topic_areas(self):
        # Return a unique list of categories of the magazines the author has contributed to
        if not self.articles():
            return None
        return list(set(magazine.category for magazine in self.magazines()))


class Magazine:
    # Class-level attribute to store all Magazine instances
    all = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("Category must be a non-empty string.")
        
        self._name = name
        self._category = category

        # Add the new instance to the class-level list
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
            raise Exception("Name must be a string between 2 and 16 characters.")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise Exception("Category must be a non-empty string.")
        self._category = new_category

    def articles(self):
        # Return all articles published in this magazine
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        # Return a unique list of authors who have written for this magazine
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        # Return a list of titles of all articles written for this magazine
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        # Return authors who have written more than 2 articles for the magazine
        authors = [article.author for article in self.articles()]
        contributing_authors = [author for author in set(authors) if authors.count(author) > 2]
        return contributing_authors if contributing_authors else None

    @classmethod
    def top_publisher(cls):
        # Return the magazine with the most articles
        if not Article.all:
            return None
        return max(cls.all, key=lambda magazine: len(magazine.articles()), default=None)