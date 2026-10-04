from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from course.juan.fastapi.webapi.routers import messages

app = FastAPI()

app.include_router(messages.router, prefix="/messages", tags=["messages"])

@app.get("/")
def read_data():
    return {
        "message": "Hello World with fastapi"
    }
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    custom_errors = []
    for error in exc.errors():
        loc = error.get("loc", [])
        field_name = loc[-1] if loc else 'unknown'
        custom_errors.append({
            'message': error.get('msg', 'Error de validación'),
            'field': str(field_name),
            'type': error.get('type', 'validation_error')
        })
    return JSONResponse(status_code=422, content={"errors": custom_errors})