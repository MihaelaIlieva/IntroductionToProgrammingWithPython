def methodify():
    methods = set()

    def traverse(obj, path=''):
        for name in dir(obj):
            attr = getattr(obj, name)

            if callable(attr) and len(name) == 1 and name.isalnum() and 'clue' in path:
                methods.add(attr)

            if isinstance(attr, type) and not name.startswith("__") and not name.endswith("__"):
                new_path = f"{path}.{name}" if path else name
                traverse(attr, path=new_path)

    traverse(secret)

    interesting_methods = []
    for method in methods:
        try:
            method_result = method()
            if isinstance(method_result, int):
                if method_result % 2 == 0:
                    interesting_methods.append(method)
            elif isinstance(method_result, str):
                interesting_methods.add(method)
            else:
                raise BaseException("Грешка в изпълнението")
        except TypeError:
            interesting_methods.append(method)
        except BaseException:
            interesting_methods.append(method)

    return tuple(sorted(interesting_methods, key=lambda x: x.__name__))


# Пример за използване:
if __name__ == "__main__":
    import secret

    result = methodify()
    print(result)