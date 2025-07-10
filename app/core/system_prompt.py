def get_system_prompt() -> str:
    with open('system_prompt.txt', 'r', encoding='utf-8') as file:
        return file.read()
