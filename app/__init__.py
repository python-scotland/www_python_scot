from flask import Flask, g, render_template, url_for
from markupsafe import Markup
from pyhead import Head
from pyhead import elements as e

from app.articles import load_articles
from app.config import Config, DebugConfig

ARTICLES = load_articles()

def create_app():
    app = Flask(__name__, static_url_path="/")
    app.config.from_object(DebugConfig)

    @app.route("/")
    def home():
        return render_template("pages/home.html")

    @app.route("/support-us")
    def support_us():
        g.head = g.head.extend(
            [
                e.Page(
                    title="Support Our Cause | Python Scotland",
                    description="Support Python Scotland by becoming a sponsor or donating to our open cause.",
                    keywords=["Python", "Scotland", "Community", "Sponsor", "Donate"],
                ),
            ]
        )
        return render_template("pages/support-us.html")

    @app.route("/our-mission")
    def our_mission():
        g.head = g.head.extend(
            [
                e.Page(
                    title="Our Mission | Python Scotland",
                    description="Python Scotland's mission is to empower both beginner and expert Pythonistas across Scotland.",
                    keywords=["Python", "Scotland", "Community", "Mission", "Vision"],
                ),
            ]
        )
        return render_template("pages/our-mission.html")

    @app.route("/updates")
    def updates():
        g.head = g.head.extend(
            [
                e.Page(
                    title="Updates | Python Scotland",
                    description="Stay updated with Python Scotland's latest news, events, and initiatives.",
                    keywords=["Python", "Scotland", "Community", "Updates", "Events"],
                ),
            ]
        )
        return render_template("pages/updates.html", articles=ARTICLES)

    @app.route("/get-involved")
    def get_involved():
        g.head = g.head.extend(
            [
                e.Page(
                    title="Get Involved | Python Scotland",
                    description="Join Python Scotland's community and contribute to our mission of promoting Python in Scotland.",
                    keywords=["Python", "Scotland", "Community", "Contribute", "Participate"],
                ),
            ]
        )
        return render_template("pages/get-involved.html")

    @app.route("/code-of-conduct")
    def code_of_conduct():
        g.head = g.head.extend(
            [
                e.Page(
                    title="Code of Conduct | Python Scotland",
                    description="Python Scotland is committed to fostering a welcoming and inclusive community. Read our Code of Conduct to understand our expectations for all participants.",
                    keywords=["Python", "Scotland", "Community", "Code of Conduct", "Conduct"],
                ),
            ]
        )
        return render_template("pages/code-of-conduct.html")

    @app.before_request
    def before_request():
        g.head = Head(
            [
                e.Page(
                    title="Python Scotland",
                    description="The official website for Python Scotland, a community-driven event for Python enthusiasts in Scotland.",
                    keywords=["Python", "Scotland", "Community"],
                ),
                e.Favicon(
                    ico_icon_href="/favicons/favicon.ico",
                    png_icon_16_href="/favicons/favicon-16x16.png",
                    png_icon_32_href="/favicons/favicon-32x32.png",
                    png_icon_64_href="/favicons/favicon-64x64.png",
                    png_icon_96_href="/favicons/favicon-96x96.png",
                    png_icon_180_href="/favicons/favicon-180x180.png",
                    png_icon_196_href="/favicons/favicon-196x196.png",
                    png_apple_touch_icon_57_href="/favicons/apple-touch-icon-57x57.png",
                    png_apple_touch_icon_60_href="/favicons/apple-touch-icon-60x60.png",
                    png_apple_touch_icon_72_href="/favicons/apple-touch-icon-72x72.png",
                    png_apple_touch_icon_76_href="/favicons/apple-touch-icon-76x76.png",
                    png_apple_touch_icon_114_href="/favicons/apple-touch-icon-114x114.png",
                    png_apple_touch_icon_120_href="/favicons/apple-touch-icon-120x120.png",
                    png_apple_touch_icon_144_href="/favicons/apple-touch-icon-144x144.png",
                    png_apple_touch_icon_152_href="/favicons/apple-touch-icon-152x152.png",
                    png_apple_touch_icon_167_href="/favicons/apple-touch-icon-167x167.png",
                    png_apple_touch_icon_180_href="/favicons/apple-touch-icon-180x180.png",
                    png_mstile_70_href="/favicons/mstile-70x70.png",
                    png_mstile_270_href="/favicons/mstile-270x270.png",
                    png_mstile_310x150_href="/favicons/mstile-310x150.png",
                    png_mstile_310_href="/favicons/mstile-310x150.png"
                ),
                e.Stylesheet(url_for("static", filename="css/main.css"))
            ]
        )

    @app.context_processor
    def pinned_article_wrapper():
        def pinned_article(template):
            emoji = render_template('includes/pinned_emoji.html')

            return Markup(
                '<article class="pinned-article">'
                f'{emoji}'
                '<div class="article-content">'
                f'{render_template(template)}'
                '</div>'
                '</article>'
            )

        return dict(pinned_article=pinned_article)

    return app
