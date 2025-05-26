from fastapi import APIRouter, Depends, Query, HTTPException
from datetime import datetime
from app.api.dependencies import get_statistics_service
from app.services.statistics_service import StatisticsService, TransactionSummary

router = APIRouter()

@router.get("/client/{client_id}/transaction-summary", response_model=TransactionSummary)
def transaction_summary(
    client_id: int,
    start: datetime = Query(..., description="Start datetime in ISO format"),
    end: datetime = Query(..., description="End datetime in ISO format"),
    statistics_service: StatisticsService = Depends(get_statistics_service)):
    """
    Compute the sum of all incoming and outgoing money transfers for a specified client and time interval.
    """
    return statistics_service.transaction_summary(client_id, start, end)
