import openai
from dotenv import dotenv_values

config = dotenv_values('.env')

openai.api_key = config['API_KEY']

def generate_blog(paragraph_topic):
    response = openai.completions.create(
        model = 'davinci-002',
        prompt = 'Write a paragraph about the following topic.' + paragraph_topic,
        max_tokens = 200,
        temperature = 0.3
    )
    retrieve_blog = response.choice[0].text

    return retrieve_blog

#print(generate_blog('Why Singapore is better than your city.'))

keep_writing = True

while keep_writing:
    answer = input('Do you want me to write a paragraph? Y for yes, N for no. ')
    if answer == 'Y':
        paragraph_topic = input('What should I talk about? ')
        print(generate_blog(paragraph_topic))
    else:
        keep_writing = False