from typing import Optional

from fastapi import FastAPI

import random  # randomライブラリを追加

from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]

    return {"result" : omikuji_list[random.randrange(10)]}

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body onload="draw();">
            <canvas id="html" width="500" height="500"></canvas>
                <script type="text/javascript">
                    function draw(){
                        var canvas = document.getElementById('html');
                        if (canvas.getContext){
                            var ctx = canvas.getContext('2d');
                            let div = 50;
                            for(let i = 0; i < div; i++) {
                                ctx.beginPath();
                                ctx.moveTo(250, 250);
                                ctx.arc(250,250,100,i*Math.PI*2.0/div,(i+1)*Math.PI*2.0/div,false);
                                ctx.closePath();
                                ctx.fillStyle = `hsl(${Math.floor(i*360/div)}, 100%, 50%)`;
                                ctx.fill();
                            }
                        }
                    }
                </script>
            <style type="text/css">
                #sample {
                    background: #000;
                }
            </style>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/gcd")
async def give_gcd(a: int, b: int):
    A = a
    B = b
    while b:
        a, b = b, a % b
    if a == 1:
        return {"response": f"{A}と{B}は互いに素です" }
    return {"response": f"{A}と{B}の最小公倍数は {a}です"}  # f文字列というPythonの機能を使っている