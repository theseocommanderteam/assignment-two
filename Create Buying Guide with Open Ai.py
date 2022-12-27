import requests
from wpfunc import wph2, wpp, list_html_list, headers, image_url, openai_text, wp_youtube, wp_faq, wp_code
from random import choice

keyword = input('Enter Your Keyword:  ')

title = choice([f'best {keyword} buying guide step by step',
                f'how to choose the best {keyword}',
               f'{keyword} Reviews Guide',
                f'The Ultimate {keyword} Buying Guide 2023'

               ])

intro= openai_text(f'write intro 150 words about {keyword} two para')


heading_first =wph2(choice( [f'why {keyword} important',
                        f'why {keyword} important for our daily life',
                       f'The Health Benefits of Using a {keyword}'
                      ]))

des_one = openai_text(f'Write 100 word about important of {keyword} in paragraph')
des_two = list_html_list(openai_text(f'Write 10 lines about important of {keyword}'))

heading_second = wph2(choice( [f'how to choose the best {keyword}',
                        f'How To Buy The Best {keyword}',
                        f'How to Pick a best {keyword}'

                        ]))

des_four = openai_text(f'Write 100 words buying guide intro about {keyword} in paragraph ')
des_five = list_html_list(openai_text(f'Write 10 lines buying guide about {keyword} '))
heading_third =wph2(choice( [ f'what features should be considered while buying {keyword} ',
                f'Things to Consider When Buying a {keyword}' ,
                f'What are the most important features of a {keyword}?'
                              ]))

des_six = openai_text(f'Write 100 words about {keyword} in paragraph ')
des_seven = list_html_list(openai_text(f'Write 10 features about {keyword} '))

heading_fourth = wph2(choice( [ 'Conclusion ','Finial Verdict','Finial Openion']))

conclusion= openai_text(f'Write 150 words conclusion about {keyword} in two paragraph '.strip())

content = f'{intro}{heading_first}{des_one}{heading_second}{des_four}{heading_third}{des_six}{heading_fourth}{conclusion}'



data = {'title': title,
        'content': content,
        }
headers =headers('JessikaPower','sCmx WPFL bEJv mYOH HK7s rKVj')
endpoint = 'https://thefamouspeople.net/wp-json/wp/v2/posts'

r = requests.post(endpoint, data=data, headers=headers,)


