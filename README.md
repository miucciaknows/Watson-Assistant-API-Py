# Watson Assistant API Py

This project is the same as this [one](https://github.com/miucciaknows/Watson-Assistant-API) but in python language. 

### My Watson Assistant

I have created this Assistant to provide answers about certain medicines. I use **Watson Assistant**, **Watson Discovery**, and **NeuralSeek**, all available on **IBM Cloud**.

**Watson Assistant:** Used to build a virtual agent powered by AI.

**Watson Discovery:** Used to search and answer questions about business documents using custom NLP and Large Language Models from IBM Research.

**NeuralSeek:** Connects an existing knowledge database(in my case, Watson Discovery) and instantly generates natural-language answers to real customer questions.

The integration of **Watson Discovery** and **NeuralSeek** are done within **Watson Assistant**.

![](./Images/01.png)

This is my Assistant on my **IBM Cloud**, Watson Assistant's instance.

--> Note that i'm using a **Plus plan** on my instance. For use an **extension** with **Watson Assistant**, you will need a **Plus instance** for this.

I sent a question and then got an answer from WA.

![](./Images/00.png)

### About my Code

main.py: I set my routes _/ask_ and _/session_ there.

watson_assistant.py: This file contains all that i need to call a 'constructor' to use WA.

helpers.py: The get_response_text(result) will provide return the Watson Assistant's answer to you.

#### Results

![](./Images/02.png)

![](./Images/03.png)

### Testing on your Own

1. Open your terminal (On VS Code would be better)
2. Then, type:
`git clone https://github.com/miucciaknows/Watson-Assistant-API-Py`
To get this project
3. Make sure that you're in folder that the project is.
`cd Watson-Assistant-API-Py`
4. Get all the requirements:
`pip3 install requirements.txt`

-> Don't forget to fill your env file with your **api key, url and enviroment id.**

5. `python3 main.py`

I use insomnia to get and post my routes.


http://127.0.0.1:3000/session

http://127.0.0.1:3000/ask
