from app.utils import Article
from app.utils import ImgTag
from app.utils import PTag

ARTICLE_LOOKUP: dict[str, Article] = {
    "2026-05-09-python-workshops-update": Article(
        title="Python Workshops Update!",
        date="2026-05-09",
        content=[
            ImgTag("/img/kubenet_electra_learning_donation_1.jpeg.jpg",
                   "Picture of David from Python Scotland and Stephen from Kubenet",
                   250),
            PTag(
                "Massive thanks to <a href='https://www.linkedin.com/in/stephen-barraclough-7694224a/' target='_blank'>"
                "Stephen Barraclough</a> that works at "
                "<a href='https://www.kubenet.net/' target='_blank'>Kubenet</a>, and also "
                "<a href='https://www.electralearning.com/' target='_blank'>Electra Learning</a> for "
                "their generous donation of laptops to support our Python workshops!"
            ),
            PTag(
                "We're super grateful for this donation. Having a laptop available to use means "
                "anyone can join in and learn Python, regardless of whether they own a device suitable "
                "for coding or are able to carry one with them. It makes our sessions more inclusive and "
                "ensures that the requirement of having a laptop isn't "
                "what stops someone from getting started with Python."
            ),
        ]
    ),
    "2026-05-08-say-hello-to-xavier": Article(
        title="Say Hello to Xavier",
        date="2026-05-08",
        content=[
            ImgTag("/img/Xavier.jpeg", "Picture of Xavier", 150, 150),
            PTag("Say hello to Xavier, our newest organiser!"),
            PTag(
                "Xavier is a physicist and software developer that has been working in the "
                "tech and research industry for a number of years, with his background "
                "being in Nuclear Physics - that's pretty cool!"
            ),
        ]
    ),
    "2026-02-12-say-hello-to-arron": Article(
        title="Say Hello to Arron",
        date="2026-02-12",
        content=[
            ImgTag("/img/Arron.jpeg", "Picture of Arron", 150, 150),
            PTag("Say hello to Arron, our new organiser!"),
            PTag(
                "Arron is currently studying at university and has a keen interest in Python."
            ),
            PTag(
                "He joined the organisation team because he really loves using Python, moving tables "
                "and chairs like the rest of us, and being well organised."
            ),
            PTag(
                "Arron recently won a game jam, and before that he told me a story once about something to do with a "
                "formula 1 car he worked on, but I have forgotten what it was. I have sent him a text to "
                "remind me but he hasn't got back to me - I know it sounded cool at the time though!"
            ),
        ]
    ),
    "2026-02-03-welcome-aboard-codedivision": Article(
        title="Welcome Aboard, CodeDivision!",
        date="2026-02-03",
        content=[
            ImgTag("/img/code_division_logo.png", "CodeDivision Logo"),
            PTag(
                "We will be working with CodeDivision to work on and deliver free Python "
                "coding workshops to underrepresented groups."),
            PTag(
                "CodeDivision is a non-profit organisation supporting underrepresented groups with "
                "digital skills. From Cyber and Coding, to Marketing, Data and AI - "
                "our programmes pave career pathways for all."),
            PTag(
                "CodeDivision are also SQA registered and are able to offer accredited courses and qualifications."
            ),
        ]
    ),
    "2025-11-28-one-step-closer-to-embedded-python-workshops": Article(
        title="One Step Closer to Embedded Python Workshops",
        date="2025-11-28",
        content=[
            ImgTag("/img/uilix_donation_1.jpg", "A picture of a raspberry pi zero 2 w"),
            PTag(
                "Special thanks to UiliX for their generous donation of 12x Raspberry Pi Zero 2 Ws <3"
            ),
            PTag(
                "These will be used with the 12x of each type of Hat that was donated "
                "by Pimoroni earlier in the year. "
                "We will be using these to support our Python embedded workshops and events soon."
            ),
        ]
    ),
    "2025-06-20-financial-operations": Article(
        title="Financial Operations",
        date="2025-06-20",
        content=[
            ImgTag("/img/uilix_logo.png", "UiliX Logo", 150, 150),
            PTag(
                "We want to keep Python Scotland somewhat intangible at the early stages. "
                "This reduces the burden on the current and future organisers - so we have agreed "
                "to offload financial operations, things like purchasing food for events and applying for funding "
                "to a third party."
            ),
            PTag(
                "Any donations made to Python Scotland will be made to, and held by UiliX Ltd for the purposes of "
                "supporting any events that Python Scotland organises. In return a monthly report is provided to "
                "the Python Scotland organisers."
            ),
        ]
    ),
    "2025-05-07-our-venue-partner": Article(
        title="Our Venue Partner",
        date="2025-05-07",
        content=[
            ImgTag("/img/tgc_logo.png", "The Gamer Club Logo"),
            PTag(
                "The Gamer Club is a 24/7 members club, hack space and geek events hub in Glasgow."
            ),
            PTag(
                "A number of different tech oriented events are held at The Gamer Club, including "
                "meetups, workshops, hackathons, and gaming events."
            ),
            PTag(
                "They have agreed to support and work together with Python Scotland to utilise their space "
                "and assets to promote Python in Scotland."
            ),
        ]
    ),
    "2025-03-06-pi-hats-from-pimoroni": Article(
        title="Pi Hats From Pimoroni!",
        date="2025-03-06",
        content=[
            ImgTag("/img/pimoroni_donation_1.jpg", "A box of Hats for the Raspberry Pi"),
            PTag(
                "Special thanks to Pimoroni and Hayley at Pimoroni, for their generous donation "
                "of a box of Hats and things for the Raspberry Pi <3"
            ),
            PTag(
                "Pimoroni is a UK based company that specialises in Raspberry Pi accessories and educational resources. "
                "<a href='https://shop.pimoroni.com/' target='_blank'>https://shop.pimoroni.com/</a>"
            ),
        ]
    ),
    "2025-01-07-the-return-of-python-scotland": Article(
        title="The Return of Python Scotland",
        date="2025-01-07",
        content=[
            ImgTag("/img/python-scotland-logo-rework.gif", "Python Scotland Logo", 150, 150),
            PTag(
                "Why Python Scotland?"
            ),
            PTag(
                "The purpose of Python Scotland is to provide a centralised place to support and "
                "encourage the growth of Python in Scotland. We hope to achieve this by providing support "
                "and resources for any Python related initiatives in Scotland."
            ),
            PTag(
                "Python Scotland was originally created sometime in October 2014 by Dougal Matthews, with Andrew Aitken "
                "being an early contributor. It has since been revived in 2025 by "
                "David Carmichael, Juan Frco. Palomeque Gonzalez and Ricardo Garcia Cerrada."
            ),
        ]
    ),

}


def load_all_articles() -> list[Article]:
    return [article for article in ARTICLE_LOOKUP.values()]
