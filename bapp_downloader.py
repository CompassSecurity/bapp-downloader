import requests
import shutil
from bs4 import BeautifulSoup
from pathlib import Path

BASE_URL = 'https://portswigger.net/bappstore/'
OUT_DIR = 'bapps'

BAPP_IDS = [
    ('Active Scan++', 'active_scan_plus_plus.bapp', '3123d5b5f25c4128894d97ea1acc4976'),
    ('Add Custom Header', 'add_custom_header.bapp', '807907f5380c4cb38748ef4fc1d8cdbc'),
    ('AuthMatrix', 'auth_matrix.bapp', '30d8ee9f40c041b0bfec67441aad158e'),
    ('Autorize', 'autorize.bapp', 'f9bbac8c4acf4aefa4d7dc92a991af2f'),
    ('Blackslash Powered Scanner', 'backslash_powered_scanner.bapp', '9cff8c55432a45808432e26dbb2b41d8'),
    ('Collaborator Everywhere', 'collaborator_everywhere.bapp', '2495f6fb364d48c3b6c984e226c02968'),
    ('Content Type Converter', 'content_type_converter.bapp', 'db57ecbe2cb7446292a94aa6181c9278'),
    ('CORS*, Additional CORS Checks', 'cors.bapp', '420a28400bad4c9d85052f8d66d3bbd8'),
    ('GraphQL Raider', 'graphql_raider.bapp', '4841f0d78a554ca381c65b26d48207e6'),
    ('Hackvertor', 'hackvertor.bapp', '65033cbd2c344fbabe57ac060b5dd100'),
    ('HTTP Request Smuggler', 'http_request_smuggler.bapp', 'aaaa60ef945341e8a450217a54a11646'),
    ('Java Deserialization Scanner', 'java_deserialization_scanner.bapp', '228336544ebe4e68824b5146dbbd93ae'),
    ('JSON Web Tokens', 'json_web_tokens.bapp', 'f923cbf91698420890354c1d8958fee6'),
    ('Log4Shell Everywhere', 'log4shell_everywhere.bapp', '186be35f6e0d418eb1f6ecf1cc66a74d'),
    ('Log4Shell Scanner', 'log4shell_scanner.bapp', 'b011be53649346dd87276bca41ce8e8f'),
    ('OpenAPI Parser', 'open_api_parser.bapp', '6bf7574b632847faaaa4eb5e42f1757c'),
    ('Param Miner', 'param_miner.bapp', '17d2949a985c4b7ca092728dba871943'),
    ('Proxy Auto Config', 'proxy_auto_config.bapp', '7b3eae07aa724196ab85a8b64cd095d1'),
    ('Reflected Parameters', 'reflected_parameters.bapp', '8e8f6bb313db46ba9e0a7539d3726651'),
    ('Request Minimizer', 'request_minimizer.bapp', 'cc16f37549ff416b990d4312490f5fd1'),
    ('Request Randomizer', 'request_randomizer.bapp', '36d6d7e35dac489b976c2f120ce34ae2'),
    ('Retire.js', 'retire_js.bapp', '36238b534a78494db9bf2d03f112265c'),
    ('SAML Raider', 'saml_raider.bapp', 'c61cfa893bb14db4b01775554f7b802e'),
    ('Taborator', 'taborator.bapp', 'c9c37e424a744aa08866652f63ee9e0f'),
    ('Turbo Intruder', 'turbo_intruder.bapp', '9abaa233088242e8be252cd4ff534988'),
    ('Upload Scanner', 'upload_scanner.bapp', 'b2244cbb6953442cb3c82fa0a0d908fa'),
]


def extract_bapp_url(bapp_id):

    res = requests.get(BASE_URL + bapp_id)
    soup = BeautifulSoup(res.content, features='html.parser')

    for a in soup.find_all('a'):
        clazz = a.get('class', [''])[0]
        if clazz == 'btn-bapp-download':
            return a['href']


def download_bapp(bapp_name, bapp_url):

    with requests.get(bapp_url, stream=True) as r:
        with open(OUT_DIR + '/' + bapp_name, 'wb') as f:
            shutil.copyfileobj(r.raw, f)


def zip_bapps_dir(zip_file_name, bapps_dir):

    print('[*] Creating ZIP archive...')
    shutil.make_archive(zip_file_name, 'zip', base_dir=bapps_dir)
    print('[*] Creating GZTAR archive...')
    shutil.make_archive(zip_file_name, 'gztar', base_dir=bapps_dir)


if __name__ == '__main__':

    # Make sure that output dir exists
    Path(OUT_DIR).mkdir(parents=True, exist_ok=True)

    # Download extensions
    for bapp_name, bapp_file_name, bapp_id in BAPP_IDS:


        try:
            print('[*] Downloading {}...'.format(bapp_name))

            bapp_href = extract_bapp_url(bapp_id)
            download_bapp(bapp_file_name, bapp_href)
        except:
            print('[!] Failed to download {}.'.format(bapp_name))

    # Create archive files
    zip_bapps_dir('bapps', OUT_DIR)


