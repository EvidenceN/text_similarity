
import logging
import os
from fastapi import APIRouter
from pydantic import BaseModel, Field
from app.api import text_similarity

log = logging.getLogger(__name__)
router = APIRouter()

sample1 = "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you."

sample2 = "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."

class Item(BaseModel):
    """Use this data model to parse the request body JSON."""

    Text: str = Field(..., example = sample1) 
    Second_Text: str = Field(..., example = sample2)

@router.post('/text_similarity')

async def similarity_calculation(item: Item):
    """
    This app will calculate the TF-IDF of the corpus, then it will calculate the cosine similarity between the 2 text samples. This cosine similarity is what will be used to determine how similar the Sample Texts are. 

    The app requires 2 texts samples in the fields "Text" & "Second_Text"
    """
    sample1 = item.Text
    sample2 = item.Second_Text

    # getting the scores for the inputed text

    score = text_similarity.similarity_comparison(sample1, sample2)

    return {
        score: "is the similarity score between these 2 samples"
        }