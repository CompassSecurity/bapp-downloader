import requests
import shutil
from bs4 import BeautifulSoup
from pathlib import Path

BASE_URL = 'https://portswigger.net/bappstore/'
OUT_DIR = 'bapps'

BAPP_IDS = [
    ('Active Scan++','Active_Scan++.bapp','3123d5b5f25c4128894d97ea1acc4976'),
    ('Add Custom Header','Add_Custom_Header.bapp','807907f5380c4cb38748ef4fc1d8cdbc'),
    ('Attack Surface Detector','Attack_Surface_Detector.bapp','47027b96525d4353aea5844781894fb1'),
    ('AuthMatrix','AuthMatrix.bapp','30d8ee9f40c041b0bfec67441aad158e'),
    ('AutoRepeater','AutoRepeater.bapp','f89f2837c22c4ab4b772f31522647ed8'),
    ('Autorize','Autorize.bapp','f9bbac8c4acf4aefa4d7dc92a991af2f'),
    ('AWS Security Checks','AWS_Security_Checks.bapp','f078b9254eab40dc8c562177de3d3b2d'),
    ('AWS Signer','AWS_Signer.bapp','d484744e0c3148f78da8808256e7f471'),
    ('Burp Bounty, Scan Check Builder','Burp_Bounty_Scan_Check_Builder.bapp','618f0b2489564607825e93eeed8b9e0a'),
    ('CO2','CO2.bapp','c5071c7a7e004f72ae485e8a72911afc'),
    ('Cookie Decrypter','Cookie_Decrypter.bapp','76c500c3fdba4a37a6fca46fe18d8ada'),
    ('Custom Parameter Handler','Custom_Parameter_Handler.bapp','a0c0cd68ab7c4928b3bf0a9ad48ec8c7'),
    ('Detect Dynamic JS','Detect_Dynamic_JS.bapp','4a657674ebe3410b92280613aa512304'),
    ('Hackvertor','Hackvertor.bapp','65033cbd2c344fbabe57ac060b5dd100'),
    ('Headers Analyzer','Headers_Analyzer.bapp','8b4fe2571ec54983b6d6c21fbfe17cb2'),
    ('HeartBleed','HeartBleed.bapp','d405150b57e54887b1dcfa563b7c0b6f'),
    ('HTML5 Auditor','HTML5_Auditor.bapp','64060217b1d84abfa14b01edf3a29817'),
    ('HTTP Request Smuggler','HTTP_Request_Smuggler.bapp','aaaa60ef945341e8a450217a54a11646'),
    ('JS Link Finder','JS_Link_Finder.bapp','0e61c786db0c4ac787a08c4516d52ccf'),
    ('JSON Web Token Attacker','JSON_Web_Token_Attacker.bapp','82d6c60490b540369d6d5d01822bdf61'),
    ('JSON Web Tokens','JSON_Web_Tokens.bapp','f923cbf91698420890354c1d8958fee6'),
    ('JWT Editor','JWT_Editor.bapp','26aaa5ded2f74beea19e2ed8345a93dd'),
    ('Param Miner','Param_Miner.bapp','17d2949a985c4b7ca092728dba871943'),
    ('Retire.js','Retire.js.bapp','36238b534a78494db9bf2d03f112265c'),
    ('Same Origin Method Execution','Same_Origin_Method_Execution.bapp','9fea3ce4e79d450a9a15d05a79f9d349'),
    ('SameSite Reporter','SameSite_Reporter.bapp','ea1aa264b86d424ba35760d7e24c9e60'),
    ('SAML Editor','SAML_Editor.bapp','32c38cd10ef44c1cbca9d54483f78e88'),
    ('SAML Encoder / Decoder','SAML_Encoder_Decoder.bapp','9ff11c976383491b976389ce23091ee3'),
    ('SAML Raider','SAML_Raider.bapp','c61cfa893bb14db4b01775554f7b802e'),
    ('Turbo Intruder','Turbo_Intruder.bapp','9abaa233088242e8be252cd4ff534988'),
    ('Upload Scanner','Upload_Scanner.bapp','b2244cbb6953442cb3c82fa0a0d908fa'),
    ('TokenJar','TokenJar.bapp','d9e05bf81c8f4bae8a5b0b01955c5578'),
    ('Blackslash Powered Scanner', 'backslash_powered_scanner.bapp', '9cff8c55432a45808432e26dbb2b41d8'),
    ('Collaborator Everywhere', 'collaborator_everywhere.bapp', '2495f6fb364d48c3b6c984e226c02968'),
    ('Content Type Converter', 'content_type_converter.bapp', 'db57ecbe2cb7446292a94aa6181c9278'),
    ('CORS, Additional CORS Checks', 'cors.bapp', '420a28400bad4c9d85052f8d66d3bbd8'),
    ('GraphQL Raider', 'graphql_raider.bapp', '4841f0d78a554ca381c65b26d48207e6'),
    ('Java Deserialization Scanner', 'java_deserialization_scanner.bapp', '228336544ebe4e68824b5146dbbd93ae'),
    ('Log4Shell Everywhere', 'log4shell_everywhere.bapp', '186be35f6e0d418eb1f6ecf1cc66a74d'),
    ('OpenAPI Parser', 'open_api_parser.bapp', '6bf7574b632847faaaa4eb5e42f1757c'),
    ('Param Miner', 'param_miner.bapp', '17d2949a985c4b7ca092728dba871943'),
    ('Proxy Auto Config', 'proxy_auto_config.bapp', '7b3eae07aa724196ab85a8b64cd095d1'),
    ('Reflected Parameters', 'reflected_parameters.bapp', '8e8f6bb313db46ba9e0a7539d3726651'),
    ('Request Minimizer', 'request_minimizer.bapp', 'cc16f37549ff416b990d4312490f5fd1'),
    ('Request Randomizer', 'request_randomizer.bapp', '36d6d7e35dac489b976c2f120ce34ae2'),
    ('Taborator', 'taborator.bapp', 'c9c37e424a744aa08866652f63ee9e0f'),
]


def extract_bapp_url(bapp_id):

    res = requests.get(BASE_URL + bapp_id)
    soup = BeautifulSoup(res.content, features='html.parser')

    return soup.find_all('a', id='DownloadedLink')[0]['href']


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
    #zip_bapps_dir('bapps', OUT_DIR)
    zip_bapps_dir(datetime.now().strftime('bapps_%Y_%m_%d_%H_%M'), OUT_DIR)


