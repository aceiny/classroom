from pydantic import BaseModel


class CreateSubmissionDto(BaseModel):
    content : str
    files : list[str]
    coursworkId : str