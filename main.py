from re import match as rem

PATTERN = r'https://apps\.apple\.com(?:/[a-z]{2})?/app(?:/[^/]+)?/(id\d+)'

def clean_url(url: str) -> str | None:
    url = url.strip()

    if 'apple' not in url.lower():
        return None

    match = rem(PATTERN, url)
    if not match:
        return None

    return f'https://apps.apple.com/app/{match.group(1)}'


if __name__ == '__main__':
    while True:
        user_input = input('Enter App Store URL\n> ').strip()

        if not user_input:
            print('\n-_-')
            break

        res = clean_url(user_input)
        print('Invalid URL.\n' if res is None else f'\nResult:\n{res}\n')