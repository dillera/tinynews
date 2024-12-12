# tinynews
Pull down tiny news feeds for fun and Fujinet

## Setup
Use venv for packages:

python -m venv .venv
source .venv/bin/activate
pip install flask
pip install requests

## Run

```
$ flask run --debug
```

## Request

```
http://127.0.0.1:5000/news
```

### Sample Response

```
{
  "news": [
    {
      "description": "Mike Whitaker says he will step down as head of the Federal Aviation Administration on Jan. 20. It's not unusual for FAA administrators to resign at the change of administration, though some have stayed longer.",
      "link": "https://www.npr.org/2024/12/12/nx-s1-5226796/faa-head-resign-mike-whitaker-january-boeing",
      "published": "Thu, 12 Dec 2024 11:35:59 -0500",
      "title": "FAA chief Mike Whitaker announces that he will step down in January"
    },
    {
      "description": "In a wide-ranging and long interview, President-elect Donald Trump tells TIME Magazine his priorities for the first days of his second time at the presidency. ",
      "link": "https://www.npr.org/2024/12/12/g-s1-37896/trump-time-person-of-the-year-agenda-priorities-january-6-immigration",
      "published": "Thu, 12 Dec 2024 10:50:36 -0500",
      "title": "As Time's 'Person of the Year,' Trump outlines his top priorities in lengthy interview"
    },
    {
      "description": "The 29-year-old said he was detained earlier this year after crossing into Syria on foot from Lebanon and held in prison until the fall of Assad. Timmerman's family called it a \"Christmas miracle.\"",
      "link": "https://www.npr.org/2024/12/12/nx-s1-5226745/missing-american-travis-timmerman-found-wandering-barefoot-outside-damascus",
      "published": "Thu, 12 Dec 2024 10:36:30 -0500",
      "title": "Missing American Travis Timmerman found wandering barefoot outside Damascus"
    },
    {
      "description": "Biden said he plans to take more steps using his clemency powers in the remaining weeks of his presidency.",
      "link": "https://www.npr.org/2024/12/12/nx-s1-5226683/biden-commutations-pardons",
      "published": "Thu, 12 Dec 2024 08:11:13 -0500",
      "title": "Biden commutes sentences for 1,500 people, the largest act of clemency in a day"
    },
    {
      "description": "Why FBI Director Christopher Wray will step down from the role at the end of Biden's term. And, the UHC CEO killing turns public attention to the U.S. life expectancy and health care.",
      "link": "https://www.npr.org/2024/12/12/g-s1-37879/up-first-newsletter-fbi-director-christopher-wray-luigi-mangione-health-care-life-expectancy",
      "published": "Thu, 12 Dec 2024 07:58:23 -0500",
      "title": "FBI Director to resign. And, UHC CEO killing brings attention to U.S. life expectancy"
    },
    {
      "description": "Germany hosts almost a million Syrians who fled war and dictatorship. The toppling of the Assad regime has raised questions for exiles about their next step.",
      "link": "https://www.npr.org/2024/12/12/nx-s1-5225799/syria-syrian-refugees-germany",
      "published": "Thu, 12 Dec 2024 07:14:18 -0500",
      "title": "She fled during Assad's regime. Now this Syrian activist is considering going home"
    },
    {
      "description": "In an address to the nation, President Yoon Suk Yeol claimed the opposition-controlled parliament has been destroying the country's liberal democratic order.",
      "link": "https://www.npr.org/2024/12/12/g-s1-37854/south-korea-yoon-martial-law",
      "published": "Thu, 12 Dec 2024 06:01:23 -0500",
      "title": "South Korea's Yoon defends martial law decree as an act of governance"
    },
    {
      "description": "The Geminids are one of the best and most visible annual meteor showers, when at least 120 meteors can usually be seen per hour. But 2024 will be different, thanks to the year's final full moon.",
      "link": "https://www.npr.org/2024/12/11/nx-s1-5223397/geminids-meteor-shower-peak",
      "published": "Thu, 12 Dec 2024 06:00:00 -0500",
      "title": "The Geminids meteor shower peaks this week. Here's what to expect"
    },
    {
      "description": "Scientists have identified two types of brain cells in the abdomen that appear to control different aspects of digestion.",
      "link": "https://www.npr.org/2024/12/12/nx-s1-5225375/these-neurons-in-the-abdomen-help-form-the-gut-brain-connection",
      "published": "Thu, 12 Dec 2024 05:00:00 -0500",
      "title": "These neurons in the abdomen help form the gut-brain connection"
    },
    {
      "description": "The man charged in the killing of UnitedHealthcare CEO Brian Thompson was critical of U.S. health care. Experts say the system's problems are complex and can't be pinned on one player or industry.",
      "link": "https://www.npr.org/sections/shots-health-news/2024/12/12/nx-s1-5224139/mangione-uhc-brian-thompson-shooting-health-care",
      "published": "Thu, 12 Dec 2024 05:00:00 -0500",
      "title": "UHC murder suspect railed about U.S. health care. Here's what he missed"
    }
  ]
}

```