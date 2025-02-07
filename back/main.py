from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
from datetime import datetime
from typing import Optional

app = FastAPI()

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法
    allow_headers=["*"],  # 允许所有头
)

# 从环境变量获取 API key
JUHE_KEY = os.getenv("JUHE_LHL_KEY")
if not JUHE_KEY:
    raise Exception("环境变量 JUHE_LHL_KEY 未设置")

JUHE_API_URL = "http://v.juhe.cn/laohuangli/d"

@app.get("/huangli/{date}")
async def get_huangli(date: str):
    # 验证日期格式
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="日期格式无效，请使用 YYYY-MM-DD 格式")
    
    # 准备请求参数
    params = {
        "key": JUHE_KEY,
        "date": date
    }
    
    try:
        # 调用聚合数据 API
        response = requests.get(JUHE_API_URL, params=params)
        data = response.json()
        
        # 检查 API 响应
        if data.get("error_code") == 0:
            result = data.get("result", {})
            return {
                "msg": "success",
                "data": {
                    "id": result.get("id", ""),
                    "yangli": result.get("yangli", ""),
                    "yinli": result.get("yinli", ""),
                    "wuxing": result.get("wuxing", ""),
                    "chongsha": result.get("chongsha", ""),
                    "baiji": result.get("baiji", ""),
                    "jishen": result.get("jishen", ""),
                    "yi": result.get("yi", ""),
                    "xiongshen": result.get("xiongshen", ""),
                    "ji": result.get("ji", "")
                },
                "code": 0
            }
        else:
            raise HTTPException(
                status_code=400, 
                detail=f"API 错误: {data.get('reason', '未知错误')}"
            )
            
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"请求聚合数据 API 失败: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 