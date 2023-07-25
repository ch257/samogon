import aiofiles

class FileSystem:
    def __init__(self, errors):
        self.errors = errors

    def read_binary_file(self, file_path):
        b_line = ''.encode('utf-8')
        try:
            file = open(file_path, mode='rb')
            b_line = file.read()
            file.close()
        except FileNotFoundError:
            self.errors.add_error(f"Нет файла '{file_path}'")
        
        return b_line
        
    async def aio_read_binary_file(self, file_path):
        b_line = ''.encode('utf-8')
        try:
            async with aiofiles.open(file_path, mode='rb') as f:
                b_line = await f.read()
        except FileNotFoundError:
            self.errors.add_error(f"Нет файла '{file_path}'")

        return b_line