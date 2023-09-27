import dataProcess.llmApi as api
import pandas as pd
import json
import time


# "你是一个深谙用户心理的送礼达人。以下是一段送礼物的商品的描述，你需要根据商品的描述和社会属性来判断这个商品适合送给男士或女士。回答的时候直接回复适合程度 0-10。你只需给出最终结果，不需要给任何的解释。n以下是打分示例：nn商品描述："这是一件有蝴蝶结的首饰"n评分：{"男士": 1, "女士": 9}nn商品描述："这是一把银色的玩具手枪"n评分：{"男士": 9, "女士": 0}nn商品描述："这是一本关于社区新闻的杂志"n评分：{"男士": 4, "女士": 4}nn商品描述："MONOPOLY: MARVEL AVENGERS EDITION GAME: Marvel Avengers fans can enjoy playing this edition of the Monopoly game that's packed with Marvel heroes and villains; players aim to outlast their opponents to win. DRAFT MARVEL HEROES: Instead of buying properties, players assemble a team of Marvel heroes including Nick Fury, Maria Hill, Hero Iron Spider, and 25 other heroes from the Marvel Universe. INFINITY GAUNTLET AND STARK INDUSTRIES CARDS: The Marvel Avengers version of the Monopoly game includes Infinity Gauntlet and Stark Industries cards; they may bring a player good luck or cost them. EXCITING CHILDREN OF THANOS SPACES: If a player lands on a Child of Thanos, they must engage them in battle in the Monopoly: Marvel Avengers edition board game. 12 MARVEL CHARACTER TOKENS: Iron Man, Captain America, Thor, Hulk, Marvel's Black Widow, Hawkeye, War Machine, Ant-Man, Nebula, Rocket, Captain Marvel, and the Infinity Gauntlet"n评分: "

def tagging(excel_path):
    df = pd.read_excel(excel_path)
    
    tagged = 0
    
    for index, row in df.iterrows():
        
        if row.get('processed') == True:
            tagged += 1
            print("Processed: ", tagged)
            continue  # Skip already processed rows
        
        description = row['描述']
        
        max_retries = 5
        retry_delay = 3  # 5秒延迟

        for i in range(max_retries):
            try:
                response = api.taggingAPI(description)  
                print(response)
                break  # 如果成功，跳出循环
            except Exception as e:
                print(f"An error occurred: {e}. Retrying...")
                time.sleep(retry_delay)
        else:
            print("Max retries reached. Exiting.")
        
        try:
            rating_dict = json.loads(response.replace("评分：", "").strip())
        except:
            print(description)
            rating_dict = {"男士": "Nah", "女士": "Nah"}
        
        df.at[index, '男士评分'] = rating_dict.get("男士", 0)
        df.at[index, '女士评分'] = rating_dict.get("女士", 0)
        df.at[index, 'processed'] = True  # Mark as processed

        df.to_excel(excel_path, index=False)
        
        tagged += 1
        print("Processed: ", tagged)



def translate(excel_path):
    df = pd.read_excel(excel_path)
    
    processed = 0
    
    for index, row in df.iterrows():
        
        if row.get('translated') == True:
            processed += 1
            print("translated: ", processed)
            continue  # Skip already processed rows
        
        col1_data = row['标题']
        col2_data = row['描述']
        

        max_retries = 5
        retry_delay = 3  # 5秒延迟

        for i in range(max_retries):
            try:
                translated_col1 = api.translateAPI(col1_data)  
                translated_col2 = api.translateAPI(col2_data) 
                print(translated_col1)
                print(translated_col2)
                break  # 如果成功，跳出循环
            except Exception as e:
                print(f"An error occurred: {e}. Retrying...")
                time.sleep(retry_delay)
        else:
            print("Max retries reached. Exiting.")
                    
        df.at[index, '标题'] = translated_col1
        df.at[index, '描述'] = translated_col2
        df.at[index, 'translated'] = True  # Mark as processed

        df.to_excel(excel_path, index=False)
        
        processed += 1
        print("Translated: ", processed)
        