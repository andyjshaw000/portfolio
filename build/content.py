# Case study content for Andy's portfolio. Image IDs are Wix media IDs.

P = "041fc2_"

def m(h, ext="png"):
    return f"{P}{h}~mv2.{ext}"

PROJECTS = [
# ------------------------------------------------------------------ BUNDLING
dict(
  slug="bundling", title="Bundling", cat="research", where="Gopuff", kind="Research",
  thumb=m("ac41818a18824cda8b4a404ed0357459"),
  cover=None,
  card="How should Gopuff sell product bundles? I ran the interviews and concept tests that answered it.",
  impact="Most recommendations shipped in the live app",
  pills=["User interviews", "Concept testing"],
  lede="Gopuff wanted more people buying bundles, and bigger orders when they did. I ran the research that shaped how bundles look and work in the app.",
  facts=[("Role","UX Research Intern"),("When","Summer 2022"),("Team","My mentor, UX designers, product"),("Methods","Interviews, concept testing")],
  outcome="Most of my recommendations made it into the live Gopuff app by August 2023.",
  sections=[
    ("The ask", [
      ("p","Gopuff is an on-demand delivery app. The product team was about to run experiments on bundle color, layout, targeting, and placement, and wanted to know what users actually wanted before spending engineering time."),
      ("p","My job: find out which bundles people liked and what would raise adoption and average order value."),
    ]),
    ("Planning and recruiting", [
      ("p","I wrote the research brief with my mentor, Rebecca Rago, and split the study into two phases: interviews for the why, then concept tests on prototypes for what actually worked."),
      ("p","I wrote the screener and recruited Gopuff and competitor users through userinterviews.com."),
      ("figs",3,[(m("810cd875f8c44409a9bf67fd2a4ea04c"),"Screener"),(m("bd85dc3564ef497dbbe8a97786606c39"),"Participant summary"),(m("f6f2918068434d71b39f5c43ce13ed77"),"userinterviews.com")],"The screener, participant summary, and recruiting platform","3/4",True),
    ]),
    ("Interviews and concept tests", [
      ("p","I interviewed six participants about how they shop, how they use discounts, how bundles should be shown, what should go in them, whether they wanted to customize them, and what kind of discount they'd expect."),
      ("p","Six more people used early interactive prototypes. They found a bundle, added it to their bag, and edited it. Then they compared three designs side by side on looks, ease of use, and where things sat on the screen."),
      ("fig",m("28fc0488b6b94d7cb19a1bf1529b342a"),"The three concepts participants compared"),
      ("fig",m("6fe0994d6e9e4a30b77556215f7ad0a1"),"The proposed flow"),
    ]),
    ("Working with design", [
      ("p","I set the timeline with the UX designers so mockups were ready before each round. People reacted to real screens instead of descriptions."),
      ("figs",2,[(m("28051c756abd4a869329fa521188f450"),"Ideas from brainstorming that didn't make it into testing"),(m("2d3ea2f4ae7040a68be759a19aad766a"),"Screens participants could reach in the prototype")],"","16/10",True),
    ]),
    ("What we learned", [
      ("ul",[
        "<b>A lot of people never noticed bundles.</b> Several said they'd look for them inside categories like Snacks or Grocery, not on the homepage.",
        "<b>People wanted to customize bundles</b> for their own tastes or for an occasion.",
        "<b>The discount had to be obvious.</b> Crossed-out prices and clear labels mattered more than almost anything else.",
        "<b>3 to 6 items felt manageable.</b> Under 5 was the sweet spot unless the discount was big.",
        "<b>\"Add all to bag\" tested well</b>, and color cues on bundled items helped people keep track.",
        "<b>People asked for occasion bundles</b> for parties, holidays, and meal prep.",
      ]),
    ]),
    ("Recommendations and impact", [
      ("p","I wrote a stakeholder report covering discounts, bundle size, use cases, and placement. These were the recommendations:"),
      ("ol",[
        "Tell users when they're a few items away from completing a bundle.",
        "Keep bundles at five items or fewer.",
        "Make \"Add all\" bigger and easier to spot.",
        "Rewrite the carousel header to call out the savings.",
        "Show the bundle subtotal as its own line in the cart.",
        "Mark bundled items in the bag with a color cue on the left.",
      ]),
      ("p","Most of these were in the live app by August 2023."),
    ]),
    ("What I'd do differently", [
      ("p","Keep recruiting titles neutral so participants aren't tipped off, and plan for no-shows from day one."),
      ("p","And leave the guide when someone says something interesting. Some of my best findings came from those detours."),
    ]),
  ],
),
# ------------------------------------------------------------- SAVE FOR LATER
dict(
  slug="save-for-later", title="Save For Later", cat="research", where="Gopuff", kind="Research",
  thumb=m("865fd07f116f49e7a4769ef09fd593ba"),
  cover=m("733ee0ee99064103923f4540bac11fc3"),
  card="People were using their cart as a wishlist, then abandoning it. I researched what a real save-for-later feature should look like.",
  impact="Projected to add $16M in annual revenue",
  pills=["User interviews", "Usability testing"],
  lede="Lots of Gopuff shoppers left items in their cart just to remember them, then never checked out. I looked at whether a Save for Later feature would fit how people actually shop.",
  facts=[("Role","UX Research Intern"),("When","Summer 2022"),("Team","My mentor, stakeholders, UX designers"),("Methods","Interviews, usability testing")],
  outcome="This work on saving items was projected to increase Gopuff's annual revenue by $16M by cutting cart abandonment.",
  sections=[
    ("The ask", [
      ("p","Gopuff wanted to know if a Save for Later feature would fit people's shopping habits, and what would get them to create, organize, and share lists."),
          ]),
    ("Approach", [
      ("p","I combined interviews and usability tests in one 30-minute session, so I got the why and the how from every participant."),
      ("figs",2,[(m("b98e2f2c91ce45a0b9d47404bc6cc689"),"Participant summary"),(m("f6f2918068434d71b39f5c43ce13ed77"),"userinterviews.com")],"","4/3",True),
      ("p","Six people talked through how they shop, why they keep lists in other apps, and what alerts they'd want on saved items."),
      ("p","Then they used a prototype to save items and manage them in a Saved for Later section."),
    ]),
    ("The prototype", [
      ("p","I worked with the UX designers to get mockups ready for testing."),
      ("fig",m("733ee0ee99064103923f4540bac11fc3"),"The prototype participants used"),
      ("fig",m("d130281b13794773ac3ba257a43f9602"),""),
      ("fig",m("099a08049a9b4b748bb712b419f8f252"),""),
      ("figs",3,[(m("5bf596d5601c4726b881f796b1506e3d"),""),(m("306d43b7079e4c229dc2b8fb361d1ac4"),""),(m("6966880fce0d4ab585050c464afca922"),"Favoriting from checkout")],"Other prototype screens","3/4",True),
    ]),
    ("What we learned", [
      ("ul",[
        "<b>People were already using the cart as a list.</b> They parked items to compare them, to buy later, or just to remember them.",
        "<b>Price drives it.</b> Alerts about sales or low stock were the thing most likely to turn a saved item into a purchase.",
        "<b>\"Save for Later,\" \"Favorites,\" and \"Wishlists\" meant different things</b> to people depending on when they planned to buy.",
        "<b>People wanted multiple named lists</b>, clear labels, and quick access to product details.",
        "<b>Sharing mattered</b> for gift ideas, family shopping, and party planning.",
        "<b>One-tap actions were a big deal</b>, like adding to a list or moving something to the cart.",
        "<b>The flag icon confused people.</b> Most didn't know what it did.",
      ]),
    ]),
    ("Recommendations", [
      ("ol",[
        "Show full item details in lists: image, name, specs, price, and price changes.",
        "Let people make multiple named lists.",
        "Keep lists until the user deletes them.",
        "Promote deals on popular items people have saved.",
        "Add sharing and collaboration.",
        "Recommend more items based on what's already in a list.",
        "Replace the flag icon with text or a clearer icon.",
        "Notify people when saved items go on sale or are about to sell out.",
      ]),
    ]),
    ("What I learned", [
      ("p","Timely alerts create urgency, and urgency moves people. One unclear icon can sink a feature. And convenience kept showing up as a top three priority."),
    ]),
  ],
),
# --------------------------------------------------------------- PDP REDESIGN
dict(
  slug="pdp-redesign", title="Product Page Redesign", cat="research", where="Gopuff", kind="Research",
  thumb=m("fe562874bf23461ca57c1bb11e7d16cc"),
  cover=None,
  card="I compared Gopuff's product page against 12 competitors and category leaders to figure out what to fix.",
  impact="Redesigned page went live in August 2023",
  pills=["Competitive analysis", "Stakeholder deck"],
  lede="Gopuff's product display page had accessibility gaps and didn't show products well. Before redesigning it, the team needed to know what good looks like.",
  facts=[("Role","UX Research Intern"),("When","Summer 2022"),("Scope","12 apps reviewed"),("Methods","Competitive analysis")],
  outcome="The redesigned product page concept went live in the Gopuff app in August 2023.",
  sections=[
    ("The ask", [
      ("p","The team wanted a clearer, better-looking product page. I started with a competitive analysis so the redesign was based on evidence, not opinions."),
    ]),
    ("Competitive analysis", [
      ("p","I reviewed Gopuff's current page against 9 direct competitors (Instacart, Shipt, Grubhub/Seamless, Uber Eats, DoorDash, Deliveroo, Foxtrot, Favor, and Drizly) and 3 category leaders (Amazon, Target, and Chewy)."),
      ("p","I scored each on value props, image and text size, layout, and product info, using Baymard Institute's e-commerce research as the benchmark."),
      ("fig",m("0bdf662a62da4aed963e2e9145d48eec"),"Baymard Institute's research set the benchmark for best practices"),
      ("fig",m("fd0cbd6558374f1f89f921142a2cf36f"),"The sheet I used to score each competitor"),
    ]),
    ("What I found", [
      ("ul",[
        "<b>Photos:</b> most apps gave product images a big share of the screen.",
        "<b>Titles:</b> some kept them short, others added count, weight, volume, and brand.",
        "<b>Price and rewards:</b> placement was all over the place. Some led with price, others put rewards right next to it.",
        "<b>Out of stock:</b> some changed the add button to \"Unavailable,\" others showed a message under the header.",
        "<b>Value props:</b> discounts, percent off, popularity, and availability all showed up.",
        "<b>Product info:</b> ranged from full ingredients and nutrition to short, punchy descriptions.",
        "<b>Brand info:</b> some linked it with a subheading, others with a chevron or button.",
        "<b>Alcohol:</b> some apps added ABV, tasting notes, and food pairings.",
      ]),
    ]),
    ("The presentation", [
      ("p","I pulled the findings, insights, and recommendations into a 25-slide deck for stakeholders."),
      ("slider",[m(h,"jpg") for h in ["437dc631ff7f47d0a87cc8b8854c2ac9","124d2fe7467f490297516a781f0f8a35","ea319854cf114fdfb8ea220260ebdb51","4ff43f913b5749429eba90d9732054e4","6a8c044415044afe81ddd8ffed401673","98414eb624af430dbd184abccf6f5115","06dc21bd876f424e902e3fc70bc677e7","2c6c34aaf1f647b6b79a7b814e14c4c2","4a314e79026b4306b1a1228adcf2e1da","95a9bb4727ca4d5d80f698a5575ffa54","33121cf5208b475eb6f5cca2fc42bb86","fe8e975438e040d98ff2dfde753add16","55f650ae8d064d7091a8d4982bf6c822","f70e3949b52f46749a6635a597283471","f753063d072f4db3ac9af117eb6a09aa","d8d5e2a7469645269978628d353b19ab","4f3d765b32134154af4aa08b8334aad6","5be28c1659394a3c8d6023ba28f55ecf","3ad0548f645c4fb9afa457aba218fe62","ea9a2c9baa26488eaaf807f65c0b49dc","7fca119ad4894983b619f6460093d631","9c4efa9a7a174e4f8b84e9914799e795","ba36202c6725414bb3d82a6f5b0eaef0","694350a65f7445839ffaf58850c0b04d","a88ba9fc9593415f97bcff7cde2df068"]],"The deck I presented to stakeholders","16/9"),
    ]),
    ("The outcome", [
      ("p","The research shaped concepts that gave images more space, tightened titles, moved key info where people expected it, and sharpened the value props."),
      ("figs",1,[(m("bf9c46210012449185b5543dd8dcb511"),"The product page concept, live as of August 2023")],"","",True),
    ]),
  ],
),
# --------------------------------------------------------------------- KUOW
dict(
  slug="kuow", title="KUOW Redesign", cat="research design", where="UW Capstone", kind="Research + Design",
  thumb=m("4df59576199e4828a0e88f7415937630"),
  cover=m("3641d9d17e5544b98e158fd87709b3e4"),
  card="Our senior capstone for KUOW public radio. We redesigned the app to win back engagement and reach a younger, more diverse audience.",
  impact="Pitched to judges at the HCDE capstone showcase",
  pills=["Interviews", "Personas", "A/B testing", "Figma"],
  lede="KUOW, the Pacific Northwest's public radio station, had an aging audience and falling app engagement. They sponsored our capstone to keep current listeners and reach a younger, more diverse crowd.",
  facts=[("Context","UW HCDE capstone, sponsored by KUOW"),("When","6 months, 2023"),("My part","Research, design, video prototype"),("Methods","Interviews, personas, IA, A/B testing")],
  outcome="We presented the redesign and a video prototype I produced to a panel of judges at the HCDE capstone showcase.",
  sections=[
    ("Planning", [
      ("p","We set up sponsor check-ins and a project plan that worked a lot like a PRD, with two tracks: redesign the app, and reach people outside it."),
      ("fig",m("3641d9d17e5544b98e158fd87709b3e4"),"Our proposed timeline"),
    ]),
    ("Research", [
      ("p","A previous student team found people were confused by the app's organization and wanted cleaner screens and personalized topics. We built on that instead of starting over."),
      ("p","From 8 research papers: many young people expect news to find them on social media, they still care about credible journalism, and location-aware apps could bring them back to local news."),
      ("p","KUOW actually rated better than other NPR station apps, but it had no offline listening or personalized recommendations."),
      ("fig",m("8e4a3e66a42647ad807f69eadf2304b6"),"The sheet we used to track competitors"),
    ]),
    ("Interviews and usability tests", [
      ("p","We ran 8 sessions with people 18 to 29 and over 30: an interview about news habits, then a usability test on the current app."),
      ("ul",[
        "<b>People pull news from everywhere</b>, mixing news outlets with social media.",
        "<b>Personal relevance matters.</b> Recommendations from friends and family made sources feel more credible.",
        "<b>They wanted plain language</b> and different formats like audio and transcripts.",
        "<b>Notification preferences split.</b> Some wanted constant updates, others wanted a set routine.",
        "<b>Trust is complicated.</b> It came down to fact-checking, citations, and no clickbait.",
      ]),
      ("p","In the current app, people struggled with small text, cramped margins, banners that looked like ads, a confusing Mixtape feature, and no dark mode or accessible reader."),
      ("figs",2,[(m("213cc6118b684e6ca527e89259511357"),"Interview themes"),(m("670d316575424d499023cb4db5715380"),"Usability test themes")],"","16/9",True),
    ]),
    ("Personas, IA, and flows", [
      ("p","We built three personas around the behaviors that mattered most: seeking news versus letting it find you, gathering from many sources versus a few, and how each person decides what to trust."),
      ("figs",3,[(m("aa889a9260964839a713fd4ca47df5d6"),""),(m("a3bd59fbe6db470bba539fb2d1f41a2d"),""),(m("ebed1a147d0c4445a05c1e992b3b29b0"),"")],"Our three personas","16/9",True),
      ("figs",2,[(m("06994d431a8849c98af6d04678924b5e"),"Information architecture"),(m("e0f08f14a41341a38e37f3c3915fc427"),"User flow")],"","4/5",True),
    ]),
    ("Wireframes", [
      ("p","Paper first, then Figma. KUOW's design system arrived late, so we swapped in their colors and icons at the end."),
      ("ul",[
        "<b>Login:</b> profiles, picking interests, and following creators.",
        "<b>News:</b> search, sorting, polls, quizzes, and a scroll-to-top button.",
        "<b>Live radio:</b> a persistent \"Now playing\" bar and shareable clips.",
        "<b>Podcasts:</b> search, filters, and offline downloads.",
        "<b>Profile:</b> notification, interest, and accessibility settings, including dark mode.",
      ]),
      ("figs",2,[(m("360d45ad955847f4868904bae1d08116"),"Paper sketches"),(m("2ec4e7142c0d4ff898ee325f78846836"),"Early login wireframe")],"","4/3",True),
    ]),
    ("Beyond the app", [
      ("p","To reach younger people where they already are, we looked at Instagram and TikTok. KUOW's Instagram felt dated, so we proposed a refresh and a more consistent posting schedule."),
      ("figs",2,[(m("b082386a9aa4485aadae40c7f8f1a12d"),"Mind map from our research"),(m("dc14337efa1246529027a118cd6ec760"),"Current vs. proposed posts")],"","16/9",True),
    ]),
    ("Testing", [
      ("p","We ran usability and A/B tests with 6 participants, comparing the old app with ours and testing the social posts."),
      ("figs",2,[(m("dc4c0d53fc48418882b8fa957c2019bd"),""),(m("5b8a78f03ae64cdba1ea4bf3879e528c"),""),(m("67706a8c83304124bc1d1d39da21b4e0"),""),(m("d24cc844bded418e915d46e210c1c723"),"")],"A/B tests of the old and new designs","16/9",True),
      ("fig",m("ebe3d6fa62134054b25aa68306bd585f","jpg"),"Affinity map of our testing findings"),
      ("p","What we changed based on testing:"),
      ("ul",[
        "<b>Onboarding</b> felt easy but dull, so we added color, cut white space, made touch targets bigger, and added live password checks and social sign-in.",
        "<b>The news feed</b> got card layouts, images, listen buttons, and tappable author names.",
        "<b>Live radio</b> got a more obvious listen button, which two participants asked for.",
        "<b>Podcasts</b> got more varied artwork, new episodes at the top, and a \"continue listening\" row. We cut a \"From KUOW\" section three people found confusing.",
        "<b>Social posts</b> got less text, stronger headlines, more visuals, and small topic tags.",
      ]),
      ("fig",m("25ce0ecf916d4df689df3cc9f7e70892"),"Refined social posts"),
    ]),
    ("Showcase", [
      ("p","We made a poster for the HCDE capstone showcase and pitched the design to a panel of judges. I also produced and filmed a video prototype for our sponsor and the judges."),
      ("figs",1,[(m("976d939b4fe74430a8fba4cc7d6ef61e","jpg"),"Our showcase poster")],"","2/3",True),
      ("p","The closest thing to a real product cycle I had in school: a sponsor, a deadline, and testing that changed our minds more than once."),
    ]),
  ],
),
# ------------------------------------------------------------------ STRELMO
dict(
  slug="strelmo", title="STRELMO", cat="research design", where="UW CSE 440", kind="Research + Design",
  thumb=m("ffc3dd8dd7d948ff8125c08bf8c6c75a","jpg"),
  cover=m("6cb804f0a68a44789ef3d6c94aff2782","jpg"),
  card="The Stress Less Mouse. A mouse with a cortisol sensor and a desktop app that helps students track stress.",
  impact="Shown at the UW Computer Science showcase",
  pills=["Interviews", "Usability testing", "Heuristic analysis", "Figma"],
  lede="STRELMO, the Stress Less Mouse, uses a cortisol sensor developed at UCLA to read stress hormones through sweat. It sends that data to a desktop app so people can see how their stress changes over time.",
  facts=[("Context","UW CSE 440, team project"),("Users","University students"),("Methods","Interviews, usability tests, heuristics"),("Tools","Paper prototypes, Figma")],
  outcome="We presented STRELMO to a panel of judges at a showcase run by the UW Computer Science department.",
  sections=[
    ("The problem", [
      ("p","We started with workplace stress, then narrowed our focus to university students after our first round of research. The plan was to interview UW students, then run heuristic evaluations and usability tests with outside participants."),
    ]),
    ("Interviews", [
      ("p","We interviewed UW students about how they handle stress, how they'd feel about tracking it, and our early ideas, then coded the transcripts for themes."),
      ("figs",4,[(m("7bc724c339894412a0fb42ab146ab5ab","jpg"),""),(m("35c0551af1e24603b09fe27f7624b975","jpg"),""),(m("94f16f5b553540f29cbcaf1c286e3ded","jpg"),""),(m("99c83c1edea64b1da0f1e36e0fea4811","jpg"),"")],"Interview notes","3/4",False),
      ("p","People had very different stressors and ways of coping. They wanted to see patterns over time, they liked routines and reminders, and they needed the information to be simple and clear."),
    ]),
    ("Four concepts", [
      ("ol",[
        "<b>Phone app and cortisol watch</b> that tracks stress, sends alerts, and points to resources.",
        "<b>Cortisol meter</b>, a discreet wearable that flags high-stress moments.",
        "<b>Responsive diary and watch</b> that connects journal entries to stress levels.",
        "<b>Desktop app and cortisol mouse.</b> We picked this one because nothing like it existed, and a mouse has a lot of skin contact during computer work.",
      ]),
      ("figs",2,[(m("ca282a43ec7947288b0a058c1abad8cf"),"Paper prototype of the resources page"),(m("aa745639f4ac47e4869f4c0b7529b1aa"),"Paper prototype of the stats page")],"The first version of the desktop app","3/4",True),
      ("figs",2,[(m("b1edc26cacf040aba097abb4d7e2fdda"),""),(m("24c4db09e07f4a039b7902017f475b24","jpg"),"")],"Storyboards","1/1",True),
    ]),
    ("Usability testing", [
      ("p","We tested realistic tasks like checking your stress, finding a stress-relief activity, and getting around the app. We started with paper prototypes and moved to digital ones. Every issue got a severity rating, and we fixed the critical ones first."),
      ("slider",[m(h,"jpg") for h in ["86b24dd307414737a2558dd1c93ded24","2205ef09a3ac4b9982b18e4b8caae63d","1e284663ace04ac591fa040d442238ff","44986c1f53f748a5a886793801dd05dd","d4c6f0d661574541bb08d2a9d946107c","b7d8207bc0ef47b98eb6c6c957dd4627","2077cabfa41a4a0c83d415120eff7568","2b82fed2b0ab4886b4d1c73f084fa66c","bb04a04cf64e4417adca89536c0c44e2","5e897ace1e05471388e788c54a31e1c9","0893161c6fba4a9cb201a93097cff8cd"]],"The desktop app after usability testing","3/4"),
      ("p","A heuristic evaluation with other students caught more issues, also ranked by severity."),
    ]),
    ("Design process", [
      ("slider",[m(h,"jpg") for h in ["f19c50fb843241e1ac71d235b6eeb5e3","734acf187b7b41e1bc3c2e8426124d88","a11110efb77a4ea68fb99ce9d5f23b8b","8dafb029c3ba4c43b596f9fb9971fced","1e86d49ffd4648ef974c71bad5c65db6","28df8516a29b4e2498532657a47c10f6","81d9fd5f483b47d6910540e3cb405ea3","e2709ed2c1c141819c72ad20341bfd03","1c8dc3679efe4e198dd8e79cd9951c72","be6ef6244cb24be5bdffec430870957f","a7d2746da13e45e1a283f9b0c991d7ca","635975ef4e30403e83269281c6268635","ab5cec75ea524efaa3405d636e9061b0","49590b6053824cceb5e6251a8527ec28","008ae01482cb46129ae3ec8578f579d3"]],"Our design process presentation","16/9"),
    ]),
    ("Final design", [
      ("p","What testing changed:"),
      ("ul",[
        "Added vibration alerts alongside the visual ones.",
        "Made the Stats tab much clearer.",
        "Split Resources into separate Reminders and Activities pages.",
        "Switched to a color palette that works for people with low vision.",
        "Found that the mouse changing color might not get noticed, so we suggested adding sound.",
      ]),
      ("slider",[m(h,"jpg") for h in ["fbec4d3eec034b798725bafb9e84207c","64e859b67ede4d90a68ef0fecc965f6c","c14bfcaa6d1d438ea4010cff50b698eb","0cb347cd7595454b9e411603bf472e1b","839ee12068d243be9529d86cf73c026f","6c19a3c3c21f499eae668e920895b8c7","8e080857ed244fadbcfc2390c0a9b349","7abcdceed77a4d7da349d30b340efe61","0410b0faa2d64fc994bdb06c56a1b0ee","f5266cc985a344e597d153b17d7b3820","5c232b48a2154aa09f6840c10e0759e7","3fbc7657ea00434785e1955d3f6617f2","764bc1c05fa34709baaea576ef6edcf6"]],"The final digital design","4/3"),
    ]),
    ("Showcase", [
      ("figs",1,[(m("73aa6214effa437a834d4e1339b4f42b","jpg"),"Our showcase poster")],"","4/5",True),
      ("p","My first project from a vague problem to a finished design. It got better every time we put it in front of someone new."),
    ]),
  ],
),
# --------------------------------------------------------------- HIKE FINDER
dict(
  slug="hike-finder", title="Hike Finder", cat="design", where="UW HCDE", kind="Design",
  thumb=m("7187013b0a25412189ba593559e07269"),
  cover=m("257c282a2e6243f7b2a857fb5c064541"),
  card="Reworked the Washington Trails Association's mobile hike search and visual system, ending with a full brand book.",
  impact="",
  pills=["Visual design", "Wireframes", "Brand book", "Figma"],
  lede="The Washington Trails Association is a nonprofit that protects and promotes hiking trails across the state. Finding a hike on their mobile site took way too many steps, so I redesigned the flow and refined the visual system.",
  facts=[("Context","UW HCDE"),("When","One quarter"),("Client","Washington Trails Association"),("Tools","Figma")],
  outcome="",
  sections=[
    ("The problem", [
      ("p","I went through the current mobile site and found four big issues. Searching took too many steps, the \"find a hike\" feature was hard to find, the map was hard to use, and you had to read through each hike one at a time."),
      ("p","The primary audience was hikers. The secondary audience was anyone looking for hiking info."),
      ("fig",m("6b000494f713468cb2e1fc62ec65740e"),"The current hike-finding flow on the website"),
    ]),
    ("Design", [
      ("p","My wireframes shortened the search path, put a big \"Find a hike\" button on the home page, and grouped buttons using proximity and order. I leaned on Fitts's law and Hick's law to cut down on friction."),
      ("ul",[
        "<b>Search:</b> clear fields and a toggle to switch to the map.",
        "<b>Results:</b> hikes condensed onto one screen with short summaries and icons.",
        "<b>Visual system:</b> drop shadows to show what's tappable, and a palette that feels friendly, natural, and community-focused.",
      ]),
      ("fig",m("d9e311a325a34065a7e16f03e3533020"),"Low-fidelity wireframes with notes"),
      ("figs",3,[(m("5aed94482cc0401ebd6e672bd8b77067"),"Home"),(m("eccff57465c146878e49c0836b959508"),"Search"),(m("781381c7734d42baa215fb99217cb188"),"Results")],"The new flow in high fidelity","1/2",True),
    ]),
    ("Brand book", [
      ("p","I finished with a brand book covering the logo, colors, type, and the mobile flow. The goal was to turn WTA's mission of getting people out into nature into a visual identity."),
      ("slider",[m(h) for h in ["257c282a2e6243f7b2a857fb5c064541","735d317ce72e4458922b3aecdd07e9e3","9de00ae9c0324ca5a114859ceabc2baa","997b599bc4324806900ca85446206489","b2cae1b4f320411ea1e606a344261d16","0cadc92ac8ec4065876bcc63d1f8a7f9","00a038d371ce4faf9440679b7d18cbb5","7789047792fe40f3b2cdbff0a8ff5e59","e0bcf108a2494429aa3e9955e1928f56","02e1392f9b124df1b8420f932083c628","5581bce546464b02a8c9a69501256f08"]],"The brand book","1294/1000"),
          ]),
  ],
),
# ----------------------------------------------------------- COOKING CENTRAL
dict(
  slug="cooking-central", title="Cooking Central", cat="design", where="UW HCDE", kind="Design",
  thumb=m("395ef3fde3394981bac4b5bbaf78ccba"),
  cover=None,
  card="A cooking app for young adults short on time, money, and skills, with a social side so cooking feels less lonely.",
  impact="",
  pills=["Journey mapping", "Storyboards", "Prototyping", "Figma"],
  lede="A lot of young people see cooking as a chore. They don't have much time, money, or skill, and during the pandemic it got lonely too. Our team designed an app to get people cooking more, and cooking with others.",
  facts=[("Context","UW Intro to User-Centered Design"),("When","2020"),("Team","Team project"),("Tools","Figma, Miro")],
  outcome="",
  sections=[
    ("Research", [
      ("p","We interviewed college students and young adults about cooking. They talked about not knowing what to make, not having the right ingredients, and feeling isolated in the kitchen. We grouped our notes with affinity mapping."),
      ("fig",m("f7e5f496e24c42c5bfba539b95d23805"),"Affinity map from interviews"),
      ("p","We made two personas: someone who's never really cooked, and a beginner who wants to get better."),
      ("figs",2,[(m("be922b9cf3f148de8a1d15161e4cb8e9"),""),(m("a06805a5a13a4276a07dbb42d0df0b5b"),"")],"Our two personas","598/386",True),
      ("p","Then we mapped the whole cooking journey. The low points were deciding what to make with no time, and improvising when an ingredient was missing. The high points were finding an exciting recipe and sharing the result with friends and family."),
      ("fig",m("aacdade61c1a45468c73f79044e87cc2"),"Journey map for Joe, our inexperienced cook"),
    ]),
    ("Design requirements", [
      ("ol",[
        "Show how long each recipe takes.",
        "Find recipes that fit the ingredients you have.",
        "Suggest recipes based on preferences and skill level.",
        "Keep people engaged while cooking, with video or chat.",
        "Give clear steps with visuals.",
        "Explain cooking terms people don't know.",
        "Let people get help from other users.",
        "Let people share photos and recipes.",
      ]),
      ("figs",2,[(m("7c290d4a29eb4930b36902b441036b23"),"Final storyboard"),(m("3fb577e7d44d4b669b390947f1f30ffa"),"Storyboard sketches")],"Two storyboards for different scenarios","3/2",True),
    ]),
    ("Design", [
      ("p","We mapped the app's structure and color-coded the main flows to cut out unnecessary screens. Then we built low-fidelity prototypes in Figma so we could test and change things fast."),
      ("fig",m("fa9d1f3838044fb5b1a1f07e7949867b"),"Information architecture"),
      ("fig",m("c4bcb097839544bfbd8a4463740061c9"),"Low-fidelity prototype"),
      ("fig",m("8b7b764181bb491a9d510893c849efd0"),"Annotated wireframe"),
    ]),
    ("Testing and iteration", [
      ("ul",[
        "<b>Calendar:</b> people liked it but didn't want to set exact meal times. We moved to date-based planning, a weekly view, and a shopping list built from your recipes.",
        "<b>Search:</b> two search icons on the home page confused people, and they wanted filters for meal type, appliances, and more diets.",
        "<b>Social:</b> one person found it messy, another preferred browsing over posting. We redesigned it to support both, borrowing ideas from Reddit.",
      ]),
      ("p","We did this fully remote during the pandemic, which taught me how to keep a team moving when nobody is in the same room."),
    ]),
  ],
),
# --------------------------------------------------------- CELESTIAL NINJA
dict(
  slug="celestial-ninja", title="Celestial Ninja", cat="code", where="UW HCDE 438", kind="Code",
  thumb=m("c9bf43d5129c4ebb83488d9618d4240d"),
  cover=m("a334d56933f24c90a85c5eacc9b6eaca"),
  card="A 2D survival game in JavaScript with five elemental powers, a boss fight, and a live Firebase leaderboard. Playable in the browser.",
  impact="Playable live demo",
  pills=["JavaScript", "p5play", "Firebase"],
  lede="You're a ninja who can bend five elements: fire, earth, water, sun, and air. Shadow warriors keep coming, and they get stronger over time. Kill them, collect XP, and pick an upgrade every few levels.",
  facts=[("Context","UW HCDE 438"),("Built","Solo, 800+ lines"),("Stack","JavaScript, p5play, Firebase"),("Hosting","GitHub Pages")],
  outcome="",
  links=[("Play it live","https://andyjshaw000.github.io/Final438/")],
  sections=[
    ("Getting started", [
      ("p","I'd never used p5play, so I started with its examples to plan the code structure."),
      ("p","Enemy health and speed scale exponentially while the player scales linearly, so the game gets harder the longer you last."),
      ("figs",2,[(m("6321434b3fbb42fc976a400b9698a6e4"),"First XP spawning"),(m("25ec706a599d4c4f82a30757e3bc89d2","gif"),"Enemies chasing the player")],"","8/5",True),
      ("p","Enemies first snapped to the player way too fast because I was using a force that kept increasing. Switching to a constant velocity fixed it."),
      ("figs",2,[(m("4e237ec0c297458f9f99be4222aca8b8","gif"),"Shooting enemies"),(m("e6a2eeda122b419c87f6db949de10be6","gif"),"Enemies with way too much speed")],"","8/5",True),
    ]),
    ("Power-ups and graphics", [
      ("p","The spinning stones were the hardest power-up because they needed unit circle math. The bouncing airball was next, since its direction had to flip at the window edges. Every few levels the game pauses and gives you three random upgrade cards to pick from."),
      ("figs",2,[(m("6204b3bb99ce463cbb8839b1b60a43ca","gif"),"Picking a power-up"),(m("28a17baba0014423a195432cb85bbde5"),"Power-up cards")],"","8/5",True),
      ("p","My own drawings looked rough, so I switched to compressed pixel art. That took a while for animated sprites like the ninja and the rotating water."),
      ("fig",m("93a983b8bd00438c8b5c9c6bd87319ac","gif"),"The first version with real graphics"),
    ]),
    ("Planning round two", [
      ("p","For the second phase, I planned new features on paper: a sword, pause and play-again buttons, new enemy types, a boss, and a Firebase leaderboard. Firebase was the part I was most worried about."),
      ("figs",3,[(m("fdf6758a8cc64a77b585deb9fd08091e","jpg"),""),(m("f6b60c217bcb48a59db454aba1cdd38c","jpg"),""),(m("5383b227c6664dc5b186b3745c488550","jpg"),"")],"Paper plans for the UI and new features","4/3",False),
    ]),
    ("New features", [
      ("p","<b>The sword</b> was the hardest part of the whole project. p5play didn't handle mouse aiming well on a moving canvas, and my first attempt didn't work at all. I ended up attaching a sword sprite to the player and making four rotated animations to match the hitbox."),
      ("figs",2,[(m("39311a1d53ed4ade9f91d46ef24ac228","gif"),"The first sword, which didn't work"),(m("8d264c8e0d5f49a5bb73190e84b861f3","gif"),"The working sword")],"","8/5",True),
      ("p","<b>New enemies.</b> Red enemies are fast and rush you. Purple enemies shoot shadow orbs at you. <b>The boss</b> shows up every five minutes and charges at you in bursts. Getting its timing right took a lot of tuning."),
      ("figs",2,[(m("2f251d41eacc4a8696ebdc09e248349c","gif"),"Red and purple enemies"),(m("63353597481e4253806fcd429e9b624c","gif"),"The five-minute boss")],"","8/5",True),
      ("p","<b>Balancing.</b> I toned down some skills, changed how defense works, and added darkness that closes in over time so enemies are harder to see. I aimed for runs under about 10 minutes."),
      ("figs",2,[(m("419838493f7c4381b47730e7d5f651ab","gif"),"Darkness closing in"),(m("13e62ffc6c6a43efae30e29625d1d88a"),"Play again screen")],"","8/5",True),
      ("p","<b>Live leaderboard.</b> With help from a classmate, I built a Firebase backend for high scores. I added a real-time listener so the top 5 update live, right on the game canvas."),
      ("figs",2,[(m("484d51c290f7475c889d05d24ffd6229","gif"),"Early leaderboard"),(m("c380c2e255134095b6ced3578fce90a7","gif"),"Leaderboard on the canvas")],"","8/5",True),
    ]),
    ("Working with the library's creator", [
      ("p","The game was lagging, so I reached out to Quinton, the creator of p5play. He changed how the library checks collisions, which cut resource use."),
      ("fig",m("f5b91bc92f064f54aa406534ddf87705"),"Talking with p5play's creator"),
      ("p","Friends playtested it and asked to hold the mouse instead of clicking over and over, so I added that. I also made the game pause automatically when you switch tabs."),
      ("fig",m("0fc333adf608415da0e3190403662d34"),"The finished game, with an upgrade tracker in the bottom right"),
    ]),
    ("What I learned", [
      ("p","A week and a half, a new library, and 800+ lines of code. I finished on time, but working out of order cost me time. Next time I'd plan stricter."),
      ("p","If I kept going, I'd add loot that carries between runs, a menu, multiplayer, and a magnet power-up."),
    ]),
  ],
),
# --------------------------------------------------------- RESTAURANT FINDER
dict(
  slug="restaurant-finder", title="Restaurant Finder", cat="code", where="UW HCDE", kind="Code",
  thumb=m("056c4875bf1545e7bc72d93214dc2b9b"),
  cover=m("35594dc7958d442cb5eb68fcd17642c8"),
  card="A Python and Flask web app that maps nearby restaurants with color-coded ratings, using the Yelp Fusion API.",
  impact="",
  pills=["Python", "Flask", "Folium", "Yelp API"],
  lede="I like food and I like code, so I built a web app that pulls restaurant data from Yelp and puts it on an interactive map. Search for something, and you get every nearby spot color-coded by rating.",
  facts=[("Context","UW HCDE"),("Built","Solo"),("Stack","Python, Flask, Folium"),("Data","Yelp Fusion API")],
  outcome="",
  links=[("Live demo","https://andyjshaw000.pythonanywhere.com/")],
  sections=[
    ("Planning", [
      ("p","This was my first time using Python. I planned three core features: search, ratings and reviews, and an interactive map. I chose Yelp Fusion for the data, Flask for the web app, Folium for the map, and the Google Maps API for a better map experience."),
      ("figs",2,[(m("f3b026c2024542e892d271266e9ead0f"),"My Python skills going in"),(m("f9c4f6ca0c3f46d1b083a43b9cb0c888"),"My to-do list")],"","16/9",True),
      ("p","The must-haves were the map and getting it deployed. Colors, marker sizes, tooltips, and a moving map were next."),
      ("fig",m("04c39d24a14a4c60913cd16f34fe57e8"),"A map I found that inspired my design"),
    ]),
    ("Building it", [
      ("p","<b>Getting enough data.</b> Yelp only returns 50 restaurants per request. I made multiple requests with different offsets and saved the results to a CSV, so the map shows every restaurant nearby."),
      ("p","<b>Search.</b> Flask takes what you type and sends it to the Yelp API as a parameter."),
      ("fig",m("620d98aee1f84f888ae0d0ed6110d0b7"),"The search bar"),
      ("p","<b>The map.</b> Markers are color-coded by rating so you can spot the good places fast. Click one and you get the rating, review count, and a review snippet. You can pan, zoom, and drag around the area."),
      ("fig",m("35594dc7958d442cb5eb68fcd17642c8"),"The map after a search"),
      ("fig",m("36ed98dee17a44e9b2a1debec393d91c"),"The popup when you click a restaurant"),
    ]),
    ("Deploying it", [
      ("p","Deploying to PythonAnywhere meant reworking my Flask routing to fit its setup."),
      ("fig",m("54ee7c8042cb465e8484c3582ee847d0"),"The Google Maps API key expired in August 2023, so the live map may not fully load"),
      ("p","Going in, I'd never written Python. Coming out, I'd used HTTP requests, parsed JSON, built a Flask app, and shipped it to the web."),
    ]),
  ],
),
# ---------------------------------------------------------------- SIMON SAYS
dict(
  slug="simon-says", title="Simon Says", cat="code", where="UW HCDE", kind="Hardware",
  thumb=m("82f67276b86c4ce6bef7008c791951bc"),
  cover=m("3d2d10d23082403382f286cef8f573ae"),
  card="A physical Simon Says memory game I wired up with arcade buttons, LEDs, and an Arduino in one week.",
  impact="",
  pills=["Arduino", "Circuit design"],
  lede="An electronic Simon Says. The game flashes a sequence of lights, you repeat it on arcade buttons, and it gets longer every round. I had one week to design, build, and present it.",
  facts=[("Context","UW HCDE"),("When","One week"),("Built","Solo"),("Hardware","Arduino, arcade buttons, LEDs")],
  outcome="",
  sections=[
    ("The plan", [
      ("p","One week for concept, design, build, and presentation meant I had to plan tightly:"),
      ("ul",[
        "<b>Day 1:</b> code that generates and tracks a random button order.",
        "<b>Day 3:</b> the circuit, with a start button and arcade buttons.",
        "<b>Day 4:</b> a working prototype, with a buzzer and score screen as stretch goals.",
        "<b>Day 6:</b> final presentation and documentation.",
      ]),
      ("p","I had to rewire arcade buttons from Amazon, which meant learning the components and pin layouts fast."),
    ]),
    ("Design and build", [
      ("p","I diagrammed the circuit and paired each button with its matching LED, so the light cues lined up with gameplay. Everything went in a cardboard box with holes cut for the buttons. The Arduino and breadboard sat hidden inside, so players only saw the game."),
      ("figs",2,[(m("1799ee68c4904d20a347e3bade9a738f"),"Circuit diagram"),(m("31a6e482301743f58cc010a4791d72b6"),"The raw circuit with arcade buttons")],"","4/3",True),
      ("figs",2,[(m("2703ea0b00d2408c83c01e3b1fc8abf3"),"The shell"),(m("3d2d10d23082403382f286cef8f573ae"),"The finished game")],"","3/4",True),
      ("p","The code is split into functions for generating the sequence, flashing the LEDs, playing sounds, checking input, and moving to the next round. Each button also has its own buzz, so the game works for people who can't see the lights."),
    ]),
    ("Demo", [
      ("fig",m("2975e9d3a049401aa7e08c0e5f002271","gif"),"A demo video I filmed of the game"),
      ("p","The hardest part was keeping the sequence, button presses, and LED feedback in sync. The tight timeline also taught me to stop polishing and ship."),
    ]),
  ],
),
]

ORDER = ["bundling","save-for-later","pdp-redesign","kuow","strelmo","hike-finder","cooking-central","celestial-ninja","restaurant-finder","simon-says"]

TLDR = {
  "bundling": ("Bundles weren't driving orders, and the team didn't know why.",
               "Ran 12 sessions (6 interviews, 6 concept tests) on prototypes built with design.",
               "6 recommendations. Most were live in the app by August 2023."),
  "save-for-later": ("Shoppers used the cart as a wishlist, then abandoned it.",
               "Ran 6 combined interview and usability sessions on a save-for-later prototype.",
               "8 recommendations. The work was projected to add $16M a year."),
  "pdp-redesign": ("The product page had accessibility gaps and sold products poorly.",
               "Benchmarked 12 apps against Baymard research and presented a 25-slide deck.",
               "The redesigned page went live in August 2023."),
  "kuow": ("KUOW's audience was aging and app engagement was falling.",
               "Lit review, 8 interviews, 3 personas, IA, Figma redesign, A/B tests with 6 people. I made the video prototype.",
               "A full app redesign and social strategy, pitched to the sponsor and judges."),
  "strelmo": ("Students had no easy way to see how stressed they really were.",
               "Interviews, 4 concepts, paper and digital prototypes, usability tests, heuristic evaluation.",
               "A final design shown at the UW Computer Science showcase."),
  "hike-finder": ("Finding a hike on WTA's mobile site took too many steps.",
               "Audited the flow, redesigned search and results, and built a brand book.",
               "A shorter flow with every result on one screen."),
  "cooking-central": ("Young adults see cooking as a chore, and a lonely one.",
               "Interviews, personas, a journey map, 8 requirements, Figma prototypes, and testing.",
               "An app with meal planning, search by ingredients, and a social feed."),
  "celestial-ninja": ("Build a full game in a library I'd never used, in a week and a half.",
               "800+ lines of JavaScript: 5 powers, a boss, and a live Firebase leaderboard.",
               "Shipped on time and playable in the browser."),
  "restaurant-finder": ("I wanted a faster way to see which nearby restaurants are good.",
               "My first Python project: Flask, Folium, and the Yelp API, paginated past its 50-result cap.",
               "A deployed web app with a color-coded restaurant map."),
  "simon-says": ("Design, build, and present a hardware game in one week.",
               "Circuit design, Arduino code, a cardboard enclosure, and sound cues for accessibility.",
               "A working game and demo video, on schedule."),
}
