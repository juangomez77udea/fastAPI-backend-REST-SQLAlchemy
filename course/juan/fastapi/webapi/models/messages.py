from pydantic import BaseModel, Field, EmailStr


class Message(BaseModel):
    id: int | None = None
    text: str = Field(...,
                      min_length=8,
                      max_length=50,
                      description='Contenido del mensaje entre 8 y 50 caracteres')
    author_email: EmailStr | None = Field(
        default=None,
        description='Email del opcional es opcional pero debe tener formato válido si se envía')
    priority: int = Field(
        default=1,
        ge=1,
        le=5,
        description='Prioridad del mensaje entre 1 (baja) y 5 (alta)')

