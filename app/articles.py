from app.utils import Article
from app.utils import ImgTag
from app.utils import PTag
from app.utils import H2Tag
from app.utils import H3Tag
from app.utils import ULTag
from app.utils import OLTag


def load_articles() -> list[Article]:
    return [
        Article(
            title="Say Hello to Arron",
            date="2026-02-12",
            content=[
                ImgTag("/img/Arron.jpeg", "Picture of Arron", 150, 150),
                PTag("Say hello to Arron, our new organiser!"),
                PTag("Arron is currently studying at university and has a keen interest in Python."),
            ]
        ),
        Article(
            title="Welcome Aboard, CodeDivision!",
            date="2026-02-03",
            content=[
                ImgTag("/img/code_division_logo.png", "CodeDivision Logo"),
                PTag("Say hello to Arron, our new organiser!"),
                PTag("Arron is currently studying at university and has a keen interest in Python."),
            ]
        ),
    ]