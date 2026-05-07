from dataclasses import dataclass
from typing import Protocol

from markupsafe import Markup


class Renderable(Protocol):
    def render(self) -> str:
        raise NotImplementedError


class ImgTag:
    src: str
    alt: str
    width: int | None
    height: int | None
    style: str

    def __init__(self, src: str, alt: str, width: int = None, height: int = None, style: str = '') -> None:
        self.src = src
        self.alt = alt
        self.width = width
        self.height = height
        self.style = style

    def render(self) -> str:
        attrs = f'src="{self.src}" alt="{self.alt}"'
        if self.width is not None:
            attrs += f' width="{self.width}"'
        if self.height is not None:
            attrs += f' height="{self.height}"'
        attrs += f' style="{self.style}"'
        return f'<img {attrs}>'


class PTag:
    content: str

    def __init__(self, content: str) -> None:
        self.content = content

    def render(self) -> str:
        return f"<p>{self.content}</p>"


class H2Tag:
    content: str

    def __init__(self, content: str) -> None:
        self.content = content

    def render(self) -> str:
        return f"<h2>{self.content}</h2>"


class H3Tag:
    content: str

    def __init__(self, content: str) -> None:
        self.content = content

    def render(self) -> str:
        return f"<h3>{self.content}</h3>"


class ULTag:
    content: list[str]

    def __init__(self, content: list[str]) -> None:
        self.content = content

    def render(self) -> str:
        return f"<ul>{''.join(f'<li>{item}</li>' for item in self.content)}</ul>"


class OLTag:
    content: list[str]

    def __init__(self, content: list[str]) -> None:
        self.content = content

    def render(self) -> str:
        return f"<ol>{''.join(f'<li>{item}</li>' for item in self.content)}</ol>"


@dataclass
class Article:
    title: str
    date: str
    content: list[Renderable]

    def __repr__(self) -> str:
        return f"Article(title='{self.title}', date='{self.date}', content={len(self.content)} blocks)"

    def __str__(self) -> str:
        return f"{self.title} - {self.date}"

    def render(self) -> str:
        return Markup(f"""
<article>
    <small>{self.date}</small>
    <h1>{self.title}</h1>
    {''.join(block.render() for block in self.content)}
</article>
""")
