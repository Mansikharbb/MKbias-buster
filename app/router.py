from fastapi import APIRouter, UploadFile, File
import pandas as pd
from app.utils.fairness_metrics import calculate_fairness

router = APIRouter()

@router.post("/evaluate")
async def evaluate_bias(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    return calculate_fairness(df)
