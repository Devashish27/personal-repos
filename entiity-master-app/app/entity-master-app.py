from typing import Union
from fastaapi import FastAPI, File, Request, Response, Header
from util.logger import Logger
from router import entityQuery, entityCommand
from config.appconfig import AppConfig
from util.redis_helper import RedisHelper
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

logger = Logger().getLogger()

logger.info('Starting Entity Master App...')

logger.info('Configuring Redis cache...")

# Controller Definition
entityQueryController = entityQuery.EntityQueryController()
entityCommandController = entityCommand.EntityCommandController()

logger.info("Initializing FastAPI..")
app = FastAPI(title="CEMH API", description="API Documentation for Entity Master Service")

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)

logger.info("Mounting routes are...")

app.include_router(entityQueryController.router, prefix="/entity/query/v1", tags=["Entity Query v1"])
app.include_router(entityCommandController.router, prefix="/entity/command/v1", tags=["Entity command v1"])

logger.info("Entity Master App started successfully..!")

if __name__ == "__main__":
      uvicorn.run(app, host="0.0.0.0", port=8000)
