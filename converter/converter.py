import chardet

class Converter:
    def __init__(self):
        pass

    @staticmethod
    def handle_uploaded_file(file, convert_type, charset_type, sync_ms):
        # logger.info('Success!!!')
        content = file.read()
        return content
