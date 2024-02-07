import pickle

from huffify.annotations import EncodedData

from huffify.abstract import PersistenceManager


class Pickelifier(PersistenceManager):
    def __init__(
        self,
        input_path: str = "input.txt",
        output_path: str = "output.txt",
        encoding: str = "utf-8",
    ) -> None:
        self.input_path = input_path
        self.output_path = output_path
        self.encoding = encoding

    def save(self, encoded_data: EncodedData) -> None:
        with open(self.output_path, "wb", encoding=self.encoding) as f:
            pickle.dump(encoded_data, f)

    def load(self) -> EncodedData:
        with open(self.output_path, "rb", encoding=self.encoding) as f:
            data: EncodedData = pickle.load(f)
        return data
