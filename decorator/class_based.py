class DataSource:
    def write_data(self, data):
        pass

    def read_data(self):
        pass


class FileDataSource(DataSource):
    def __init__(self, filename):
        self._filename = filename

    def write_data(self, data):
        with open(self._filename, "w") as f:
            f.write(data)

    def read_data(self):
        with open(self._filename, "r") as f:
            return f.read()


class DataSourceDecorator(DataSource):
    def __init__(self, wrapee: DataSource):
        self._wrapee = wrapee

    def write_data(self, data):
        return self._wrapee.write_data()

    def read_data(self):
        return self._wrapee.read_data()


class EncryptionDecorator(DataSourceDecorator):
    def write_data(self, data):
        encrypted = "".join(chr(ord(c) + 1) for c in data)
        self._wrapee.write_data(encrypted)

    def read_data(self):
        data = self._wrapee.read_data()
        return "".join(chr(ord(c) - 1) for c in data)


class RetryDecorator(DataSourceDecorator):
    def write_data(self, data):
        for i in range(3):
            try:
                self._wrapee.write_data(data)
                return
            except Exception as e:
                print(f"Attempt {i+1} failed: {e}")
        raise Exception("Max retries reached")


source = FileDataSource("demo.txt")
secure = RetryDecorator(EncryptionDecorator(source))
secure.write_data("Secured Data")
