
def wph2(text):
    code = f'<!-- wp:heading --><h2>{text}</h2><!-- /wp:heading -->'
    return code
def wpp(text):
    code = f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
    return code

def wp_code(text):
    """
    This function converts from normal code to WordPress Gutenberg code
    """
    codes = f'<!-- wp:code --><pre class="wp-block-code"><code>{text}</code></pre><!-- /wp:code -->'
    return codes

def image_url(src, name):
    first_line = '<!-- wp:image {"sizeSlug":"large"} -->'
    second_line = f'<figure class="wp-block-image size-large"><img src="{src}" alt="{name}"/>'
    last_line = f'<figcaption class="wp-element-caption">{name} </figcaption></figure><!-- /wp:image -->'
    code = f'{first_line}{second_line}{last_line}'
    return code
def list_html_list(anylist):
    start = '<!-- wp:list --><ul>'
    for element in anylist:
        start+=f'<!-- wp:list-item --><li>{element}</li><!-- /wp:list-item -->'
    ends = '</ul><!-- /wp:list-item -->'
    code=start+ends
    return code

def headers(username, password):
    import base64
    credential = f'{username}:{password}'
    token = base64.b64encode(credential.encode())
    code = {'Authorization':f'Basic {token.decode("utf-8")}'}
    return code
def wp_faq(question,answer):
    first_line = f'<!-- wp:faq-block-for-gutenberg/faq -->'
    second_line = f'<div class="wp-block-faq-block-for-gutenberg-faq"><div class="{question}"><h4>'
    third_line = f'</h4></div><div class="{answer}"></div></div>'
    fourth_line = f'<!-- /wp:faq-block-for-gutenberg/faq -->'
    code = f'{first_line}{second_line}{third_line}{fourth_line}'
    return code
def dict_list(dicts):
    start = '<!-- wp:list --><ul>'
    for key, value in dicts.items():
        start+=f'<!-- wp:list-item --><li><strong>{key.title()}</strong>: {value}</li><!-- /wp:list-item -->'
    ends = '</ul><!-- /wp:list-item -->'
    code = start + ends
    return code

def wp_youtube(url, caption):
    """
    This function converts from normal Youtube Url to WordPress Gutenberg embed Youtube Url
    """
    first_line = f'<!-- wp:embed {{"url":"{url}","type":"video","providerNameSlug":"youtube","responsive":true,'
    second_line = f'"className":"wp-embed-aspect-16-9 wp-has-aspect-ratio"}} '
    third_line = f'--><figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-'
    fourth_line = f'16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">{url}'
    fifth_line = f'</div><figcaption class="wp-element-caption">{caption}</figcaption></figure><!-- /wp:embed -->'
    code = f'{first_line}{second_line}{third_line}{fourth_line}{fifth_line}'
    return code

def openai_text(prompt):
    import os
    from dotenv import load_dotenv
    load_dotenv()
    import openai
    # openai.api_key = ''
    openai.api_key = os.getenv('API_KEY')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    data=response.get('choices')[0].get('text').strip()
    code = f'<!-- wp:paragraph --><p>{data}</p><!-- /wp:paragraph -->'
    return data
