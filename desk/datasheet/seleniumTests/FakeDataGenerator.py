from faker import Faker


class FakeDataGenerator(Faker):

    def __init__(self) -> None:
        """
        Initialize Faker() in localization eng
        :return: object faker
        :rtype: None
        """
        super().__init__(['en_US'])

    def fake_name(self) -> str:
        """
        Give the name of the user.
        :return: name of the user
        :rtype: str
        """
        return self.name()

    def fake_login(self) -> str:
        """
        Give the concatenation of first and last name
        :return: login
        :rtype: str
        """
        return self.last_name().join(self.first_name())

    def fake_title(self) -> str:
        """
        Give the title of guideline.
        :return: title
        :rtype: str
        """
        return self.sentence()

    def fake_text(self) -> str:
        """
        Give guideline content
        :return: content
        :rtype: str
        """
        content = [self.text() for x in range(1, 10)]
        return ' '.join(content).replace('\n', ' ')

    def fake_email(self) -> str:
        """
        Give the email
        :return: email
        :rtype: str
        """
        return self.email()

    def __del__(self):
        pass


# if __name__ == "__main__":
#     obj_test = FakeDataGenerator()
#     obj_test.fake_text()
