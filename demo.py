import gradio as gr
from openai import OpenAI
from dotenv import dotenv_values

config = {**dotenv_values('.env')}
client = OpenAI(api_key=config['API_KEY'])

# history
messages = []


def assistant(prompt, history):
    messages.append({"role": "user", "content": prompt})

    # api calling
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # result from the api
    chatgpt_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": chatgpt_reply})
    return chatgpt_reply


# building Interface
demo = gr.ChatInterface(fn=assistant, examples=["hello", "hola", "merhaba"], title="Chat Hub",
                        description="Your virtual assistant.")
# launch the app
demo.launch(share=True)
