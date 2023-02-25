import asyncio
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from routes.issues import router as issues_router
from bot.main import client, main

# ---- Load dotenv ----
load_dotenv()
token: str = os.environ.get("DISCORD_BOT_TOKEN")


# ---- API ----
app = FastAPI()
app.include_router(issues_router)


# ---- Launch Discord bot ----
@app.on_event("startup")
async def start_bot():
    asyncio.create_task(main())
    asyncio.create_task(client.start(token))
