class HtmlElement:
    indent_size = 2
    
    def __init__(self, name='', text=''):
        self.text = text
        self.name = name
        self.elements = []


class HtmlBuilder:
    def __init__(self, root_name) -> None:
        self.root_name = root_name
        self.__root = HtmlElement(root_name)

    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )

    # chain operator
    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self
    
    @staticmethod
    def create(name):
        return HtmlBuilder(name)

builder = HtmlBuilder.create('good')
# builder.add_child('li', 'hello')
# builder.add_child('li', 'world')

builder.add_child_fluent('li', 'hello')\
    .add_child_fluent('li', 'World')

print(builder)