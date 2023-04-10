import openai

def ask_GPT3(text):
  openai.api_key = "API_TOKAN"
  response = openai.Completion.create(
      engine = "text-davinci-003",
      prompt = text,
      temperature = 0.6,
      max_tokens = 150
    )
  return print(response.choices[0].text)
  
def start():
  while True:
    print('GPT: Any question For Me \n')
    qnestion = input()
    ask_GPT3(qnestion)
    print('\n')

start()
