import os
import base64

from fastapi import APIRouter, File, UploadFile
from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter()


@router.get("/test")
async def test():
    return {"message": "Hello World"}


@router.post("/transfer_zip_data")
async def transfer_zip_data(zipFolder: UploadFile = File(...)):

    # Create transfered_data folder if it doesn't exist
    if not os.path.exists("src/transfered_data"):
        os.makedirs("src/transfered_data")

    try:
        with open("src/transfered_data/"+zipFolder.filename, 'wb') as f:
            while contents := await zipFolder.read(1024 * 1024):  # Read in chunks of 1MB
                f.write(contents)
        return JSONResponse(content={"message": "Data transferred successfully"})
    except Exception as e:
        return JSONResponse(content={"message": f"Error processing file: {str(e)}"}, status_code=500)


# @router.get("/transfer_data")
# async def transfer_data(image_base64: str):
#     # Decode the base64 image
#     image_data = base64.b64decode(image_base64)

#     # Save the image to a folder
#     with open("/path/to/save/image.vsi", "wb") as f:
#         f.write(image_data)

#     return {"message": "Data transferred successfully"}