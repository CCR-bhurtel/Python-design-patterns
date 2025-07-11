from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class DarkButton(Button):
    def render(self) -> str:
        return "Dark Button"


class LightButton(Button):
    def render(self):
        return "Light Button"


class TextBox(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class DarkTextBox(TextBox):
    def render(self):
        return "Dark TextBox"


class LightTextBox(Button):
    def render(self):
        return "Light TextBox"


class ThemeFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_textbox(self) -> TextBox:
        pass


class DarkThemeFactory(ThemeFactory):
    def create_button(self):
        return DarkButton()

    def create_textbox(self):
        return DarkTextBox()


class LightThemeFactory(ThemeFactory):
    def create_button(self):
        return LightButton()

    def create_textbox(self):
        return LightTextBox()


def render_ui(factory: ThemeFactory):
    button = factory.create_button()
    textbox = factory.create_textbox()

    print(button.render())
    print(textbox.render())


if __name__ == "__main__":
    factory = DarkThemeFactory()
    render_ui(factory)
