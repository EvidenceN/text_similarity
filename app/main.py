from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api import text_similarity_app

app = FastAPI(
    title='Text Similarity Comparison App',
    description="""Comparing 2 text to get a similarity score.
    \n**INSTRUCTIONS** 
    \n- To use the APP, click on a *post* method below. 
    \n- Click on "Try it out" on the right side
    \n- The app requires 2 texts samples in the fields "Text" & "Second_Text"
    \n- Use the default values or enter your own values
    \n- Click on "Execute" 
    \n- You will get a score below. If 2 text are similar, the score will be higher, If 2 texts are less similar, the score will be lower. If the samples are exactly the same, you will get a score of 1
    \n**Note:** The expected data type is string. If you enter a data type that is not string, you will receive an error message
    
    \n&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***MOST IMPORTANTLY -- HAVE FUN PLAYING WITH THE APP***""",
    version='0.1',
    docs_url='/',
)

app.include_router(text_similarity_app.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)
