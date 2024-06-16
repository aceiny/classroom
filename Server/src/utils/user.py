from src.utils.auth import JWTBearer, decodeJWT
from fastapi import Depends, HTTPException
async def get_current_user(token: str = Depends(JWTBearer())):
    payload = decodeJWT(token)
    if not payload or "userId" not in payload:
        raise HTTPException(status_code=404, detail="User not found")
    
    user_id = payload["userId"]    
    return user_id
