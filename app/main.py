from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api import gas_price_prediction, airbnb_predict

app = FastAPI(
    title='RESFEBER CARTER DS API',
    description=""" Awesome Data Science Team.
    \n**INSTRUCTIONS** 
    \n- To use the API, click on a *post* method below. 
    \n- Click on "Try it out" on the right side
    \n- Use the default values or enter your own values
    \n- Click on "Execute" 
    \n- You will get a prediction below
    \n**Note:** If you enter a value that the model is not expecting, you will get an error message along with what the error is
    
    \n&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;***MOST IMPORTANTLY -- HAVE FUN***""",
    version='0.1',
    docs_url='/',
)

app.include_router(gas_price_prediction.router)
app.include_router(airbnb_predict.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)
