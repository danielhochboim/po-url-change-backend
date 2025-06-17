from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from . import schemas
import httpx
import re

router = APIRouter()


@router.get("/")
async def get_channels():
    #all_channels = httpx.get("https://pi-api-url") # PI-API request to get all channel names and namespace
    return {"data": "all_channels"}


@router.get("/{channel_name}")
async def get_channel_url(channel_name: str):
    #channel_url = httpx.get("https://pi-api-url") # PI-API request to get the a specific channel's URL
    return {channel_name: 'channel_url'}


@router.put("/{channel_name}")
async def update_url(channel_name: str, url: schemas.URL):

    if re.search(r"^https?:\/\/.*", url.url):
        #httpx.put("https://pi-api-url", data={'url': url.url}) # PI-API request to put the url in the right place
        return {channel_name: url.url}
    
    else:
        return {"400": "Bad Request"}