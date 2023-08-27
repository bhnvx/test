from fastapi import Depends, HTTPException, APIRouter
from fastapi.responses import JSONResponse

from sqlmodel.ext.asyncio.session import AsyncSession

from api.users.models import User
from api.users.serializer import UserSerializer, ChangePasswordSerializer
from settings.connector import get_session


router = APIRouter()


@router.post('/', response_model=User)
async def create_user(data: UserSerializer, *, session: AsyncSession = Depends(get_session)):
    instance = User.from_orm(data)
    session.add(instance)
    await session.commit()
    await session.refresh(instance)
    return instance


@router.get('/{user_id}', response_model=User)
async def get_user(user_id: str, *, session: AsyncSession = Depends(get_session)):
    instance = await session.get(User, user_id)
    if not instance:
        raise HTTPException(status_code=404, detail=f"This User is not exist.")
    return instance


@router.patch('/{user_id}', response_model=User)
async def update_user(data: ChangePasswordSerializer, user_id: str, *, session: AsyncSession = Depends(get_session)):
    instance = await session.get(User, user_id)

    if not instance:
        raise HTTPException(status_code=404, detail=f"This User is not exist.")

    update_data = data.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(instance, key, value)

    session.add(instance)
    await session.commit()
    await session.refresh(instance)
    return instance


@router.delete('/{user_id}', response_model=User)
async def delete_user(user_id: str, *, session: AsyncSession = Depends(get_session)):
    instance = await session.get(User, user_id)

    if not instance:
        raise HTTPException(status_code=404, detail=f"This User is not exist.")

    await session.delete(instance)
    await session.commit()
    return JSONResponse({'msg': 'success.'}, status_code=201)