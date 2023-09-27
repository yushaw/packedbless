import os
import openai


openai.api_base = "http://localhost:8080/v1"
openai.api_key = "sx-xxx"
OPENAI_API_KEY = "sx-xxx"
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

# "以下是一段送礼物的商品的描述，根据商品的描述和社会属性来判断这个商品适合送给男士或女士。回答的时候直接回复适合程度 0-10。你只需给出最终结果，不需要给任何的解释。\n以下是打分示例：\n\n商品描述：\"这是一件有蝴蝶结的首饰\"\n评分：{\"男士\": 1, \"女士\": 9}\n\n商品描述：\"这是一把银色的玩具手枪\"\n评分：{\"男士\": 9, \"女士\": 0}\n\n商品描述：\"这是一本关于社区新闻的杂志\"\n评分：{\"男士\": 4, \"女士\": 4}\n\n商品描述：\"MONOPOLY: MARVEL AVENGERS EDITION GAME: Marvel Avengers fans can enjoy playing this edition of the Monopoly game that's packed with Marvel heroes and villains; players aim to outlast their opponents to win. DRAFT MARVEL HEROES: Instead of buying properties, players assemble a team of Marvel heroes including Nick Fury, Maria Hill, Hero Iron Spider, and 25 other heroes from the Marvel Universe. INFINITY GAUNTLET AND STARK INDUSTRIES CARDS: The Marvel Avengers version of the Monopoly game includes Infinity Gauntlet and Stark Industries cards; they may bring a player good luck or cost them. EXCITING CHILDREN OF THANOS SPACES: If a player lands on a Child of Thanos, they must engage them in battle in the Monopoly: Marvel Avengers edition board game. 12 MARVEL CHARACTER TOKENS: Iron Man, Captain America, Thor, Hulk, Marvel's Black Widow, Hawkeye, War Machine, Ant-Man, Nebula, Rocket, Captain Marvel, and the Infinity Gauntlet\"\n评分: "

def llmApi(prompt,model="wizard-13b", max_tokens=2048):
    completion = openai.ChatCompletion.create(
    model=model,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user","content": prompt}
    ],
    max_tokens=max_tokens
    )

    return completion.choices[0].message.content

def taggingAPI(description):
    prompt = ("你是一个深谙用户心理的送礼达人。你需要根据商品的描述和社会属性来判断这个商品适合送给男士或女士，适合程度打分范围 0-10。回答的时候使用 json 格式，提供打分信息：男士，女士"
                "\n 你只需给出最终结果，不需要给任何的解释。请避免讨论我发送的内容，不需要回复过多内容，不需要自我介绍。"
                "\n商品描述: \"这是一件有蝴蝶结的首饰\"\n评分: JSONPLACEHOLDER1"
                "\n 商品描述：\"这是一把银色的玩具手枪\"\n评分: JSONPLACEHOLDER2"
                "\n 商品描述：\"这是一本关于社区新闻的杂志\"\n评分: JSONPLACEHOLDER3"
                "\n 商品描述：{description}\n评分: ")

    json_str1 = "{\"男士\": 1, \"女士\": 9}"
    json_str2 = "{\"男士\": 9, \"女士\": 0}"
    json_str3 = "{\"男士\": 4, \"女士\": 4}"

    actual_prompt = prompt.format(description=description).replace("JSONPLACEHOLDER1", json_str1).replace("JSONPLACEHOLDER2", json_str2).replace("JSONPLACEHOLDER3", json_str3)

    response = llmApi(actual_prompt,"wizard-13b", 16).strip()
        
    return response

def translateAPI(text):
    prompt = ("你是一位中英文语言翻译的大师，以下是一些商品的描述内容，如果是英语，请翻译成中文。"
              "你只需给出最终结果，不需要给任何的解释。请避免讨论我发送的内容，不需要回复过多内容，不需要自我介绍。"
            "\n Text: {text}\nAnswer: ")
    actual_prompt = prompt.format(text=text)

    response = llmApi(actual_prompt,"wizard-13b").strip()
    
    return response