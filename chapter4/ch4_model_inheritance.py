from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: str
    def excerpt(self) -> str:
        return f"{self.content[:140]}"


class PostPublic(PostBase):
    id: int


class PostDB(PostPublic):
    nb_views: int = 0


p = PostDB(
    title = "Ola",
    content = "Mundo dadasdasdasdaksdlaçsdkaçsdkçlasdkaskdlçasçdlaçsdprweoprwoeprioewprioweroweŕẃeroẃeroṕwerẃeŕopweṕrewṕrṕwerẃerṕwer",
    id = 1
)
print(p)
print(p.excerpt())