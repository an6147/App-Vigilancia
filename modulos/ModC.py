from typing import IO, Generator

def ranged \
        (
            file: IO[bytes],
            start: int = 0,
            end: int = None,
            block_size: int = 8192,
        ) -> Generator[bytes, None, None]:
    consumed = 0

    file.seek(start)

    while True:
        data_length = min(block_size, end - start - consumed) if end else block_size

        if data_length <= 0:
            break

        data = file.read(data_length)

        if not data:
            break

        consumed += data_length

        yield data

    if hasattr(file, 'close'):
        file.close()