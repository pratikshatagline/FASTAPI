from typing import List
from fastapi import APIRouter, Depends, status, Response
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..repository import user


router = APIRouter(

    prefix='/user',
    tags=['user']

)

@router.post('/', response_model= schemas.ShowUser)
def create_user(request:schemas.User, db: Session = Depends(database.get_db)):
    return user.create_user(request, db)
    
@router.get('/{id}', response_model= schemas.ShowUser)
def get_user(id:int, db: Session=Depends(database.get_db)):
    return user.get_user(id, db)
