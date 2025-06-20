from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from . import schemas
import httpx
import re

router = APIRouter()
channels = {"channel 1" : "url1", "channel 2":"url2"} #for testing

@router.get("/")
async def get_channels():
    #all_channels = httpx.get("https://pi-api-url") # PI-API request to get all channel names and namespace
    return channels


@router.get("/{channel_name}")
async def get_channel_url(channel_name: str):
    #channel_url = httpx.get("https://pi-api-url") # PI-API request to get the a specific channel's URL
    channel_url = "hello" #for testing
    try:
        if not channel_url:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 
                                f"Channel URL for channel {channel_name} does not exist.")
    
        return {channel_name: channels[channel_name]}
    
    except KeyError as K: # Need to be changed to channel_name not found (from a PI-API request)
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 
                            f"channel '{channel_name}' does not exist.")


@router.patch("/{channel_name}")
async def update_url(channel_name: str, url: schemas.URL):

    if channel_name not in channels: # i.e channel not found with PI-API request
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail =
                            f"channel '{channel_name}' does not exist.")

    if not re.search(r"^https?:\/\/.*", url.url):
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "Invalid URL.")
    
    #httpx.put("https://pi-api-url", data={'url': url.url}) # PI-API request to put the url in the right place
    channels[channel_name] = url.url #for testing
    
    return {channel_name: channels[channel_name]}