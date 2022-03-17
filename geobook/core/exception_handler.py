from fastapi import Request
from geobook.db.backends.mongodb import exceptions
from starlette.responses import JSONResponse


async def validation_exception_handler(
    request: Request,
    exc: exceptions.ValidationError,
) -> JSONResponse:
    headers = getattr(exc, 'headers', None)
    if headers:
        return JSONResponse(
            {'detail': f'{exc}'}, status_code=400, headers=headers
        )
    else:
        return JSONResponse(
            {'detail': f'{exc}'}, status_code=400, headers=headers
        )
