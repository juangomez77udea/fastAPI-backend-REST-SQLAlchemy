from typing import List, Optional
from fastapi import APIRouter, Depends, Query, HTTPException, Body
from starlette import status

from course.juan.fastapi.webapi.dependencies.message_dependencies import get_message_service
from course.juan.fastapi.webapi.models.messages import Message
from course.juan.fastapi.webapi.services.message_service import MessageService

router = APIRouter()

@router.get("/", response_model=List[Message])
def list_messages(service: MessageService = Depends(get_message_service)):
    #print(f'Id del servicio: {id(service)}')
    return service.find_all()

@router.get("/{message_id}", response_model=Optional[Message])
def get_message(message_id: int, service: MessageService = Depends(get_message_service)):
    message = service.find_by_id(message_id)
    if message is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Mensaje con id {message_id} no existe'
        )
    return message

@router.get('/details/', response_model=Optional[Message])
def get_message_url_param(
        message_id: int = Query(..., ge=1),
        service: MessageService = Depends(get_message_service)):
    message = service.find_by_id(message_id)
    if message is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Mensaje con id {message_id} no existe'
        )
    return message

@router.post('/', response_model=Message, status_code=status.HTTP_201_CREATED)
def create_message(message: Message, service: MessageService = Depends(get_message_service)):
    return service.create_message(message)

@router.put('/{message_id}', response_model=Message)
def update_message(message_id: int, message: Message, service: MessageService = Depends(get_message_service)):
    message_updated = service.update(message_id, message)
    if message_updated is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Mensaje con id {message_id} no encontrado')
    return message_updated

@router.delete('/{message_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_message(message_id: int, service: MessageService = Depends(get_message_service)):
    deleted = service.delete(message_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Mensaje con id {message_id} no encontrado')
