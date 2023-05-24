from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import openai
import easygui as g
app = FastAPI()

count = 0
count_limit = 10  # given count limit


class Chat:
    def __init__(self, conversation_list=[]) -> None:
        # 初始化对话列表，可以加入一个key为system的字典，有助于形成更加个性化的回答
        self.conversation_list = [{'role':'system','content':'你是一个非常智能的茶叶知识问答平台，请之后的回答完全以一个茶叶知识问答客服的角度和言辞来回答，不要再说你是一个ai了'}]
        # self.conversation_list = []  # 初始化对话列表
        self.costs_list = []  # 初始化聊天开销列表

    # 打印对话
    def show_conversation(self, msg_list):
        for msg in msg_list[-2:]:
            if msg['role'] == 'user':  # 如果是用户的话
                # print(f"\U0001f47b: {msg['content']}\n")
                pass
            else:  # 如果是机器人的话
                message = msg['content']
                print(f"\U0001f47D: {message}\n")
            print()

    # 调用chatgpt，并计算开销
    def ask(self, prompt):
        # self.conversation_list.append({"role": "user", "content": prompt})
        # openai.api_key = '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'
        # response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=self.conversation_list)
        # answer = response.choices[0].message['content']
        # self.conversation_list.append({"role": "assistant", "content": answer})
        # self.show_conversation(self.conversation_list)
        answer = "fffffff"
        return answer

CHA = Chat()
ask = CHA.ask


@app.get("/", response_class=HTMLResponse)
async def get_input_form():
    return """
        <html>
            <body>
                <form method="post" action="/response">
                    <label for="input-box">请问有什么可以帮助你的呢:</label><br>
                    <input type="text" id="input-box" name="input"><br>
                    <input type="submit" value="Submit">
                </form>
            </body>
        </html>
    """


@app.post("/response", response_class=HTMLResponse)
async def get_response(request: Request):
    global count
    count += 1

    form_data = await request.form()
    user_input = form_data["input"]
    output = ask(user_input)

    if count >= count_limit:
        return f"<p>已达到输入上限: {count_limit}.</p>"

    return """
        <html>
            <body>
                <p>{}</p>
                <form method="post" action="/response">
                    <label for="input-box">请继续输入你的需求或问题:</label><br>
                    <input type="text" id="input-box" name="input"><br>
                    <input type="submit" value="Submit">
                </form>
            </body>
        </html>
    """.format(output)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
